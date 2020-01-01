#
# @file MetaAI.py
# @brief メタAI
#

import random
from threading import Lock

from .ObjectRegionDirectorBase import ObjectRegionDirectorBase

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

        MetaAI._instance = self
    # def __init__

    def update(self, objects, center_pos):
        new_object_list = [obj for obj in objects if obj.is_dead() == False]
        
        super().update(new_object_list, center_pos)

        add_objects = self._generate(objects)
        for obj in add_objects:
            new_object_list.append(obj)

        return new_object_list

    def _update_region(self, objs_in_region):
        pass
    # def update

    def _generate(self, objects):
        add_objects = []

        if len(self._register_list) > 0:
            for obj in self._register_list:
                add_objects.append(obj)
            self._register_list.clear()

        self._count = self._count + 1
        if self._count < 300:
            return add_objects
        else:
            self._count = 0

        add_objects += self._generate_food(objects)
        add_objects += self._generate_enemy(objects)

        return add_objects
    # def _generate

    def _generate_enemy(self, objects):
        add_objects = []

        if len(objects) > 7:
            return add_objects

        import random
        object = Object.Object("SampleEnemy")
        object.reset_pos((100 + random.randint(-50, 50), 0, 100 + random.randint(-50, 50)))
        add_objects.append(object)

        return add_objects
    # def _generate_enemy

    def _generate_food(self, objects):
        add_objects = []

        if len(objects) > 7:
            return add_objects

        for tree in self._tree_list:
            tree_ai = tree.get_game_logic_component("ObjectControl")
            tree_ai.set_nut_interval(int(random.randint(0, 100))) # 性質を無視して実をなるように仮実装

        return add_objects
    # def _generate_food

    def _register_generate_object(self, obj):
        if self._lock.acquire():
            self._register_list.append(obj)
            self._lock.release()
        # lock
    # def _register_generate_object

    def _regist_as_tree_object(self, obj):
        if self._lock.acquire():
            self._tree_list.append(obj)
            self._lock.release()
    # def regist_as_tree_object

    @classmethod
    def generate_object(cls, object_name, pos):
        obj = Object.Object(object_name)
        obj.reset_pos(pos)
        MetaAI._instance._register_generate_object(obj)
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
