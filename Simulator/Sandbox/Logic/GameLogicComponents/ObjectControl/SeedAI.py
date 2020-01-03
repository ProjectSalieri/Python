# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SeedAI.py
# @note

import random

from Logic.System.MetaAI.MetaAI import MetaAI

class SeedAI:

    def __init__(self, host_actor, parameter):
        self._actor = host_actor
        self._parameter = parameter
        self._seed_count = 0
    # def __init__

    def update(self):
        self._seed_count += 1
        if self._seed_count > self._parameter["SeedTime"]:
            self._actor.kill()

            # 木にならない可能性あり
            r = random.randint(0, 100)
            if r < 10:
                pos = self._actor.get_pos()
                pos[1] = 0.0
                MetaAI.generate_object(self._parameter["Tree"], pos)
            

    def post_update(self):
        pass

# class SeedAI
