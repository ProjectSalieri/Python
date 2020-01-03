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
        import os, signal
        os.kill(self._process.pid, signal.SIGTERM)
    # def shutdown

    def update(self, objects, center_pos):
        new_object_list = [obj for obj in objects if obj.is_dead() == False]

        if self._result_queue.empty() == False:
            process_result = self._result_queue.get()
            if process_result == MetaAIProcess.PROCESS_MSG_QUEUE_EMPTY:
                self._logger.flush(self._queue)
        
        super().update(new_object_list, center_pos)

        add_objects = self._generate(objects)
        for obj in add_objects:
            new_object_list.append(obj)

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

    def _generate(self, objects):
        add_objects = []

        self._count = self._count + 1
        if self._count < 300:
            pass
        else:
            self._count = 0
            self._generate_food(objects)
            self._generate_enemy(objects)

        # 生成したオブジェクトを更新リストに登録
        if len(self._register_list) > 0:
            for obj in self._register_list:
                add_objects.append(obj)
            self._register_list.clear()

        return add_objects
    # def _generate

    def _generate_enemy(self, objects):
        if len(objects) > 7:
            return False

        import random
        obj = self.generate_object("SampleEnemy", (100 + random.randint(-50, 50), 0, 100 + random.randint(-50, 50)))

        return True
    # def _generate_enemy

    def _generate_food(self, objects):
        is_player_hungry = False
        for player in self._player_list:
            life_componet = player.get_object_component("Life")
            if life_componet.get_dulability() < 17000:
                is_player_hungry = True

        if is_player_hungry:
            pass # プレイヤーがピンチならオブジェクト数を無視
        elif len(objects) > 7:
            return False

        for tree in self._tree_list:
            tree_ai = tree.get_game_logic_component("ObjectControl")
            tree_ai.set_nut_interval(int(random.randint(0, 100))) # 性質を無視して実をなるように仮実装

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
