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
        range_z = (-10000.0, 10000.0)
        grid_size = (500.0, 0.0, 500.0)
        grid_num = (
            (int)((range_x[1]-range_x[0])/grid_size[0]),
            0,
            (int)((range_z[1]-range_z[0])/grid_size[2])
        )

        check_objects = [[] for x in range(grid_num[0])]
        for x in range(grid_num[0]):
            check_objects[x] = [[] for z in range(grid_num[2])]
            for y in range(grid_num[1]):
                check_objects[x][z] = []

        # 領域分割
        for obj in objects:
            physics = obj.get_object_component("Physics")
            if physics == None:
                continue
            idx = self._calc_index(physics.next_pos, range_x, range_z, grid_size)
            check_objects[idx[0]][idx[1]].append(obj)

        len_x = len(check_objects)
        len_z = len(check_objects[0])

        for x in range(len_x):
            for z in range(len_z):
                tmp_check_objs = check_objects[x][z]
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

    def _update_obj_physics(self, obj1, obj2):
        physics1 = obj1.get_object_component("Physics")
        physics2 = obj2.get_object_component("Physics")

        # ここから下はObject2D関係ない計算(=IPhysicsで完結)
        is_hit_any = False

        for shape1 in physics1.shapes:
            for shape2 in physics2.shapes:
                shape1_offset = shape1.offset
                shape2_offset = shape2.offset
                cube_diff = (
                    math.fabs((physics1.next_pos[0] + shape1_offset[0]) - (physics2.next_pos[0] + shape2_offset[0])),
                    math.fabs((physics1.next_pos[1] + shape1_offset[1]) - (physics2.next_pos[1] + shape2_offset[1])),
                    math.fabs((physics1.next_pos[2] + shape1_offset[2]) - (physics2.next_pos[2] + shape2_offset[2])),
                )

                cube_size1 = shape1.calc_cube_size()
                cube_size2 = shape2.calc_cube_size()

                if cube_diff[0] > cube_size1[0] + cube_size2[0]:
                    continue
                if cube_diff[1] > cube_size1[1] + cube_size2[1]:
                    continue
                if cube_diff[2] > cube_size1[2] + cube_size2[2]:
                    continue

                shape1.is_hit = True
                shape2.is_hit = True
                is_hit_any = True
            # for shape2
        # for shape1

        # モーメントは無視して衝突による速度反映
        if is_hit_any == True:
            # TODO : 質量差
            vel1 = physics1.velocity
            m1 = physics1.mass
            vel2 = physics2.velocity
            m2 = physics2.mass
            sum_m = m1 + m2
            new_vel1 = ( ((m1-m2)*vel1[0] + 2.0*m2*vel2[0])/sum_m,
                         ((m1-m2)*vel1[1] + 2.0*m2*vel2[1]) / sum_m,
                         ((m1-m2)*vel1[2] + 2.0*m2*vel2[2]) / sum_m )
            new_vel2 = ( (2.0*m1*vel1[0] + (m2-m1)*vel2[0])/sum_m,
                         (2.0*m1*vel1[1] + (m2-m1)*vel2[1])/sum_m,
                         (2.0*m1*vel1[2] + (m2-m1)*vel2[2])/sum_m )
            physics1.velocity = new_vel1
            physics2.velocity = new_vel2
    # def _update_obj_physics

    def _apply_obj_physics(self, obj):
        is_hit_any = False
        physics = obj.get_object_component("Physics")

        # ここから下はObject2D関係ない計算(=IPhysics)
        shapes = physics.shapes
        for shape in shapes:
            if shape.is_hit:
                is_hit_any = True
                break
        # for shape

#        if is_hit_any == True:
#            physics.velocity = (0.0, 0.0)

        physics.apply()

        # 2Dなので慣性なしで実装スタート
        if False:
            physics.velocity = (0.0, 0.0, 0.0)
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
