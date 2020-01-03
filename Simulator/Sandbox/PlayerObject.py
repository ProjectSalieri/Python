# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file PlayerObject.py
# @note

import Object

from Logic.GameLogicComponents.ObjectControl.PlayerControl import PlayerControl

class PlayerObject(Object.Object):

    def __init__(self, load_option = {}):
        super(PlayerObject, self).__init__("Player", load_option)
    # def __init__

    def get_name(self):
        return "Player"
    # def get_name

    def set_controller(self, controller):
        actor_control_component = PlayerControl()
        actor_control_component.set_control_actor(self, controller)
        self.insert_game_logic_component("ObjectControl", actor_control_component)
    # def set_controller

    def update(self):        
        super().update()
    # def update

# class PlayerObject

if __name__ == "__main__":
    pass
