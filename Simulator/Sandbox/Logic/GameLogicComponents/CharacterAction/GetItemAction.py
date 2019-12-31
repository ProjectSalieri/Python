# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file GetItemAction
# @note

#from Logic.GameLogicComponents.Item import ItemHolder
from ..Item import ItemHolder

class GetItemAction:

    def __init__(self, host_actor):
        self._actor = host_actor
        self._param = { "IsTriggerGetItem" : False }

        if self._actor.get_game_logic_component("ItemHolder") == None:
            self._actor.insert_game_logic_component("ItemHolder", ItemHolder.ItemHolder())
        # ItemHolder
    # def __init__

    def is_end(self):
        return self._param["IsTriggerGetItem"] == False
    # def is_end

    def get_execute_parts(self):
        return ["Upper"]
    # def get_execute_parts

    def set_action_param(self, param):
        self._param = param
    # set_action_param

    def update(self):
        if self._param["IsTriggerGetItem"] == True:
            item_holder = self._actor.get_game_logic_component("ItemHolder")
            item_holder.set_is_item_get_action()

        self._param["IsTriggerGetItem"] = False
    #

    def post_update(self):
        pass

# class GetItemAction
