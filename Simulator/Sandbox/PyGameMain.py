# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file PyGameMain.py
# @note

import pygame
from pygame.locals import *
import sys

class PyGameMain:
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400

    def __init__(self, app):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(app.screen_size())
        pygame.display.set_caption(app.name())

        self.app = app
    # def __init__

    def main_loop(self):
        while True:
            self.clock.tick(60)

            # app更新
            self.app.update()
            self.app.draw(self.screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit_game()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.quit_game()
            
    # def main_loop

    def quit_game(self):
        print("QuitGame")
        print("App Quit Start")
        self.app.quit_game()
        print("App Quit End")

        print("pygame quit start")
        pygame.quit()
        print("pygame quit end")
        print("sys exit")
        import sys
        sys.exit()
    # def quit_game

# class PyGameMain

if __name__ == "__main__":
    import Sandbox2D
    framework = PyGameMain(Sandbox2D.Sandbox2D())
    framework.main_loop()
