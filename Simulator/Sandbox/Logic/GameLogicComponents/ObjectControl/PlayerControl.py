# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file PlayerControl.py
# @note

from ...Input import PlayerController
from ..CharacterAction.GetItemAction import GetItemAction
from ..CharacterAction.SimpleMove import SimpleMove

from Logic.System.MetaAI.MetaAI import MetaAI

class PlayerControl:

    def __init__(self):
        self._control_actor = None
        self._controller = None
        self._actions = {}
    # def __init__

    def set_control_actor(self, actor, player_controller):
        self._controller = player_controller
        self._set_control_actor(actor)

        MetaAI.regist_player_object(self._control_actor)
    # def set_control_actor

    def update(self):        
        self._update_core(self._controller.inputs)
        
    # def update

    def post_update(self):
        pass
    # def post_update

    def _set_control_actor(self, actor):
        self._control_actor = actor

        self._actions["Move"] = SimpleMove(actor)
        self._actions["GetItem"] = GetItemAction(actor)
    # def _set_control_actor

    def _update_core(self, inputs):
        player_dir = [0.0, 0.0, 0.0]
        speed = 0.0
        action_name = None
        param = {"Move" : {}, "GetItem" : {}}
        for input in inputs:
            if input == PlayerController.PlayerController.KEY_LEFT:
                player_dir[0] = -1.0
                speed = 1.0
                action_name = "Move"
            elif input == PlayerController.PlayerController.KEY_RIGHT:
                player_dir[0] = 1.0
                speed = 1.0
                action_name = "Move"
            elif input == PlayerController.PlayerController.KEY_UP:
                player_dir[2] = -1.0
                speed = 1.0
                action_name = "Move"
            elif input == PlayerController.PlayerController.KEY_DOWN:
                player_dir[2] = 1.0
                speed = 1.0
                action_name = "Move"
            elif input == PlayerController.PlayerController.KEY_A:
                action_name = "GetItem"
                param["GetItem"] = {"IsTriggerGetItem" : True}

        if action_name == "Move":
            tmp_param = { "Speed" : speed, "Dir" : player_dir }
            self._actions[action_name].set_action_param(tmp_param)
            self._actions[action_name].update()
        elif action_name == "GetItem":
            self._actions[action_name].set_action_param(param["GetItem"])
            self._actions[action_name].update()
    
# class PlayerControl
