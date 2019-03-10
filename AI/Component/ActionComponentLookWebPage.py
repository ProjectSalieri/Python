# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ActionComponentLookWebPage
# @note

from IActionComponent import IActionComponent
from BodyComponentPCVirtual import BodyComponentPCVirtual

from IComponentArg import IComponentArg
class ComponentArgLookWebPage(IComponentArg):
    ARG_TYPE = "LookWebPage"

    def __init__(self):
        pass
    # def __init__

    def arg_type(self):
        return ComponentArgLookWebPage.ARG_TYPE
    # def arg_type
# class ComponentArgLookWebPage

class ActionComponentLookWebPage(IActionComponent):
    def __init__(self, virtual_body):
        self._virtual_body = virtual_body
    # def __init__

    def execute(self, arg):
        # look_arg = 
        # self._virtual_body.try_stimulate(look_arg)
        pass
    # def execute
# class ActionComponentLookWebPage
