# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ItemDirector.py
# @note

import math
import numpy as np

from .ObjectRegionDirectorBase import ObjectRegionDirectorBase

from Logic.System.Logger.PlayLogger import PlayLogger

class ItemDirector(ObjectRegionDirectorBase):

    def __init__(self):
        super().__init__()
        self._item_holdable_objects = []
    # def __init__

    def _update_region(self, objs_in_region):
        for obj1 in objs_in_region:
            item_holder = obj1.get_game_logic_component("ItemHolder")
            if item_holder == None:
                continue

            for obj2 in objs_in_region:
                if obj1 == obj2:
                    continue
                self._try_get_item(obj1, obj2)

            
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

        item_component = obj2.get_game_logic_component("Item")
        if item_component == None:
            return False
        if item_component.is_enable_get() == False:
            return False

        diff = obj1.get_pos() - obj2.get_pos()
        dist = np.linalg.norm(diff)

        # 仮実装
        if dist > 50:
            return False

        item_name = item_component.get_item_name()
        obj2.kill()
        PlayLogger.put_as_dead_object(obj2, "ItemGet")

        item_holder.add_item(item_name)
        PlayLogger.put_as_get_item(item_name, obj1)
    # def _try_get_item

        
        

# class ItemDirector

if __name__ == "__main__":
    pass
