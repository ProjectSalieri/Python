# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MetaAIProcess.py
# @note

import multiprocessing
import time
import signal
import numpy as np

import Object

class MetaAIProcessOrder:

    ORDER_GENERATE_TREE_FOOD = "GenerateTreeFood"

    def __init__(self, order, object_id):
        self._order = order
        self._object_id = object_id
    # def __init__

    def get_order(self):
        return self._order

    def get_object_id(self):
        return self._object_id

# class MetaAIProcessOrder

class MetaAIProcess(multiprocessing.Process):

    PROCESS_MSG_QUEUE_EMPTY = "QueueIsEmpty"
    PROCESS_MSG_QUEUE_END = "QueueEnd"

    def __init__(self, queue, result_queue):
        multiprocessing.Process.__init__(self)
        self._queue = queue
        self._result_queue = result_queue

        self._object_status = {}
        self._player_status = {}
        self._tree_list = {}

        self._is_end = False
        signal.signal(signal.SIGTERM, self._signal_handler)
    # def __init__

    def run(self):
        msec_per_frame = 10000.0 # 処理しなかったときに10秒後に確認
        while self._is_end == False:
            frame_start = time.time()

            self._update_frame()

            frame_end = time.time()
            sleep_time_ms = msec_per_frame - (frame_end-frame_start)*1000.0
            if sleep_time_ms > 0:
                time.sleep(sleep_time_ms/1000.0)
    # def run

    def _update_frame(self):
        if self._queue.empty() == True:
            self._result_queue.put(MetaAIProcess.PROCESS_MSG_QUEUE_EMPTY)
            return True

        while True:
            log = self._queue.get()
            if log == None:
                break
            # queueを共有しているのでemptyだと正確なemptyがわからない
            if log == MetaAIProcess.PROCESS_MSG_QUEUE_END:
                break
            
            self._parse_log(log)
            #print("[Time:%s] %s : %s" % (log.get_content_hash()["LogTime"], log.get_header(), log.get_content_hash()))
            #print("LogTime:   %s" % (log.get_content_hash()["LogTime"]))
            #import datetime
            #print("ReciveTime:%s" % (datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')))
        # while queue

        #self._debug_print()

        self._generate_tree_food()

        self._result_queue.put(MetaAIProcess.PROCESS_MSG_QUEUE_EMPTY)
        
    # def _update_frame

    def _generate_tree_food(self):
        is_player_pinch = False
        pinch_player_pos = None
        for object_id, status in self._player_status.items():
            if status["Life"] < 17000:
                is_player_pinch = True
                pinch_player_pos = np.array(status["Pos"])
        # for _player_status
        if is_player_pinch == True:
            nearest_tree_dist = 10000000.0
            nearest_tree_id = None
            for object_id, value in self._tree_list.items():
                if self._object_status.get(object_id) == None:
                    continue
                tree_pos = np.array(self._object_status[object_id]["Pos"])
                dist = np.linalg.norm((tree_pos - pinch_player_pos))
                if dist < nearest_tree_dist:
                    nearest_tree_dist = dist
                    nearest_tree_id = object_id
                # if dist
            # for _tree_list
            if nearest_tree_id != None:
                print("[MetaAIProcess]%s" % (MetaAIProcessOrder.ORDER_GENERATE_TREE_FOOD))
                self._result_queue.put(MetaAIProcessOrder(MetaAIProcessOrder.ORDER_GENERATE_TREE_FOOD, nearest_tree_id))
    # def _generate_tree

    def _parse_log(self, log):
        header = log.get_header()

        if header == "ObjectStatus":
            self._parse_log_object_status(log)
        elif header == "DeadObject":
            self._parse_log_dead_object(log)
        elif header == "GenerateTree":
            self._parse_log_generate_tree(log)
        elif header == "GenerateObject":
            pass
        elif header == "GetItem":
            pass
        elif header == "UseItem":
            pass
        else:
            print("[MetaAIProcess]Not Implemented Log Header:%s" % (header))

    def _parse_log_object_status(self, log):
        is_player = log.get_content_hash()["Name"] == "Player"
        life = log.get_content_hash()["Life"]
        pos = log.get_content_hash()["Pos"]
        object_id = log.get_content_hash()["ObjectId"]

        status = {
            "Life" : life,
            "Pos" : pos,
            "Name" : log.get_content_hash()["Name"]
        }
        self._object_status[object_id] = status
        if is_player == True:
            self._player_status[object_id] = status
    # def _parse_log_object_status

    def _parse_log_dead_object(self, log):
        object_id = log.get_content_hash()["ObjectId"]
        # ObjectIdのStatus情報削除
        if self._object_status.get(object_id) != None:
            del(self._object_status[object_id])
        if self._tree_list.get(object_id) != None:
            del(self._tree_list[object_id])
    # def _parse_dead_object

    def _parse_log_generate_tree(self, log):
        object_id = log.get_content_hash()["ObjectId"]
        self._tree_list[object_id] = True
    # def _parse_log_generate_tree

    def _signal_handler(self, signum, frame):
        print("[MetaAIProcess]_signal_handler:%d" % (signum))
        self._is_end = True
    # def _signal_handler

    def _debug_print(self):
        for object_id, status in self._object_status.items():
            print("ObjectStatus : %s %s" % (object_id, status))
        for object_id, value in self._tree_list.items():
            print("TreeList : %s" % (object_id))
        for object_id, status in self._player_status.items():
            print("PlayerStatus : %s" % object_id)
            print(status)

# class MetaAIProcess

