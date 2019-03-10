# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IArgExecuteModule.py
# @note ComponentArgを使う関数のインターフェース

class IArgExecuteModule:

    # 実行可能な引数のarg_type
    def _executable_arg_types(self):
        return []
    # def _execute_arg_types

    # 実行可能な引数のarg_type
    def _executable_args(self, args):
        arg_types = self._executable_arg_types()
        result_args = []
        for arg in args:
            if arg.arg_type() in arg_types:
                result_args.append(arg)
        return result_args
    # def _try_get_execute_args
