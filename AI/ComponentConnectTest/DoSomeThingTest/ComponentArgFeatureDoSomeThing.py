# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ComponentArgFeatureDoSomeThing.py
# @note

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",  ".."))

from Component.IComponentArg import IComponentArg

class ComponentArgFeatureDoSomeThing(IComponentArg):
    ARG_TYPE = "ComponentArgFeatureDoSomeThing"
    
    def __init__(self, some_feature):
        self._feature = some_feature
    # def __init__

    def arg_type(self):
        return ComponentArgFeatureDoSomeThing.ARG_TYPE
    # def arg_type
# class ComponentArgFeatureDoSomeThing
