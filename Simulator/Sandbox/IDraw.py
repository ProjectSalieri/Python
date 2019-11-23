# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IDraw.py
# @note

import pygame

class IDraw:

    def __init__(self, image_name):
        import os
        image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ImageData")
        self.image = pygame.image.load(os.path.join(image_dir, image_name)).convert_alpha()
        self.half_size = (self.image.get_width()/2, self.image.get_height()/2)
    # def __init__

    def update(self):
        pass
    # def update

    def post_update(self):
        pass
    # def update

    def draw(self, pos, screen):
        screen.blit(self.image, (pos[0], pos[1]))
    # def draw
# class IDraw
