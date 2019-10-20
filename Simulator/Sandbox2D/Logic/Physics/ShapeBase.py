# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ShapeBase.py
# @note

class ShapeBase:

    def __init__(self):
        self.offset = (0.0, 0.0)
        self.name = ""

        self.is_hit = False
    # def __init__

    def init_from_setting(self, setting):
        self.name = setting.get("Name")
        offset_setting = setting.get("Offset")
        if offset_setting != None:
            self.offset = (float(offset_setting["X"]), float(offset_setting["Y"]))
        # if offset_setting
    # def __init__

    def get_shape_type(self):
        return "ShapeBase"
    # def get_shape_name

    def update(self, pos):
        self.is_hit = False # 前フレームの結果をリセット
    # def update

# class ShapeBase

if __name__ == "__main__":
    pass
