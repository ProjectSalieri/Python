# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file Simulator2D.py
# @note

import pygame
import Object2D

class SimpleObject(Object2D.Object2D):

    def __init__(self):
        import os
        image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ImageData")
        self.image = pygame.image.load(os.path.join(image_dir, "Sample.png")).convert_alpha()
        self.half_size = (self.image.get_width()/2, self.image.get_height()/2)
    # def __init__

    def update(self):
        pass
    # def update

    def draw(self, screen):
        screen.blit(self.image, self.pos)
    # def draw
    
# class SimpleObject

if __name__ == "__main__":
    pass
