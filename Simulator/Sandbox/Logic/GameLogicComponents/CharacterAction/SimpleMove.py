# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SimpleMove
# @note


class SimpleMove:

    def __init__(self, host_actor):
        self.actor = host_actor
        self.param = { "Speed" : 1.0, "Dir" : (1.0, 0.0, 0.0) }
    # def __init__

    def set_action_param(self, param):
        self.param = param
    # set_action_param

    def update(self):
        speed = self.param["Speed"]
        dir = self.param["Dir"]
        vel = (speed*dir[0], speed*dir[1], speed*dir[2])
        self.actor.get_object_component("Physics").add_velocity(vel)
    #

    def post_update(self):
        pass

# class SimpleMove
