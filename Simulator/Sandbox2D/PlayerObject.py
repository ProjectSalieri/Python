# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file PlayerObject.py
# @note

import Object2D
import IDraw

# TODO キー操作は抽象化
import pygame
from pygame.locals import *

class PlayerObject(Object2D.Object2D):

    def __init__(self):
        super(PlayerObject, self).__init__("Sample")
    # def __init__

    def update(self):        
        player_vel = (0.0, 0.0)
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            player_vel = (-8.0, 0.0)
        elif pressed_key[K_RIGHT]:
            player_vel = (8.0, 0.0)
        elif pressed_key[K_UP]:
            player_vel = (0.0, -8.0)
        elif pressed_key[K_DOWN]:
            player_vel = (0.0, 8.0)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass

        self.add_velocity(player_vel)

        super().update()
    # def update

# class PlayerObject

if __name__ == "__main__":
    pass
