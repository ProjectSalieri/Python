# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ComponentArgRest.py
# @note

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",  ".."))

from Component.IComponentArg import IComponentArg

class ComponentArgRest(IComponentArg):
    ARG_TYPE = "ComponentArgRest"
    
    def __init__(self, args):
        self._args_stack = args
    # def __init__

    def arg_type(self):
        return ComponentArgRest.ARG_TYPE
    # def arg_type

# class ComponentArgRest
