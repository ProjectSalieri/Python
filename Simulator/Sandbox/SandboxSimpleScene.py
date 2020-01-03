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
from Logic.System.MetaAI.MetaAI import MetaAI
from Logic.System.Logger.PlayLogger import PlayLogger

# Serverロジック
from Logic.GameLogicComponents.ObjectControl.ServerControl import ServerControl

# test
from Salieri import Salieri

#
from GameSense.GraphicsSystem.GameCamera import GameCamera
from SandboxSceneDrawer import SandboxSceneDrawer
from Logic.Input.VirtualController import VirtualController

class SandboxSimpleScene(SandboxSimpleSceneBase):

    EXE_PLAY = 0
    EXE_MENU = 1

    def __init__(self):

        self.meta_ai = MetaAI()
        self._controller = VirtualController()
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

        self._state = SandboxSimpleScene.EXE_PLAY

        # Menu
        self._menu_select = 0
        
    # def __init__

    def _init_scene_from_data(self):
        import os
        save_json_path = self._save_json_path()
        if os.path.exists(save_json_path) == False:
            if os.path.exists(self._default_save_json_path()):
                save_json_path = self._default_save_json_path()
            else:
                save_json_path = None
        if save_json_path != None:
            import json
            print("[Scene]load save : %s" % (save_json_path))
            
            save_settings = None
            with open(save_json_path) as f:
                save_settings = json.load(f)

            for player_save_setting in save_settings["PlayerPlacement"]:
                player_obj = PlayerObject.PlayerObject(player_save_setting)
                self.objects.append(player_obj)
                self.player_objects.append(player_obj)
                player_obj.set_controller(self.player_controller)
            # for PlayerPlacement

            for obj_save_setting in save_settings["ObjectsPlacement"]:
                obj = Object.Object(obj_save_setting.get("Name"), obj_save_setting)
                self.objects.append(obj)
            # for ObjectsPlacement
            return True
        # if save
        
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
        self.test_client.set_control_actor(simple_object2)
        self.objects.append(simple_object2)

        simple_object3 = Object.Object("Apple")
        simple_object3.reset_pos((80, 0, 80))
        self.objects.append(simple_object3)

        simple_object4 = Object.Object("AppleTree")
        simple_object4.reset_pos((128, 0, 128))
        self.objects.append(simple_object4)

        simple_object5 = Object.Object("SampleEnemy")
        simple_object5.reset_pos((200, 0, 200))
        self.objects.append(simple_object5)

        
        ground1 = Object.Object("IceGround")
        ground1.reset_pos((256, 0, 256))
        self.objects.append(ground1)
    # def _init_scene_from_data

    def kill(self):
        self._save()
        
        self.test_client.shutdown()
        self.meta_ai.shutdown()
    # def kill

    def update(self):        
        self._update_player_controller()

        if self._state == SandboxSimpleScene.EXE_PLAY:
            self._exe_play()
        elif self._state == SandboxSimpleScene.EXE_MENU:
            self._exe_menu()

    # def update

    def pre_draw(self, screen):
        self._pre_draw(screen)

    def draw(self, screen):
        drawer = SandboxSceneDrawer()
        drawer.draw(screen, self.objects, self.game_camera._look_at_pos_screen)

        self._draw_layout(screen)
    # def draw

    def _exe_play(self):
        for player in self.player_objects:
            center_pos = player.get_object_component("Physics").pos

            self.objects = self.meta_ai.update(self.objects, center_pos)
            
            self._update_common(center_pos)

            self.item_director.update(self.objects, center_pos)
    # def _exe_play

    def _exe_menu(self):
        item_num_max = 0
        for player in self.player_objects:
            item_holder = player.get_game_logic_component("ItemHolder")
            for item_name, item_num in item_holder._items.items():
                item_num_max += 1

        if self._controller.is_trigger_pressed(VirtualController.KEY_UP):
            self._menu_select -= 1
        elif self._controller.is_trigger_pressed(VirtualController.KEY_DOWN):
            self._menu_select += 1

        if self._menu_select < 0:
            self._menu_select = 0
        elif self._menu_select > item_num_max-1:
            self._menu_select = item_num_max-1

        if self._controller.is_trigger_pressed(VirtualController.KEY_U):
            self.player_controller.input(PlayerController.PlayerController.KEY_U)
            # TODO : アイテム使用専用メニュー 対象選択など
            for player in self.player_objects:
                item_holder = player.get_game_logic_component("ItemHolder")
                cnt = 0
                use_item_name = None
                for item_name, item_num in item_holder._items.items():
                    if self._menu_select == cnt:
                        use_item_name = item_name
                    cnt += 1
                if use_item_name != None:
                    item_holder.use_item(use_item_name, player)
                    PlayLogger.put_as_use_item(use_item_name, player)
    # def _exe_menu

    def _update_player_controller(self):
        self._controller.update()

        if self._controller.is_trigger_pressed(VirtualController.KEY_M):
            if self._state != SandboxSimpleScene.EXE_MENU:
                self._state = SandboxSimpleScene.EXE_MENU
                self._menu_select = 0
                print("Menu Open")
            else:
                self._state = SandboxSimpleScene.EXE_PLAY
                print("Menu Close")
            return False
        # Mキー
        
        # キー解決
        self.player_controller.clear()
        if self._controller.is_pressed(VirtualController.KEY_LEFT):
            self.player_controller.input(PlayerController.PlayerController.KEY_LEFT)
        elif self._controller.is_pressed(VirtualController.KEY_RIGHT):
            self.player_controller.input(PlayerController.PlayerController.KEY_RIGHT)
        elif self._controller.is_pressed(VirtualController.KEY_UP):
            self.player_controller.input(PlayerController.PlayerController.KEY_UP)
        elif self._controller.is_pressed(VirtualController.KEY_DOWN):
            self.player_controller.input(PlayerController.PlayerController.KEY_DOWN)
        elif self._controller.is_trigger_pressed(VirtualController.KEY_A):
            self.player_controller.input(PlayerController.PlayerController.KEY_A)
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
        if salieri_actor != None:
            salieri_hp = salieri_actor.get_object_component("Life").get_dulability()
            salieri_hp = (int)(salieri_hp/100)*100 # 100以下の変化は見せない        
            screen.blit(font.render("S : %d" % (salieri_hp), True, (255, 0, 0) if is_pinch else (0, 255, 0)) , [10, 35])
        # if salieri_actor

        # アイテムメニュー
        if self._state == SandboxSimpleScene.EXE_MENU:
            font2 = pygame.font.Font(None, 25)
            pygame.draw.rect(screen, (255,255,255), Rect(100,100,500,500))
            screen.blit(font2.render("Item Menu", True, (0, 0, 0)) , [100, 100])
            line_cnt = 0
            for player in self.player_objects:
                item_holder = player.get_game_logic_component("ItemHolder")
                for item_name, item_num in item_holder._items.items():
                    is_select = False
                    if line_cnt == self._menu_select:
                        is_select = True
                    line_cnt += 1
                    if is_select:
                        screen.blit(font2.render("->%s : %d" % (item_name, item_num), True, (0, 0, 0)) , [100, 100 + line_cnt*20])
                    else:
                        screen.blit(font2.render("  %s : %d" % (item_name, item_num), True, (128, 128, 128)) , [100, 100 + line_cnt*20])

    def _default_save_json_path(self):
        import os
        return os.path.abspath(os.path.join("Save", "Default.Save.json"))
    # def _default_save_json_path
                        
    def _save_json_path(self):
        import os
        return os.path.abspath(os.path.join("Save", "aaaaa.Save.json"))
    # def _save_json_path
    
    def _save(self):
        print("Save Start")
        import json
        save_json_path = self._save_json_path()

        save_object = {}
        save_object["PlayerPlacement"] = []
        for player in self.player_objects:
            save_obj = {
                "ObjectId" : player.get_object_id(),
                "Pos" : [player.get_pos()[0],player.get_pos()[1],player.get_pos()[2]],
                "Name" : player.get_name() # FIXME : データ名
            }
            save_object["PlayerPlacement"].append(save_obj)
        # for player_objects

        save_object["ObjectsPlacement"] = []
        for obj in self.objects:
            if obj in self.player_objects:
                continue
            #
            save_obj = {
                "ObjectId" : obj.get_object_id(),
                "Pos" : [obj.get_pos()[0],obj.get_pos()[1], obj.get_pos()[2]],
                "Name" : obj.get_name() # FIXME : データ名
            }
            save_object["ObjectsPlacement"].append(save_obj)
        
        with open(save_json_path, "w") as f:
            json.dump(save_object, f, indent=4)
        print("Save End")
    # def _save
# class SandboxSimpleScene

if __name__ == "__main__":
    pass
