# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file Simulator2D.py
# @note

from ActorUtil import ActorUtil
import IDraw

class Object2D:

    def __init__(self, name):
        self.pos = (0.0, 0.0)
        self.velocity = (0.0, 0.0)
        self.half_size = (0, 0)

        # 初期化ファイル
        actor_setting = ActorUtil.load_actor_setting(name)

        self.components = {}
        self.drawer = None
        for component in actor_setting["Components"]:
            if component == "Draw":
                draw_setting = ActorUtil.load_component_setting(actor_setting, component)
                self.drawer = IDraw.IDraw(draw_setting["Image"])
            else:
                self.components[component] = ActorUtil.create_component(actor_setting, component)
    # def __init__

    def get_component(self, component_name):
        return self.components.get(component_name)
    # get_component

    def add_velocity(self, vel):
        self.velocity = (self.velocity[0] + vel[0], self.velocity[1] + vel[1])
    # add_velocity

    def update(self):
        for name, component in self.components.items():
            component.update()
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
