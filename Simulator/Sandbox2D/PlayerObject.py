# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file PlayerObject.py
# @note

import Object2D
import IDraw

from Logic.Input import PlayerController

# TODO キー操作は抽象化
import pygame
from pygame.locals import *

class PlayerObject(Object2D.Object2D):

    def __init__(self):
        super(PlayerObject, self).__init__("Sample")

        self.controller = None
    # def __init__

    def set_controller(self, controller):
        self.controller = controller
    # def set_controller

    def update(self):        
        player_vel = [0.0, 0.0]
        for input in self.controller.inputs:
            if input == PlayerController.PlayerController.KEY_LEFT:
                player_vel[0] = -8.0
            elif input == PlayerController.PlayerController.KEY_RIGHT:
                player_vel[0] = 8.0
            elif input == PlayerController.PlayerController.KEY_UP:
                player_vel[1] = -8.0
            elif input == PlayerController.PlayerController.KEY_DOWN:
                player_vel[1] = 8.0

        self.add_velocity(player_vel)

        super().update()
    # def update

# class PlayerObject

if __name__ == "__main__":
    pass
