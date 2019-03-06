# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ComponentArgStimulusLook.py
# @note 

from IComponentArg import IComponentArg

class ComponentArgStimulusLook(IComponentArg):
    ARG_TYPE = "StimulusLook"
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.pixel = None
        pass
    # def __init__

    # 画像パスではなく、生のピクセル情報を設定
    def set_pixel(self, pixel):
        self._pixel = pixel
    # def set_pixel

    def is_pixel(self):
        return self.pixel != None
    # def is_pixel

    def arg_type(self):
        return ComponentArgStimulusLook.ARG_TYPE
    # def arg_type
# class ComponentArgStimulusLook

if __name__ == '__main__':
    print("=====FilePath type=====")
    component_arg = ComponentArgStimulusLook("D:/tmp/test.png")
    print("[ArgType]:" + component_arg.arg_type())
    print("[isPixel]:" + str(component_arg.is_pixel()))
    print("[FilePath]:" + component_arg.file_path)

    print("\n")

    print("=====Pixel type=====")
    component_arg = ComponentArgStimulusLook(None)
    component_arg.set_pixel([])
    print("[ArgType]:" + component_arg.arg_type())
    print("[isPixel]:" + str(component_arg.is_pixel()))
