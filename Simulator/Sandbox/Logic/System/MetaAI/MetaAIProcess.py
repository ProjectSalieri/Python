# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MetaAIProcess.py
# @note

import multiprocessing
import time
import signal

import Object

class MetaAIProcess(multiprocessing.Process):

    PROCESS_MSG_QUEUE_EMPTY = "QueueIsEmpty"
    PROCESS_MSG_QUEUE_END = "QueueEnd"

    def __init__(self, queue, result_queue):
        multiprocessing.Process.__init__(self)
        self._queue = queue
        self._result_queue = result_queue

        self._object_status = {}
        self._player_status = {}

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

        for object_id, status in self._object_status.items():
            pass
            #print("ObjectStatus : %s %s" % (object_id, status))
        for object_id, status in self._player_status.items():
            print("PlayerStatus : %s" % object_id)
            print(status)


        self._result_queue.put(MetaAIProcess.PROCESS_MSG_QUEUE_EMPTY)
        
    # def _update_frame

    def _parse_log(self, log):
        header = log.get_header()

        if header == "ObjectStatus":
            self._parse_log_object_status(log)
        elif header == "DeadObject":
            self._parse_log_dead_object(log)

    def _parse_log_object_status(self, log):
        is_player = log.get_content_hash()["Name"] == "Player"
        life = log.get_content_hash()["Life"]
        pos = log.get_content_hash()["Pos"]
        object_id = log.get_content_hash()["ObjectId"]

        status = {
            "Life" : life,
            "Pos" : pos,
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
    # def _parse_dead_object

    def _signal_handler(self, signum, frame):
        self._is_end = True
    # def _signal_handler

# class MetaAIProcess

