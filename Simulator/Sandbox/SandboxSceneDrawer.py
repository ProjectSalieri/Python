# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SandboxSimpleScene.py
# @note

import pygame
from pygame.locals import *

import Object

class SandboxSceneDrawer:
    
    def __init__(self):
        pass
    # def __init__

    def draw(self, screen, objects, look_at_pos):
        # TODO : ObjectRegionDirectorBase
        priorities = []
        draw_list = {}

        for object in objects:
            priority = object.drawer.get_priority()
            if draw_list.get(priority) == None:
                draw_list[priority] = []
                priorities.append(priority)
            draw_list[priority].append(object)

        priorities.sort()

        for priority in priorities:
            draw_object = draw_list[priority]
            for object in draw_object:
                drawer = object.drawer
                obj_pos = object.get_object_component("Physics").pos
                draw_pos = (obj_pos[0]-look_at_pos[0], obj_pos[1]-look_at_pos[1], obj_pos[2]-look_at_pos[2])
                drawer.draw(draw_pos, screen)
            # for draw_object
        # for priorities
    # def draw

# class SandboxSceneDrawer

if __name__ == "__main__":
    pass
