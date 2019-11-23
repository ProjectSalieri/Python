# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IDraw.py
# @note

import pygame

class IDraw:

    def __init__(self):
        self.image = None
        self.half_size = (0, 0)
        self.priority = 0
    # def __init__

    def init_from_setting(self, draw_setting):
        image_name = draw_setting["Image"]
        import os
        image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "ImageData")
        self.image = pygame.image.load(os.path.join(image_dir, image_name)).convert_alpha()
        self.half_size = (self.image.get_width()/2, self.image.get_height()/2)

        self.priority = draw_setting["Priority"] if draw_setting.get("Priority") else 0
    # def init_from_setting

    def update(self):
        pass
    # def update

    def post_update(self):
        pass
    # def update

    def draw(self, pos, screen):
        screen.blit(self.image, (pos[0], pos[2]))
    # def draw
# class IDraw
