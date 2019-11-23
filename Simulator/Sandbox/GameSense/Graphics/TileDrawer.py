# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IDraw.py
# @note

from .DrawerUtil import DrawerUtil

class TileDrawer:

    def __init__(self):
        self.tile_info = [[0, 0], [0, 0]]
        self.tile_size = (32, 32)

        self.image = None
    # def __init__

    def init_from_setting(self, draw_setting):
        self.image = DrawerUtil.create_image(draw_setting["Image"])
        self.priority = DrawerUtil.get_priority_from_setting(draw_setting)

    def set_tile_info(self, tile_info):
        self.tile_info = tile_info
    # def set_tile_info

    def draw(self, pos, screen):
        if self.tile_info == None:
            return None

        len_x = len(self.tile_info)
        len_z = len(self.tile_info[0])
        for x in range(len_x):
            for z in range(len_z):
                screen.blit(self.image, (pos[0] + self.tile_size[0]*x, pos[2] + self.tile_size[1]*z))
            #
        #
    # def draw

# class TileDrawer
