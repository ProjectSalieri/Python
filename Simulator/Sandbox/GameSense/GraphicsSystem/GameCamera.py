# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file GameCamera.py
# @note

import numpy as np

class GameCamera:

    def __init__(self):
        self._look_at_pos_screen = np.array([0.0, 0.0, 0.0])
        self._look_at_pos = np.array([0.0, 0.0, 0.0])
        self.player_objects = []
        self.screen = None
    # def __init__

    def set_player_objects(self, player_objects):
        self.player_objects = player_objects
    # def set_player_objects

    def set_screen(self, screen):
        self.screen = screen
    #

    def update(self):
        pass
    # def update

    def pre_draw(self, screen):
        camera_idx = 0
        player = self.player_objects[camera_idx]

        player_pos = player.get_pos()
        self._look_at_pos = 0.15*player_pos + 0.85*self._look_at_pos # 補完追従
        self._look_at_pos_screen = (self._look_at_pos[0] - screen.get_width()/2, 0, self._look_at_pos[2] - screen.get_height()/2)
    # def pre_draw
# class GameCamera
