# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file TreeAI.py
# @note

from Logic.System.MetaAI import MetaAI

class TreeAI:

    def __init__(self, host_actor, parameter):
        self._actor = host_actor
        self._parameter = parameter

        MetaAI.regist_as_tree_object(host_actor)
    # def __init__

    def update(self):
        pass
            

    def post_update(self):
        pass

# class TreeAI
