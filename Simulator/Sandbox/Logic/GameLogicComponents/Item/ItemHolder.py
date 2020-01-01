# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ItemHolder.py
# @note

from Logic.System.MetaAI import MetaAI

import numpy as np

class ItemHolder:

    def __init__(self):
        self._items = {}
        self._is_item_get_action = False
    # def __init__

    def is_item_get_action(self):
        return self._is_item_get_action
    # def is_item_get_action

    def set_is_item_get_action(self):
        self._is_item_get_action = True
    # def set_is_item_get_action

    def reset_flags(self):
        self._is_item_get_action = False
    # def reset_flags

    def add_item(self, item_name):
        if self._items.get(item_name) == None:
            self._items[item_name] = 0
        self._items[item_name] += 1
    # def add_item

    def use_item(self, item_name, target):
        item_num = self._items.get(item_name)
        if item_num == None or item_num <= 0:
            return False
        self._items[item_name] -= 1

        item_param = self._get_item_param(item_name)
        item_effect = item_param.get("Effect")
        if item_effect.get("Dulability") != None:
            life_component = target.get_object_component("Life")
            if life_component != None:
                life_component.add_life(item_effect["Dulability"])
        # Dulability
        if item_effect.get("GenerateItem") != None:
            target_item_holder = target.get_game_logic_component("ItemHolder")
            if target_item_holder != None:
                target_item_holder.add_item(item_effect["GenerateItem"])
        # GenerateItem
        if item_effect.get("GenerateActor") != None:
            actor_name = item_effect.get("GenerateActor").get("Actor")
            offset_setting = item_effect.get("GenerateActor").get("Offset")
            print(offset_setting)
            offset = np.array([offset_setting.get("X"), offset_setting.get("Y"), offset_setting.get("Z")])
            MetaAI.generate_object(actor_name, target.get_pos() + offset)

        return True
    # def use_item

    def update(self):
        pass

    def post_update(self):
        pass

    def _get_item_param(self, item_name):
        import os, json
        item_jsons_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "Data", "Item"))
        item_json = os.path.join(item_jsons_dir, ("%s.Item.json" % item_name))
        item_param = None
        with open(item_json) as f:
            item_param = json.load(f)
        return item_param
    # def _get_item_param

# class ItemHolder

if __name__ == "__main__":
    pass
