# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IDraw.py
# @note

import pygame

from . import SimpleDrawer
from . import TileDrawer

class IDraw:

    def __init__(self):
        self.custom_drawer = None
    # def __init__

    def init_from_setting(self, draw_setting):
        drawer_name = draw_setting.get("Drawer")
        if drawer_name == None:
            self.custom_drawer = SimpleDrawer.SimpleDrawer()
        elif drawer_name == "TileDrawer":
            self.custom_drawer = TileDrawer.TileDrawer()
        self.custom_drawer.init_from_setting(draw_setting)
    # def init_from_setting

    def get_priority(self):
        return self.custom_drawer.priority

    def update(self):
        pass
    # def update

    def post_update(self):
        pass
    # def update

    def draw(self, pos, screen):
        self.custom_drawer.draw(pos, screen)
    # def draw
# class IDraw
