# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IThinkComponent.py
# @note 思考Componentのインターフェース

from ComponentArgCollection import ComponentArgCollection
from ComponentArgLookWebPage import ComponentArgLookWebPage
from IThinkComponent import IThinkComponent

class ThinkComponentLookWebPage(IThinkComponent):

    def __init__(self):
        self._action_args = ComponentArgCollection()
    # def __init__

    def execute(self, args):
        # self._action_args.append(ComponentArgLookWebPage())
        pass
    # def execute

    # private
    def _executable_arg_types(self):
        return []
    # def _execute_arg_types
    
# class ThinkComponentLookWebPage
