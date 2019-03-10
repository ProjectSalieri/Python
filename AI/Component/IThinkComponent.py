# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IThinkComponent.py
# @note 思考Componentのインターフェース

from IArgExecuteModule import IArgExecuteModule

class IThinkComponent(IArgExecuteModule):
    def __init__(self):
        pass
    # def __init__

    # ComponentArgsAction~をarrayで返す
    def execute(self, args):
        pass
    # def execute
# class IThinkComponent
