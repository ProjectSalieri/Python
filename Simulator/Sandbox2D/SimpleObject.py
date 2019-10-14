# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file Simulator2D.py
# @note

import Object2D
import IDraw

class SimpleObject(Object2D.Object2D):

    def __init__(self):
        self.drawer = IDraw.IDraw("Sample.png")
    # def __init__

    def update(self):
        pass
    # def update

    def draw(self, screen):
        self.drawer.draw(self.pos, screen)
    # def draw
    
# class SimpleObject

if __name__ == "__main__":
    pass
