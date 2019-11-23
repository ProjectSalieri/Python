# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SimpleDrawer.py
# @note

import pygame

from .DrawerUtil import DrawerUtil

class SimpleDrawer:

    def __init__(self):
        self.image = None
        self.half_size = (0, 0)
        self.priority = 0
    # def __init__

    def init_from_setting(self, draw_setting):
        image_name = draw_setting["Image"]
        self.image = DrawerUtil.create_image(image_name)
        self.half_size = DrawerUtil.calc_half_size(self.image)

        self.priority = DrawerUtil.get_priority_from_setting(draw_setting)
    # def init_from_setting

    def draw(self, pos, screen):
        screen.blit(self.image, (pos[0], pos[2]))
    # def draw
# class IDraw
