# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ObjectSenseDirector
# @note

import math

from .ObjectRegionDirectorBase import ObjectRegionDirectorBase

import numpy as np

class ObjectSenseDirector(ObjectRegionDirectorBase):

    def __init__(self):
        super().__init__()
    # def __init__

    def _update_region(self, objs_in_region):
        for obj1 in objs_in_region:
            for obj2 in objs_in_region:
                if obj1 == obj2:
                    continue

                self._update_eyesight(obj1, obj2)
                self._update_smell(obj1, obj2)
        # for objs_in_region
    # def _update_region

    def _update_eyesight(self, obj1, obj2):
        sense1 = obj1.get_object_component("Sense")
        eye_sensor1 = None
        if sense1 != None:
            eye_sensor1 = sense1.try_get_eye_sensor()
        sense2 = obj2.get_object_component("Sense")
        eye_sensor2 = None
        if sense2 != None:
            eye_sensor2 = sense2.try_get_eye_sensor()

        # 視覚センサーがともになければ何もしない
        if eye_sensor1 == None and eye_sensor2 == None:
            return None

        diff = obj1.get_pos() - obj2.get_pos()
        dist = np.linalg.norm(diff)

        if eye_sensor1 != None and eye_sensor1.calc_enable_sense(dist) == True:
            eye_sensor1.add_sense_object(obj2)
        if eye_sensor2 != None and eye_sensor2.calc_enable_sense(dist) == True:
            eye_sensor2.add_sense_object(obj1)

    # def _update_eyesight

    def _update_smell(self, obj1, obj2):
        pass
    # def _update_smell
        
# class ObjectSenseDirector

if __name__ == "__main__":
    pass
