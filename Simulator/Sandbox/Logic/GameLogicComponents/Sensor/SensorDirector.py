# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SensorDirector
# @note

import math

from ...System.ObjectRegionDirectorBase import ObjectRegionDirectorBase

class SensorDirector(ObjectRegionDirectorBase):

    def __init__(self):
        super().__init__()
    # def __init__

    def _update_region(self, objs_in_region):
        len_obj = len(objs_in_region)
        # 総当たりチェック
        for i in range(len_obj):
            for j in range(i+1, len_obj, 1):
                self._update_obj_sensor(objs_in_region[i], objs_in_region[j])
            # for j
        # for i

    def _update_obj_sensor(self, obj1, obj2):
        sensors1 = obj1.get_game_logic_component("Sensor")
        if sensors1 == None:
            return None
        sensors2 = obj2.get_game_logic_component("Sensor")
        if sensors2 == None:
            return None

        pos1 = obj1.get_object_component("Physics").pos
        pos2 = obj2.get_object_component("Physics").pos

        for sensor1 in sensors1.sensors:
            for sensor2 in sensors2.sensors:
                sensor1_offset = sensor1.offset
                sensor2_offset = sensor2.offset
                # 確定位置で計算
                diff_x = (pos1[0] + sensor1_offset[0]) - (pos2[0] + sensor2_offset[0])
                diff_y = (pos1[1] + sensor1_offset[1]) - (pos2[1] + sensor2_offset[1])
                diff_z = (pos1[2] + sensor1_offset[2]) - (pos2[2] + sensor2_offset[2])
                diff = math.sqrt(
                    math.pow(diff_x, 2) + math.pow(diff_y, 2) + math.pow(diff_z, 2)
                )

                radius1 = sensor1.radius
                radius2 = sensor2.radius

                if diff > radius1 + radius2:
                    continue

                sensor1.hit_sensors.append(sensor2)
                sensor2.hit_sensors.append(sensor1)
            # for sensor2
        # for sensor1
    # def _update_obj_sensor

# class SensorDirector

if __name__ == "__main__":

    arr = [[] for x in range(2)]
    for x in range(2):
        arr[x] = [[] for y in range(3)]
        for y in range(3):
            arr[x][y] = [[] for obj in range(4)]

    print(arr)
    print(len(arr))
    print(len(arr[0]))
    print(len(arr[0][0]))
