# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SampleMove.py
# @note

from ..CharacterAction import SimpleMove

class SampleMove:

    def __init__(self, host_actor):
        self.actor = host_actor
        self.counter = 0
        self.state = 0
        self.actions = {"Move" : SimpleMove.SimpleMove(host_actor)}
        self.actions["Move"].set_action_param({"Speed" : 1.0, "Dir" : (1.0, 0.0, 0.0) })
        pass
    # def __init__

    def update(self):
        self.counter = self.counter + 1
        if self.counter % 60 == 0:
            self.state = (self.state+1) %4
            import random
            self.counter = random.randint(0, 10) %  10

        if self.state == 0:
            self.actions["Move"].set_action_param({"Speed" : 1.0, "Dir" : (1.0, 0.0, 0.0) })
        elif self.state == 2:
            self.actions["Move"].set_action_param({"Speed" : 1.0, "Dir" : (-1.0, 0.0, 0.0) })
        else:
            # Stop
            self.actions["Move"].set_action_param({"Speed" : 0.0, "Dir" : (0.0, 0.0, 0.0) })


        self.actions["Move"].update()

        #if counter

    def post_update(self):
        pass

# class SampleMove
