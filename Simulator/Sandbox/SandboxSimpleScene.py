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
from Logic.System import ItemDirector
from Logic.GameLogicComponents.Item import ItemHolder
from Logic.System.MetaAI import MetaAI

# Serverロジック
from Logic.GameLogicComponents.ObjectControl.ServerControl import ServerControl

# test
from Salieri import Salieri

#
from GameSense.GraphicsSystem.GameCamera import GameCamera
from SandboxSceneDrawer import SandboxSceneDrawer

class SandboxSimpleScene(SandboxSimpleSceneBase):

    def __init__(self):

        self.player_controller = PlayerController.PlayerController()

        # データ読み込み
        self.player_objects = []

        # test
        self.test_client = Salieri.Salieri()

        self.item_director = ItemDirector.ItemDirector()

        super().__init__()

        # GraphicsSystem
        self.game_camera = GameCamera()
        self.game_camera.set_player_objects(self.player_objects)

        self.meta_ai = MetaAI()
        
    # def __init__

    def _init_scene_from_data(self):
        simple_object = PlayerObject.PlayerObject()
        simple_object.pos = (128, 0, 32)
        simple_object.set_controller(self.player_controller)
        simple_object.insert_game_logic_component("ItemHolder", ItemHolder.ItemHolder())
        self.objects.append(simple_object)
        self.player_objects.append(simple_object)

        simple_object2 = Object.Object("Sample")
        simple_object2.reset_pos((32, 0, 32))
        server_control2 = ServerControl(simple_object2)
        server_control2.set_test_client(self.test_client)
        simple_object2.insert_game_logic_component("ObjectControl", server_control2)
        self.test_client.set_control_actor(simple_object2)
        self.objects.append(simple_object2)

        simple_object3 = Object.Object("Apple")
        simple_object3.reset_pos((80, 0, 80))
        self.objects.append(simple_object3)

        simple_object4 = Object.Object("Sample")
        simple_object4.reset_pos((128, 0, 128))
        self.objects.append(simple_object4)

        simple_object5 = Object.Object("SampleEnemy")
        simple_object5.reset_pos((200, 0, 200))
        self.objects.append(simple_object5)

        
        ground1 = Object.Object("IceGround")
        ground1.reset_pos((256, 0, 256))
        self.objects.append(ground1)

        self.item_director.add_item_holdable_object(simple_object)
        self.item_director.add_item_holdable_object(simple_object2)
    # def _init_scene_from_data

    def kill(self):
        self.test_client.shutdown()
    # def kill

    def update(self):        
        self._update_player_controller()

        for player in self.player_objects:
            center_pos = player.get_object_component("Physics").pos

            self.objects = self.meta_ai.update(self.objects, center_pos)
            
            self._update_common(center_pos)

            self.item_director.update(self.objects, center_pos)
    # def update

    def pre_draw(self, screen):
        self._pre_draw(screen)

    def draw(self, screen):
        drawer = SandboxSceneDrawer()
        drawer.draw(screen, self.objects, self.game_camera.look_at_pos)

        self._draw_layout(screen)
    # def draw

    def _update_player_controller(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_m]:
            print("Menu Open")
            for player in self.player_objects:
                item_holder = player.get_game_logic_component("ItemHolder")
                for item_name, item_num in item_holder._items.items():
                    print(item_name + ":" + str(item_num))
            return False
        
        
        # キー解決
        self.player_controller.clear()
        if pressed_key[K_LEFT]:
            self.player_controller.input(PlayerController.PlayerController.KEY_LEFT)
        elif pressed_key[K_RIGHT]:
            self.player_controller.input(PlayerController.PlayerController.KEY_RIGHT)
        elif pressed_key[K_UP]:
            self.player_controller.input(PlayerController.PlayerController.KEY_UP)
        elif pressed_key[K_DOWN]:
            self.player_controller.input(PlayerController.PlayerController.KEY_DOWN)
        elif pressed_key[K_a]:
            self.player_controller.input(PlayerController.PlayerController.KEY_A)
        elif pressed_key[K_u]:
            self.player_controller.input(PlayerController.PlayerController.KEY_U)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
    # def _update_player_controller

    def _pre_draw(self, screen):
        self.game_camera.pre_draw(screen)
    # def _pre_draw

    def _draw_layout(self, screen):
        font = pygame.font.Font(None, 40)

        # プレイヤー情報
        player = self.player_objects[0]
        player_hp = player.get_object_component("Life").get_dulability()
        player_hp = (int)(player_hp/100)*100 # 100以下の変化は見せない
        is_pinch = player_hp < 2000
        screen.blit(font.render("P : %d" % (player_hp), True, (255, 0, 0) if is_pinch else (0, 255, 0)) , [10, 10])

        # salieri
        salieri_actor = self.test_client._actor
        salieri_hp = salieri_actor.get_object_component("Life").get_dulability()
        salieri_hp = (int)(salieri_hp/100)*100 # 100以下の変化は見せない        
        screen.blit(font.render("S : %d" % (salieri_hp), True, (255, 0, 0) if is_pinch else (0, 255, 0)) , [10, 35])
# class SandboxSimpleScene

if __name__ == "__main__":
    pass
