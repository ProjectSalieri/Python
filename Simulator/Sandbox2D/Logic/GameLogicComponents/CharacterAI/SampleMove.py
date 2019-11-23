# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SampleMove.py
# @note


class SampleMove:

    def __init__(self, host_actor):
        self.actor = host_actor
        self.counter = 0
        self.is_reverse = False
        pass
    # def __init__

    def update(self):
        self.counter = self.counter + 1
        if self.counter % 60 == 0:
            self.is_reverse = self.is_reverse == False
        
        if self.is_reverse:
            self.actor.add_velocity((-1.0, 0.0))
        else:
            self.actor.add_velocity((1.0, 0.0))
        #if counter

    def post_update(self):
        pass

# class SampleMove
