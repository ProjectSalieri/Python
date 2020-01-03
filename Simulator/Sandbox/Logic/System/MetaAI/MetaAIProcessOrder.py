# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MetaAIProcess.py
# @note

class MetaAIProcessOrder:

    ORDER_GENERATE_TREE_FOOD = 0 #"GenerateTreeFood"
    ORDER_GENERATE_ENEMY = 1 #"GenerateEnemy"

    def __init__(self, order, object_id, option):
        self._order = order
        self._object_id = object_id
        self._option = option
    # def __init__

    def get_order(self):
        return self._order

    def get_object_id(self):
        return self._object_id

    def get_option(self):
        return self._option

# class MetaAIProcessOrder

