# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SensorDirector
# @note

import math

class SensorDirector:

    def __init__(self):
        pass
    # def __init__

    def update(self, objects):
        # 領域分割
        range_x = (-10000.0, 10000.0)
        range_y = (-10000.0, 10000.0)
        grid_size = (500.0, 500.0)
        grid_num = (
            (int)((range_x[1]-range_x[0])/grid_size[0]),
            (int)((range_y[1]-range_y[0])/grid_size[1])
        )

        check_objects = [[] for x in range(grid_num[0])]
        for x in range(grid_num[0]):
            check_objects[x] = [[] for y in range(grid_num[1])]
            for y in range(grid_num[1]):
                check_objects[x][y] = []

        # 領域分割
        for obj in objects:
            if obj.get_component("Sensor") == None:
                continue
            idx = self._calc_index(obj.next_pos, range_x, range_y, grid_size)
            check_objects[idx[0]][idx[1]].append(obj)

        len_x = len(check_objects)
        len_y = len(check_objects[0])

        for x in range(len_x):
            for y in range(len_y):
                tmp_check_objs = check_objects[x][y]
                len_obj = len(tmp_check_objs)
                # 総当たりチェック
                for i in range(len_obj):
                    for j in range(i+1, len_obj, 1):
                        self._update_obj_sensor(tmp_check_objs[i], tmp_check_objs[j])
                    # for j
                # for i
            # for y
        # for x
                        
        
    # def update

    def _calc_index(self, pos, range_x, range_y, grid_size):
        tmp_x = pos[0] - range_x[0]
        if tmp_x >= 0.0:
            idx_x = (int)(tmp_x / grid_size[0])
        else:
            idx_x = 0

        tmp_y = pos[1] - range_y[1]
        if tmp_y >= 0.0:
            idx_y = (int)(tmp_y / grid_size[1])
        else:
            idx_y = 0

        return (idx_x, idx_y)
    # def _calc_index

    def _update_obj_sensor(self, obj1, obj2):
        sensors1 = obj1.get_component("Sensor")
        sensors2 = obj2.get_component("Sensor")

        for sensor1 in sensors1.sensors:
            for sensor2 in sensors2.sensors:
                sensor1_offset = sensor1.offset
                sensor2_offset = sensor2.offset
                # 確定位置で計算
                diff_x = (obj1.pos[0] + sensor1_offset[0]) - (obj2.pos[0] + sensor2_offset[0])
                diff_y = (obj1.pos[1] + sensor1_offset[1]) - (obj2.pos[1] + sensor2_offset[1])
                diff = math.sqrt(
                    math.pow(diff_x, 2) + math.pow(diff_y, 2)
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
