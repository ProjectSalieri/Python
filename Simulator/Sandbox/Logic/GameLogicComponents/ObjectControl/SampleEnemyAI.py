# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SampleMove.py
# @note

from ..CharacterAction import ActionExecutor
from ..CharacterAction import GetItemAction
from ..CharacterAction import SimpleMove

import numpy as np

# Parameter定義
# MoveSpeed : 

class SampleEnemyAI:

    SAMPLE_ENEMY_STATE_WANDER = 0
    SAMPLE_ENEMY_STATE_MOVE_TO_ITEM = 1
    SAMPLE_ENEMY_STATE_GET_ITEM = 2

    def __init__(self, host_actor, parameter):
        self._actor = host_actor

        self._param = parameter

        self._item_get_counter = 0

        self.actions = {"Move" : SimpleMove.SimpleMove(host_actor),
                        "GetItem" : GetItemAction.GetItemAction(host_actor)
        }
        self.actions["Move"].set_action_param({"Speed" : 1.0, "Dir" : (1.0, 0.0, 0.0) })
        self._action_executor = ActionExecutor.ActionExecutor()
    # def __init__

    def update(self):
        # 近くにアイテムがあるかチェック
        eye_sense_objects = []
        if self._actor != None:
            eye_sense_objects = self._actor.get_object_component("Sense").try_get_eye_sensor().sense_objects
        item_objects = []
        for obj in eye_sense_objects:
            if obj.get_game_logic_component("Item") != None:
                item_objects.append(obj)

        # TODO : アイテムの価値や距離を考慮
        target_object = None
        target_dir = [0.0, 0.0, 0.0]
        if len(item_objects) > 0:
            target_object = item_objects[0]
            diff = target_object.get_pos() - self._actor.get_pos()
            if np.linalg.norm(diff) > 50.0:
                self._item_get_counter = 0
                
                if diff[0] > 0.0:
                    target_dir[0] = 1.0
                elif diff[0] < 0.0:
                    target_dir[0] = -1.0

                if diff[2] < 0.0:
                    target_dir[2] = -1.0
                elif diff[2] > 0.0:
                    target_dir[2] = 1.0
            else:
                self._item_get_counter += 1
            # if np.linalg.norm
        else:
            self._item_get_counter = 0
        # if len(item_objects)

        if target_dir[0] != 0.0 or target_dir[2] != 0.0:
            self.actions["Move"].set_action_param({"Speed" : self._param["MoveSpeed"], "Dir" : (target_dir[0], target_dir[1], target_dir[2]) })
            self._action_executor.try_start_action(self.actions["Move"])
        else:
            # Stop
            self.actions["Move"].set_action_param({"Speed" : 0.0, "Dir" : (0.0, 0.0, 0.0) })

            if self._item_get_counter < 120:
                pass
            else:
                self._item_get_counter = 0
                self.actions["GetItem"].set_action_param({"IsTriggerGetItem" : True})
                self._action_executor.try_start_action(self.actions["GetItem"])
                
        # if dir

        self._action_executor.update()

    # def update

    def post_update(self):
        pass
    # def post_update

# class SampleEnemyAI
