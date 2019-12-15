# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SalieriDebugger.py
# @note

import multiprocessing
from multiprocessing import Process

from SandboxSceneDrawer import SandboxSceneDrawer

class SalieriDebugger:

    def __init__(self, virtual_scene):
        self._virtual_scene = virtual_scene

#        self._process_queue = multiprocessing.Queue()
#        self._process = Process(target=self.update_thread_func, args=(self._process_queue,))
#        self._process.start()
#        self._process_queue.put(0)

#        self._process_queue.put(self._virtual_scene)
    # def __init__

    def update_thread_func(self, queue):
        # 親プロセスから仮想シーンのインスタンス取得
        
        virtual_scene = queue.get()
        import pygame
        pygame.init
        clock = pygame.time.Clock()
#        screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("SalieriDebugger")

        signal = None

        cnt = 0
        while signal == None:
            cnt = cnt + 1
            if cnt % 10 == 0:
                print("AAWA")
            import time
            time.sleep(1)
            signal = queue.get()
#            clock.tick(20) # 低頻度でいい

#            self.update()
            # 背景色リセット
#            screen.fill((255,255,255,))

#            look_at_pos = virtual_scene.object_self.get_object_component("Physics").pos
#            objects = virtual_scene.objects
#            SandboxSceneDrawer().draw(screen, objects, look_at_pos)
#            self.draw()

#            pygame.display.update()
#        pygame.quit()
    # def draw_thread_func

    def update(self):
        pass
    # def update

    def draw(self):
        # 背景色リセット
        self.screen.fill((255,255,255,))

        look_at_pos = self._virtual_scene.object_self.get_object_component("Physics").pos
        objects = self._virtual_scene.objects
        SandboxSceneDrawer().draw(self.screen, objects, look_at_pos)
    # def draw

    def shutdown(self):
        print("SalieriDebugger shutdown")
#        self._process_queue.put(True)
#        self._process.join()
    # def shutdown

# class Salieri

if __name__ == "__main__":
    pass
