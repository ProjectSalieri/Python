# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SalieriVirtualScene.py
# @note

from SandboxSimpleSceneBase import SandboxSimpleSceneBase

from Salieri.SalieriVirtualObject import SalieriVirtualObject

class SalieriVirtualScene(SandboxSimpleSceneBase):

    def __init__(self):
        self.object_self = None
        super().__init__()
    # def __init__

    def _init_scene_from_data(self):
        self.object_self = SalieriVirtualObject("Sample")

        self.objects.append(self.object_self)
    # def _init_scene_from_data

    def update(self):
        self._update_common(self.object_self.get_object_component("Physics").pos)
    # def update

# class SalieriVirtualScene

if __name__ == "__main__":
    pass
