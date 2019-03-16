# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ThinkComponentDoSomeThing.py
# @note なにかする思考コンポーネント

from ThinkSubComponentDoSomeThingCalc import ThinkSubComponentDoSomeThingCalc

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",  ".."))

from Component.IThinkComponent import IThinkComponent

class ThinkComponentDoSomeThing(IThinkComponent):
    def __init__(self):
        self._sub_components = [
            ThinkSubComponentDoSomeThingCalc(),
        ]
    # def __init__
    
    # ComponentArgsAction~をarrayで返す
    def execute(self, args, body):
        return_args = []
        for sub_component in self._sub_components:
            return_args += sub_component.execute(args, body)

        return return_args
    # def execute
# class ThinkComponentDoSomeThing
