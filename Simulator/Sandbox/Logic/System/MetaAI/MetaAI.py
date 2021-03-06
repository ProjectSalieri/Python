#
# @file MetaAI.py
# @brief メタAIp
#

import random
from threading import Lock
import multiprocessing

from ..ObjectRegionDirectorBase import ObjectRegionDirectorBase
from ..Logger.PlayLogger import PlayLogger
from ..Logger.PlayLogger import PlayLog

from .MetaAILogger import MetaAILogger
from .MetaAIProcess import MetaAIProcess
from .MetaAIProcessOrder import MetaAIProcessOrder

import Object

class MetaAI(ObjectRegionDirectorBase):

    _instance = None

    def __init__(self):
        super().__init__()

        self._count = 0
        self._lock = Lock()
        self._register_list = []

        #
        self._tree_list = []
        #
        self._player_list = []

        self._logger = MetaAILogger()
        PlayLogger.add_logger(self._logger)

        self._queue = multiprocessing.Queue()
        self._result_queue = multiprocessing.Queue()
        self._process = MetaAIProcess(self._queue, self._result_queue)
        self._process.daemon = True
        self._process.start()

        MetaAI._instance = self
    # def __init__

    def shutdown(self):
        print("[MetaAI]shutdown start")
        
        import os, signal
        print("[MetaAI]MainProcess : %d" % (os.getpid()))
        print("[MetaAI]SubProcess : %d" % (self._process.pid))
        os.kill(self._process.pid, signal.SIGTERM)
        print("[MetaAI]Wait for SubProcess end")
        self._process.join()
        print("[MetaAI]shutdown end")
    # def shutdown

    def update(self, objects, center_pos):
        new_object_list = [obj for obj in objects if obj.is_dead() == False]

        if self._result_queue.empty() == False:
            process_result = self._result_queue.get()
            if process_result == None:
                pass
            elif process_result == MetaAIProcess.PROCESS_MSG_QUEUE_EMPTY:
                self._logger.flush(self._queue)
            elif process_result.get_order() == MetaAIProcessOrder.ORDER_GENERATE_TREE_FOOD:
                self._generate_food(process_result.get_object_id())
            elif process_result.get_order() == MetaAIProcessOrder.ORDER_GENERATE_ENEMY:
                self._generate_enemy(process_result.get_option().get("Name"), process_result.get_option().get("Pos"))
        
        super().update(new_object_list, center_pos)

        # 生成されたアクターを更新リストに登録
        if len(self._register_list) > 0:
            for obj in self._register_list:
                new_object_list.append(obj)
            self._register_list.clear()

        # 現在状態のログ送信
        for obj in new_object_list:
            PlayLogger.put_as_object_status(obj)

        # 死因ログ解析
        dead_objects = [obj for obj in objects if obj.is_dead() == True]
        for dead_obj in dead_objects:
            # システム管理外の死亡要因
            if dead_obj.get_object_component("Life") != None and dead_obj.get_object_component("Life").is_dead() == True:
                # Life枯渇
                PlayLogger.put_as_dead_object(dead_obj, "LifeDead")
                
            
        return new_object_list

    def _update_region(self, objs_in_region):
        pass
    # def update

    def _generate_enemy(self, name, appear_pos):
        print("[MetaAI]%s" % (name))
        obj = self.generate_object(name, appear_pos)
        return obj
    # def _generate_enemy

    def _generate_food(self, tree_object_id):
        for tree in self._tree_list:
            if tree.get_object_id() != tree_object_id:
                continue
            tree_ai = tree.get_game_logic_component("ObjectControl")
            tree_ai.set_nut_interval(int(random.randint(0, 100))) # 性質を無視して実をなるように仮実装
            print("[MetaAI]generate_food:%s" % (tree_object_id))

        return True
    # def _generate_food

    def _regist_player_object(self, player):
        if self._lock.acquire():
            self._player_list.append(player)
            self._lock.release()

    def _register_generate_object(self, obj):
        if self._lock.acquire():
            self._register_list.append(obj)
            PlayLogger.put_as_generate_object(obj)
            
            self._lock.release()
        # lock
    # def _register_generate_object

    def _regist_as_tree_object(self, obj):
        if self._lock.acquire():
            self._tree_list.append(obj)
            self._logger.put(PlayLog("GenerateTree", PlayLog.get_object_common_content(obj)))
            self._lock.release()
    # def regist_as_tree_object

    @classmethod
    def regist_player_object(cls, player):
        MetaAI._instance._regist_player_object(player)
    # def regist_player_object

    @classmethod
    def generate_object(cls, object_name, pos):
        obj = Object.Object(object_name)
        obj.reset_pos(pos)
        MetaAI._instance._register_generate_object(obj)
        return obj
    # def generate_object

    @classmethod
    def regist_as_tree_object(cls, obj):
        MetaAI._instance._regist_as_tree_object(obj)
    # def regist_as_tree_object
'''
    def get_instance(cls):
        return MetaAI._instance
    # def get_instance
'''

if __name__ == "__main__":
    pass
