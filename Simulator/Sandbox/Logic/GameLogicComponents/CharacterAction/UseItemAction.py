# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file UseItemAction
# @note

#from Logic.GameLogicComponents.Item import ItemHolder
from ..Item import ItemHolder

class UseItemAction:

    def __init__(self, host_actor):
        self._actor = host_actor
        self._param = { "ItemName" : None, "Target" : None }

        if self._actor.get_game_logic_component("ItemHolder") == None:
            self._actor.insert_game_logic_component("ItemHolder", ItemHolder.ItemHolder())
        # ItemHolder
    # def __init__

    def set_action_param(self, param):
        self._param = param
    # set_action_param

    def update(self):
        if self._param["ItemName"] != None:
            item_holder = self._actor.get_game_logic_component("ItemHolder")
            item_holder.use_item(self._param["ItemName"], self._param["Target"])

        self._param["ItemName"] = None
        self._param["Target"] = None
    #

    def post_update(self):
        pass

# class UseItemAction
