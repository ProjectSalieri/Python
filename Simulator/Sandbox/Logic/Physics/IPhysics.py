# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IPhysics
# @note

from . import ShapeCube
from . import ShapeSphere

import numpy as np

class IPhysics:

    def __init__(self):
        self.shapes = []
        self.is_ground = False

        self.mass = 0.0

        # 代表位置、速度
        self.pos = (0.0, 0.0, 0.0)
        self.next_pos = (0.0, 0.0, 0.0)
        self.velocity = (0.0, 0.0, 0.0)
    # def __init__

    def init_from_setting(self, setting):
        self.is_ground = True if setting.get("IsGround") == "True" else False
        if self.is_ground == True:
            return None
        
        self.mass = setting["Mass"]
        shape_settings = setting["Shapes"]
        for shape_setting in shape_settings:
            shape_type = shape_setting["Shape"]
            shape = None
            if shape_type == "Cube":
                shape = ShapeCube.ShapeCube()
            elif shape_type == "Shpere":
                shape = ShapeSphere.ShapeSphere()
            shape.init_from_setting(shape_setting)
            self.shapes.append(shape)
        # for shape_settings
    # def init_from_setting

    def get_pos(self):
        # 互換
        return np.array([self.pos[0], self.pos[1], self.pos[2]])

    def reset_pos(self, pos):
        self.velocity = (0.0, 0.0, 0.0)
        self.pos = pos
        # TODO : 前フレームの結果使うようならフラグ立てる

    def add_velocity(self, vel):
        self.velocity = (self.velocity[0] + vel[0], self.velocity[1] + vel[1], self.velocity[2] + vel[2])
    # add_velocity

    def update(self):
        # 物理挙動による速度更新(ex. 摩擦)
        fric_tmp = 0.8
        self.velocity = (self.velocity[0]*fric_tmp, self.velocity[1]*fric_tmp, self.velocity[2]*fric_tmp)
    # def update

    def post_update(self):
        # Physics + AIによる速度決定後にPhysicsDirector
        self.next_pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1], self.pos[2] + self.velocity[2])
    # def post_update

    # 全ての計算の後に結果反映
    def apply(self):
        self.pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1], self.pos[2] + self.velocity[2])
        for shape in self.shapes:
            shape.update(self.pos)
    # def apply

# class Physics

if __name__ == "__main__":
    pass
