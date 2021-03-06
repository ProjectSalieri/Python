# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file Sandbox2D.py
# @note

import pygame
from pygame.locals import *

import SandboxSimpleScene

class Sandbox2D:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode()
        pygame.display.set_caption("Sandbox2D")

        self.scene = SandboxSimpleScene.SandboxSimpleScene()
    # def __init__

    def screen_size(self):
        return (Sandbox2D.SCREEN_WIDTH, Sandbox2D.SCREEN_HEIGHT)
    # def screen_size

    def name(self):
        return "Sandbox2D"
    # name

    def update(self):
        # Clientの操作情報だけ送信して、サーバーで姿勢等更新するのもあり
        self.scene.update()
    # def update

    def draw(self, screen):
        # クラウドゲームみたくサーバーで画像生成して、画像だけ描画するとかもあり
        
        # 背景色リセット
        screen.fill((255,255,255,))

        self.scene.pre_draw(screen)

        self.scene.draw(screen)
    # def draw

    def quit_game(self):
        self.scene.kill()
    # def quit_game

# class Sandbox2D

if __name__ == "__main__":
    sandbox = Sandbox2D()
    sandbox.main_loop()
