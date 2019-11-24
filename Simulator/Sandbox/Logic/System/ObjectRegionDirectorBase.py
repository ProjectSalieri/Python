# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ObjectRegionDirector.py
# @note Objectを領域ごとに管理するクラスのベース

import math

class ObjectRegionDirectorBase:

    def __init__(self):
        # 領域分割パラメータ
        self.range_x = (-10000.0, 10000.0)
        self.range_z = (-10000.0, 10000.0)
        self.grid_size = (500.0, 0.0, 500.0)
        self.grid_num = (
            (int)((self.range_x[1]-self.range_x[0])/self.grid_size[0]),
            0,
            (int)((self.range_z[1]-self.range_z[0])/self.grid_size[2])
        )
    # def __init__

    def update(self, objects):
        check_objects = [[] for x in range(self.grid_num[0])]
        for x in range(self.grid_num[0]):
            check_objects[x] = [[] for z in range(self.grid_num[2])]
            for y in range(self.grid_num[1]):
                check_objects[x][z] = []

        # 領域分割
        for obj in objects:
            physics = obj.get_object_component("Physics")
            if physics == None:
                continue
            idx = self._calc_index(physics.next_pos, self.range_x, self.range_z, self.grid_size)
            check_objects[idx[0]][idx[1]].append(obj)

        len_x = len(check_objects)
        len_z = len(check_objects[0])

        for x in range(len_x):
            for z in range(len_z):
                objs_in_region = check_objects[x][z]

                self._update_region(objs_in_region)
            # for y
        # for x
                        
        
    # def update

    def _calc_index(self, pos, range_x, range_z, grid_size):
        tmp_x = pos[0] - range_x[0]
        if tmp_x >= 0.0:
            idx_x = (int)(tmp_x / grid_size[0])
        else:
            idx_x = 0

        tmp_z = pos[2] - range_z[0]
        if tmp_z >= 0.0:
            idx_z = (int)(tmp_z / grid_size[2])
        else:
            idx_z = 0

        return (idx_x, idx_z)
    # def _calc_index

    # 継承先で実装
    def _update_region(self, objects_in_region):
        pass
    # def _update_region

# class ObjectRegionDirector

if __name__ == "__main__":
    pass
