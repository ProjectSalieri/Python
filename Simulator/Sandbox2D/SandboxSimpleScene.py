# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SandboxSimpleScene.py
# @note

import pygame
from pygame.locals import *

import Object2D
import PlayerObject
from Logic.Physics import PhysicsDirector

class SandboxSimpleScene:

    def __init__(self):
        self.objects = []

        # データ読み込み
        self._init_scene_from_data()

        self.physics_director = PhysicsDirector.PhysicsDirector()
    # def __init__

    def _init_scene_from_data(self):
        simple_object = PlayerObject.PlayerObject()
        simple_object.pos = (128, 32)
        self.objects.append(simple_object)

        simple_object2 = Object2D.Object2D("Sample")
        simple_object2.pos = (32, 32)
        self.objects.append(simple_object2)

        simple_object3 = Object2D.Object2D("Apple")
        simple_object3.pos = (80, 80)
        self.objects.append(simple_object3)

        simple_object4 = Object2D.Object2D("Sample")
        simple_object4.pos = (128, 128)
        self.objects.append(simple_object4)
    # def _init_scene_from_data

    def update(self):
        for object in self.objects:
            object.update()

        self.physics_director.update(self.objects)
    # def update

    def draw(self, screen):
        for object in self.objects:
            object.draw(screen)
    # def draw

# class SandboxSimpleScene

if __name__ == "__main__":
    pass
