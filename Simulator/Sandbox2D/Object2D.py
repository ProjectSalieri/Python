# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file Simulator2D.py
# @note

import IDraw

class Object2D:

    def __init__(self, name):
        self.pos = (0.0, 0.0)
        self.half_size = (0, 0)

        # 初期化ファイル
        import os
        actor_data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ActorData")
        actor_json = os.path.join(actor_data_dir, "Actor", "%s.Actor.json" % (name))
        actor_setting = None
        import json
        with open(actor_json) as f:
            actor_setting = json.load(f)

        self.components = []
        self.drawer = None
        for component in actor_setting["Components"]:
            if component == "Draw":
                draw_json = os.path.join(actor_data_dir, actor_setting["Components"]["Draw"])
                image_name = None
                with open(draw_json) as f:
                    image_name = json.load(f)["Image"]
                self.drawer = IDraw.IDraw(image_name)
    # def __init__

    def update(self):
        pass
    # def update

    def draw(self, screen):
        #pygame.draw.rect(screen, (255,128,0), pygame.Rect(self.x() - self.half_w(),self.y() - self.half_h(),self.x() + self.half_w(),self.y() + self.half_h()))
        if self.drawer != None:
            self.drawer.draw(self.pos, screen)
    # def draw

    def x(self):
        return self.pos[0]
    def y(self):
        return self.pos[1]
    def half_w(self):
        return self.half_size[0]
    def half_h(self):
        return self.half_size[1]
    
# class Object2D

if __name__ == "__main__":
    pass
