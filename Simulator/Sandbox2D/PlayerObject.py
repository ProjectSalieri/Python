# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file PlayerObject.py
# @note

import Object2D
import IDraw

from Logic.GameLogicComponents.ActorControl.PlayerControl import PlayerControl

class PlayerObject(Object2D.Object2D):

    def __init__(self):
        super(PlayerObject, self).__init__("Player")
    # def __init__

    def set_controller(self, controller):
        actor_control_component = PlayerControl()
        actor_control_component.set_control_actor(self, controller)
        self.game_logic_components["ActorControl"] = actor_control_component
    # def set_controller

    def update(self):        
        super().update()
    # def update

# class PlayerObject

if __name__ == "__main__":
    pass
