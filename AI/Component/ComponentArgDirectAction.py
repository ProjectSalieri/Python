# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ComponentArgDirectAction.py
# @note 体を操作する処理をコーディングせずにAIが直値で操作

from IComponentArg import IComponentArg

class ComponentArgDirectAction(IComponentArg):
    ARG_TYPE = "DirectAction"
    
    def __init__(self):
        pass
    # def __init__

    def arg_type(self):
        return ComponentArgDirectAction.ARG_TYPE
    # def arg_type
# class ComponentArgDirectAction

if __name__ == '__main__':
    component_arg = ComponentArgDirectAction()
    print("[ArgType]:" + component_arg.arg_type())
