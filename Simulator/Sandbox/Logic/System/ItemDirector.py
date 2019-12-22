# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ItemDirector.py
# @note

import math
import numpy as np

from .ObjectRegionDirectorBase import ObjectRegionDirectorBase

class ItemDirector(ObjectRegionDirectorBase):

    def __init__(self):
        super().__init__()
        self._item_holdable_objects = []
    # def __init__

    def add_item_holdable_object(self, obj):
        self._item_holdable_objects.append(obj)
    # add_item_holdable_object

    def _update_region(self, objs_in_region):
        for obj1 in objs_in_region:
            if obj1 in self._item_holdable_objects == False:
                continue

            for obj2 in objs_in_region:
                if obj1 == obj2:
                    continue
                self._try_get_item(obj1, obj2)

            item_holder = obj1.get_game_logic_component("ItemHolder")
            if item_holder != None:
                item_holder.reset_flags()
            
        # for objs_in_region
    # def _update_region

    def _try_get_item(self, obj1, obj2):
        item_holder = obj1.get_game_logic_component("ItemHolder")
        if item_holder == None:
            return False

        if item_holder.is_item_get_action() == False:
            return False

        print("get item")
        item = obj2.get_game_logic_component("Item")

        diff = obj1.get_pos() - obj2.get_pos()
        dist = np.linalg.norm(diff)

        # 仮実装
        if dist > 50:
            return False

        item_holder.add_item(item)

    # def _try_get_item

        
        

# class ItemDirector

if __name__ == "__main__":
    pass
