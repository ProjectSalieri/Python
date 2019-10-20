# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file PhysicsDirector
# @note

import math

class PhysicsDirector:

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
            if obj.get_component("Physics") == None:
                continue
            idx = self._calc_index(obj.pos, range_x, range_y, grid_size)
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
                        self._update_obj_physics(tmp_check_objs[i], tmp_check_objs[j])
                    # for j
                # for i

                # 総当たり情報を反映(とりあえず、ぶつかったら移動中止)
                for obj in tmp_check_objs:
                    self._apply_obj_physics(obj)
                # for obj
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

    def _update_obj_physics(self, obj1, obj2):
        physics1 = obj1.get_component("Physics")
        physics2 = obj2.get_component("Physics")

        for shape1 in physics1.shapes:
            for shape2 in physics2.shapes:
                shape1_offset = shape1.offset
                shape2_offset = shape2.offset
                cube_diff = (
                    math.fabs((obj1.x() + shape1_offset[0]) - (obj2.x() + shape2_offset[0])),
                    math.fabs((obj1.y() + shape1_offset[1]) - (obj2.y() + shape2_offset[1])),
                )

                cube_size1 = shape1.calc_cube_size()
                cube_size2 = shape2.calc_cube_size()

                if cube_diff[0] > cube_size1[0] + cube_size2[0]:
                    continue
                if cube_diff[1] > cube_size1[1] + cube_size2[1]:
                    continue

                shape1.is_hit = True
                shape2.is_hit = True
            # for shape2
        # for shape1
    # def _update_obj_physics

    def _apply_obj_physics(self, obj):
        is_hit_any = False
        shapes = obj.get_component("Physics").shapes
        for shape in shapes:
            if shape.is_hit:
                is_hit_any = True
                break
        # for shape

        # 特に接触がなかったので移動反映
        if is_hit_any == False:
            obj.pos = (obj.pos[0] + obj.velocity[0], obj.pos[1] + obj.velocity[1])

        # 2Dなので慣性なしで実装スタート
        if True:
            obj.velocity = (0.0, 0.0)

        for shape in shapes:
            shape.update(obj.pos)
    # def _apply_obj_physics

# class PhysicsDirector

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
