# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ShapeCube.py
# @note

from . import ShapeBase

class ShapeCube(ShapeBase.ShapeBase):

    def __init__(self):
        super().__init__()
        self.half_size = (0.0, 0.0, 0.0)
    # def __init__

    def init_from_setting(self, setting):
        super().init_from_setting(setting)

        size_setting = setting["Size"]
        self.half_size = (float(size_setting["WidthX"]), float(size_setting["Height"]), float(size_setting["WidthZ"]))

    # def __init__

    def get_shape_type(self):
        return "ShapeCube"
    # def get_shape_name

    def calc_cube_size(self):
        return self.half_size
    # def calc_cube_size

# class ShapeCube

if __name__ == "__main__":
    import ShapeBase
    shape = ShapeCube()
