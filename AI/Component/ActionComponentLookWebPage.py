# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ActionComponentLookWebPage
# @note

from IActionComponent import IActionComponent
from ComponentArgLookWebPage import ComponentArgLookWebPage

class ActionComponentLookWebPage(IActionComponent):
    def __init__(self, virtual_body):
        self._virtual_body = virtual_body
    # def __init__

    def execute(self, args):
        execute_args = _try_get_execute_args(args)
        
        # look_arg = 
        # self._virtual_body.try_stimulate(look_arg)
        pass
    # def execute

    # private
    def _execute_arg_types(self):
        return [ComponentArgLookWebPage.ARG_TYPE]
    # def _execute_arg_types
# class ActionComponentLookWebPage
