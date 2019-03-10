# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IActionComponent.py
# @note 行動Componentのインターフェース

from IArgExecuteModule import IArgExecuteModule

class IActionComponent(IArgExecuteModule):
    def __init__(self):
        pass
    # def __init__

    def execute(self, args):
        pass
    # def execute

# class IActionComponent
