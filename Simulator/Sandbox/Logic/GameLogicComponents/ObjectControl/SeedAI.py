# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SeedAI.py
# @note

from Logic.System.MetaAI import MetaAI

class SeedAI:

    def __init__(self, host_actor, parameter):
        self._actor = host_actor
        self._parameter = parameter
        self._seed_count = 0
    # def __init__

    def update(self):
        self._seed_count += 1
        if self._seed_count > self._parameter["SeedTime"]:
            MetaAI.generate_object(self._parameter["Tree"], self._actor.get_pos())
            self._actor.kill()

    def post_update(self):
        pass

# class SeedAI
