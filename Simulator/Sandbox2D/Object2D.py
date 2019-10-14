# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file Simulator2D.py
# @note

import pygame

class Object2D:

    def __init__(self):
        self.pos = (0.0, 0.0)
        self.half_size = (0, 0)
        pass
    # def __init__

    def update(self):
        pass
    # def update

    def draw(self, screen):
        pygame.draw.rect(screen, (255,128,0), pygame.Rect(self.x() - self.half_w(),self.y() - self.half_h(),self.x() + self.half_w(),self.y() + self.half_h()))
        pass
    # def draw

    def x(self):
        return self.pos[0]
    def y(self):
        return self.pos[1]
    def half_w(self):
        return self.half_size[0]
    def half_h(self):
        return self.half_size[1]
    
# class Object2D

if __name__ == "__main__":
    pass
