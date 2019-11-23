# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file PlayerObject.py
# @note

import Object
import IDraw

from Logic.GameLogicComponents.ObjectControl.PlayerControl import PlayerControl

class PlayerObject(Object.Object):

    def __init__(self):
        super(PlayerObject, self).__init__("Player")
    # def __init__

    def set_controller(self, controller):
        actor_control_component = PlayerControl()
        actor_control_component.set_control_actor(self, controller)
        self.game_logic_components["ObjectControl"] = actor_control_component
    # def set_controller

    def update(self):        
        super().update()
    # def update

# class PlayerObject

if __name__ == "__main__":
    pass
