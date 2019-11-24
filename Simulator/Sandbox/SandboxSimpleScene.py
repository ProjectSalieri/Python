# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SandboxSimpleScene.py
# @note

import pygame
from pygame.locals import *

import Object
import PlayerObject

from Logic.Input import PlayerController
from Logic.Sensor import SensorDirector
from Logic.Physics import PhysicsDirector
from Logic.System.ObjectUpdateDirector import ObjectUpdateDirector

class SandboxSimpleScene:

    def __init__(self):
        self.objects = []

        self.player_controller = PlayerController.PlayerController()

        # データ読み込み
        self._init_scene_from_data()

        #self.sensor_director = SensorDirector.SensorDirector()
        self.object_udpate_director = ObjectUpdateDirector()
        self.physics_director = PhysicsDirector.PhysicsDirector()
    # def __init__

    def _init_scene_from_data(self):
        simple_object = PlayerObject.PlayerObject()
        simple_object.pos = (128, 0, 32)
        simple_object.set_controller(self.player_controller)
        self.objects.append(simple_object)

        simple_object2 = Object.Object("Sample")
        simple_object2.reset_pos((32, 0, 32))
        self.objects.append(simple_object2)

        simple_object3 = Object.Object("Apple")
        simple_object3.reset_pos((80, 0, 80))
        self.objects.append(simple_object3)

        simple_object4 = Object.Object("Sample")
        simple_object4.reset_pos((128, 0, 128))
        self.objects.append(simple_object4)

        
        ground1 = Object.Object("IceGround")
        ground1.reset_pos((256, 0, 256))
        self.objects.append(ground1)
    # def _init_scene_from_data

    def update(self):
        self._update_player_controller()

        #self.sensor_director.update(self.objects)

        center_pos = (0.0, 0.0, 0.0)
        
        self.object_udpate_director.update(self.objects, center_pos)

        self.physics_director.update(self.objects, center_pos)
    # def update

    def draw(self, screen):
        # TODO : ObjectRegionDirectorBase
        priorities = []
        draw_list = {}

        for object in self.objects:
            priority = object.drawer.get_priority()
            if draw_list.get(priority) == None:
                draw_list[priority] = []
                priorities.append(priority)
            draw_list[priority].append(object)

        priorities.sort()

        for priority in priorities:
            draw_object = draw_list[priority]
            for object in draw_object:
                object.draw(screen)
            # for draw_object
        # for priorities
    # def draw

    def _update_player_controller(self):
        # キー解決
        self.player_controller.clear()
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            self.player_controller.input(PlayerController.PlayerController.KEY_LEFT)
        elif pressed_key[K_RIGHT]:
            self.player_controller.input(PlayerController.PlayerController.KEY_RIGHT)
        elif pressed_key[K_UP]:
            self.player_controller.input(PlayerController.PlayerController.KEY_UP)
        elif pressed_key[K_DOWN]:
            self.player_controller.input(PlayerController.PlayerController.KEY_DOWN)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
    # def _update_player_controller

# class SandboxSimpleScene

if __name__ == "__main__":
    pass
