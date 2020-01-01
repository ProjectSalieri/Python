# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file VirtualController.py
# @note エンジンのキー操作をラップ

import pygame
from pygame.locals import *

class VirtualController:

    KEY_UP = 1
    KEY_RIGHT = 2
    KEY_DOWN = 3
    KEY_LEFT = 4
    KEY_A = 5 # BCDEFGHIJKLM
    KEY_M = 17
    KEY_U = 25

    def __init__(self):
        self._current_pressed_key = pygame.key.get_pressed()

        self._key_table = {
            VirtualController.KEY_UP : K_UP,
            VirtualController.KEY_RIGHT : K_RIGHT,
            VirtualController.KEY_DOWN : K_DOWN,
            VirtualController.KEY_LEFT : K_LEFT,
            VirtualController.KEY_A : K_a,
            VirtualController.KEY_M : K_m,
            VirtualController.KEY_U : K_u
        }
    # def __init__

    def is_pressed(self, key_type):
        key_type2 = self._key_table[key_type]
        return self._current_pressed_key[key_type2]
    # is_pressed

    def is_trigger_pressed(self, key_type):
        key_type2 = self._key_table[key_type]
        return self._current_pressed_key[key_type2] and self._prev_pressed_key[key_type2] == False
    # def is_trigger_pressed

    def update(self):
        self._prev_pressed_key = self._current_pressed_key
        self._current_pressed_key = pygame.key.get_pressed()
    # def update

    
# class VirtualController

if __name__ == "__main__":
    pass
