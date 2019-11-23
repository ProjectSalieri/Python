# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ShapeSphere.py
# @note

from . import ShapeBase

class ShapeSphere(ShapeBase.ShapeBase):

    def __init__(self):
        super().__init__()
        self.radius = 0.0
    # def __init__

    def init_from_setting(self, setting):
        super().init_from_setting(setting)

        size_setting = setting["Size"]
        self.radius = float(size_setting["Radius"])
    # def __init__

    def get_shape_type(self):
        return "ShapeSphere"
    # def get_shape_name

    def calc_cube_size(self):
        return (self.radius, self.radius)
    # def calc_cube_size

# class ShapeSphere

if __name__ == "__main__":
    pass
