# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file GameCamera.py
# @note

class GameCamera:

    def __init__(self):
        self.look_at_pos = (0.0, 0.0, 0.0)
        self.player_objects = []
    # def __init__

    def set_player_objects(self, player_objects):
        self.player_objects = player_objects
    # def set_player_objects

    def update(self):
        camera_idx = 0
        player = self.player_objects[camera_idx]

        self.look_at_pos = player.get_object_component("Physics").pos
    # def update
# class GameCamera
