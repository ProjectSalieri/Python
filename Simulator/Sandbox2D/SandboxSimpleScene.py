# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SandboxSimpleScene.py
# @note

import pygame

import Object2D
import SimpleObject

class SandboxSimpleScene:

    def __init__(self):
        self.objects = []

        # データ読み込み
        self._init_scene_from_data()
    # def __init__

    def _init_scene_from_data(self):
        simple_object = SimpleObject.SimpleObject()
        simple_object.pos = (32, 32)
        self.objects.append(simple_object)

        simple_object2 = SimpleObject.SimpleObject()
        simple_object2.pos = (0, 0)
        self.objects.append(simple_object2)
    # def _init_scene_from_data

    def update(self):
        pass
    # def update

    def draw(self, screen):
        for object in self.objects:
            object.draw(screen)
    # def draw

# class SandboxSimpleScene

if __name__ == "__main__":
    pass
