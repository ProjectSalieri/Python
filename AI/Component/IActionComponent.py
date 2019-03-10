# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IActionComponent.py
# @note 行動Componentのインターフェース

class IActionComponent:
    def __init__(self):
        pass
    # def __init__

    def execute(self, args):
        pass
    # def execute

    # private
    def _execute_arg_types(self):
        return []
    
    def _try_get_execute_args(self, args):
        arg_types = self._execute_arg_types()
        result_args = []
        for arg in args:
            if arg.arg_type() in arg_types:
                result_args.append(arg)
        return result_args
# class IActionComponent
