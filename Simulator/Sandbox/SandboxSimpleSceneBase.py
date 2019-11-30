# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SandboxSimpleSceneBase.py
# @note

import Object

from Logic.Sensor import SensorDirector
from Logic.Physics import PhysicsDirector
from Logic.System.ObjectUpdateDirector import ObjectUpdateDirector

class SandboxSimpleSceneBase:

    def __init__(self):
        self.objects = []

        # データ読み込み
        self._init_scene_from_data()

        #self.sensor_director = SensorDirector.SensorDirector()
        self.object_udpate_director = ObjectUpdateDirector()
        self.physics_director = PhysicsDirector.PhysicsDirector()
    # def __init__

    def _init_scene_from_data(self):
        pass
    # def _init_scene_from_data

    def update(self):
        pass
    # def update

    def _update_common(self, center_pos):
        self.object_udpate_director.update(self.objects, center_pos)

        self.physics_director.update(self.objects, center_pos)
    # def _update_common
        

# class SandboxSimpleSceneBase

if __name__ == "__main__":
    pass
