# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file GameCamera.py
# @note

class GameCamera:

    def __init__(self):
        self.look_at_pos = (0.0, 0.0, 0.0)
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

        player_pos = player.get_object_component("Physics").pos
        self.look_at_pos = (player_pos[0] - screen.get_width()/2, 0, player_pos[2] - screen.get_height()/2)
    # def pre_draw
# class GameCamera
