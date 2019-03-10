# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ActionComponentLookWebPage
# @note

from IActionComponent import IActionComponent
from IBodyComponent import IBodyComponent
from ComponentArgLookWebPage import ComponentArgLookWebPage

class ActionComponentLookWebPage(IActionComponent):
    def __init__(self, virtual_body):
        self._virtual_body = virtual_body
    # def __init__

    def execute(self, args):
        _execute_core(args)

        _stimulate([])
        
        # look_arg = 
        # self._virtual_body.try_stimulate(look_arg)
        pass
    # def execute

    # private
    def _executable_arg_types(self):
        return [ComponentArgLookWebPage.ARG_TYPE]
    # def _execute_arg_types

    def _execute_core(self, args):
        execute_args = self._executable_args(args)
    # def _execute_core

    def _stimulate(self, args):
        for arg in args:
            self._virtual_body.try_stimulate(arg)
        # for
    # def _stimulate
# class ActionComponentLookWebPage


if __name__ == '__main__':
    action = ActionComponentLookWebPage(IBodyComponent())
    action._execute_core([ComponentArgLookWebPage()])
