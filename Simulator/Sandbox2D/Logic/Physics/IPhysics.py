# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IPhysics
# @note

from . import ShapeCube
from . import ShapeSphere

class IPhysics:

    def __init__(self):
        self.shapes = []
    # def __init__

    def init_from_setting(self, setting):
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

    def update(self):
        pass
    # def update

# class Physics

if __name__ == "__main__":
    pass
