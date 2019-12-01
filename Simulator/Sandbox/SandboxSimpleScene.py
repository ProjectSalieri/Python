# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SandboxSimpleScene.py
# @note

import pygame
from pygame.locals import *

from SandboxSimpleSceneBase import SandboxSimpleSceneBase

import Object
import PlayerObject

from Logic.Input import PlayerController

# Serverロジック
from Logic.GameLogicComponents.ObjectControl.ServerControl import ServerControl

# test
from Salieri import Salieri

#
from GameSense.GraphicsSystem.GameCamera import GameCamera

class SandboxSimpleScene(SandboxSimpleSceneBase):

    def __init__(self):

        self.player_controller = PlayerController.PlayerController()

        # データ読み込み
        self.player_objects = []

        # test
        self.test_client = Salieri.Salieri()

        super().__init__()

        # GraphicsSystem
        self.game_camera = GameCamera()
        self.game_camera.set_player_objects(self.player_objects)
        
    # def __init__

    def _init_scene_from_data(self):
        simple_object = PlayerObject.PlayerObject()
        simple_object.pos = (128, 0, 32)
        simple_object.set_controller(self.player_controller)
        self.objects.append(simple_object)
        self.player_objects.append(simple_object)

        simple_object2 = Object.Object("Sample")
        simple_object2.reset_pos((32, 0, 32))
        server_control2 = ServerControl(simple_object2)
        server_control2.set_test_client(self.test_client)
        simple_object2.insert_game_logic_component("ObjectControl", server_control2)
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

    def kill(self):
        self.test_client.shutdown()
    # def kill

    def update(self):
        self._update_player_controller()

        #self.sensor_director.update(self.objects)

        for player in self.player_objects:
            center_pos = player.get_object_component("Physics").pos
            self._update_common(center_pos)
    # def update

    def pre_draw(self, screen):
        self._pre_draw(screen)

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
                drawer = object.drawer
                obj_pos = object.get_object_component("Physics").pos
                draw_pos = (obj_pos[0]-self.game_camera.look_at_pos[0], obj_pos[1]-self.game_camera.look_at_pos[1], obj_pos[2]-self.game_camera.look_at_pos[2])
                drawer.draw(draw_pos, screen)
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

    def _pre_draw(self, screen):
        self.game_camera.pre_draw(screen)
    # def _pre_draw
# class SandboxSimpleScene

if __name__ == "__main__":
    pass
