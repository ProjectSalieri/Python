# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file TreeAI.py
# @note

import random
import numpy as np

from Logic.System.MetaAI.MetaAI import MetaAI

class TreeAI:

    def __init__(self, host_actor, parameter):
        self._actor = host_actor
        self._parameter = parameter

        self._nut_interval = 0
        self._set_nut_interval_internal()

        MetaAI.regist_as_tree_object(host_actor)
    # def __init__

    def update(self):
        self._nut_interval -= 1
        if self._nut_interval < 0:
            self._set_nut_interval_internal()
            MetaAI.generate_object(self._parameter["TreeNut"], self._actor.get_pos() + np.array([32, 0, 0]))
            

    def post_update(self):
        pass

    # MetaAIも含めて、次に実がなる間隔を設定
    def set_nut_interval(self, interval):
        rand_max = (int)(interval/10)
        self._nut_interval = interval + random.randint(-rand_max, rand_max)
    # def set_nut_interval

    def _set_nut_interval_internal(self):
        self.set_nut_interval(self._parameter["NutInterval"])
    # def _set_nut_interval_internal

# class TreeAI
