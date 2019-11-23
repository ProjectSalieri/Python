# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file PlayerControl.py
# @note

from ...Input import PlayerController

# TODO キー操作は抽象化
import pygame
from pygame.locals import *

class PlayerControl:

    def __init__(self):
        self._control_actor = None
        self._controller = None
    # def __init__

    def set_control_actor(self, actor, player_controller):
        self._control_actor = actor
        self._controller = player_controller
    # def set_control_actor

    def update(self):        
        player_vel = [0.0, 0.0, 0.0]
        for input in self._controller.inputs:
            if input == PlayerController.PlayerController.KEY_LEFT:
                player_vel[0] = -1.0
            elif input == PlayerController.PlayerController.KEY_RIGHT:
                player_vel[0] = 1.0

            elif input == PlayerController.PlayerController.KEY_UP:
                player_vel[1] = -1.0
            elif input == PlayerController.PlayerController.KEY_DOWN:
                player_vel[1] = 1.0

        physics = self._control_actor.get_object_component("Physics")
        physics.add_velocity(player_vel)
    # def update

    def post_update(self):
        pass
    # def post_update
    
# class PlayerControl
