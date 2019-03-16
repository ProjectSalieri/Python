# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ThinkComponentDoSomeThing.py
# @note なにかする思考コンポーネント

from ComponentArgRest import ComponentArgRest
from ThinkSubComponentDoSomeThingCalc import ThinkSubComponentDoSomeThingCalc
from ThinkSubComponentRestTest import ThinkSubComponentRestTest

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",  ".."))

from Component.IThinkComponent import IThinkComponent

class ThinkComponentDoSomeThing(IThinkComponent):
    def __init__(self):
        self._pre_sub_components = [
            ThinkSubComponentRestTest(),
        ]
        self._sub_components = [
            ThinkSubComponentDoSomeThingCalc(),
        ]
    # def __init__
    
    # ComponentArgsAction~をarrayで返す
    def execute(self, args, body):
        for pre_sub_component in self._pre_sub_components:
            return_args_pre = pre_sub_component.execute(args, body)

            for arg_pre in return_args_pre:
                if arg_pre.arg_type() == ComponentArgRest.ARG_TYPE:
                    print("ThinkComponentDoSomeThing : Rest")
                    return []
                #
            #
        #
        
        return_args = []
        for sub_component in self._sub_components:
            return_args += sub_component.execute(args, body)

        return return_args
    # def execute
# class ThinkComponentDoSomeThing
