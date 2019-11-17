# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file Simulator2D.py
# @note

from ActorUtil import ActorUtil

class Object2D:

    def __init__(self, name):
        self.pos = (0.0, 0.0)
        self.next_pos = (0.0, 0.0)
        self.velocity = (0.0, 0.0)
        self.half_size = (0, 0)

        # 初期化ファイル
        actor_setting = ActorUtil.load_actor_setting(name)

        self.object_components = ActorUtil.create_object_components(actor_setting)
        self.game_data_components = ActorUtil.create_game_data_components(actor_setting)

        self.drawer = self.game_data_components["Draw"]

    # def __init__

    def get_object_component(self, component_name):
        return self.object_components.get(component_name)
    # get_object_component

    def add_velocity(self, vel):
        self.velocity = (self.velocity[0] + vel[0], self.velocity[1] + vel[1])
    # add_velocity

    def update(self):
        # Object共通コンポーネント
        for name, component in self.object_components.items():
            component.update()
        # ゲーム用コンポーネント
        for name, component in self.game_data_components.items():
            component.update()

        self.next_pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])
    # def update

    def post_update(self):
        # Object共通コンポーネント
        for name, component in self.object_components.items():
            component.post_update()
        # ゲーム用コンポーネント
        for name, component in self.game_data_components.items():
            component.post_update()
    # def post_update

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
