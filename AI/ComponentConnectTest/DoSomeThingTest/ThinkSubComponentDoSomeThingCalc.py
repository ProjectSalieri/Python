# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ThinkComponentDoSomeThing.py
# @note なにかする思考コンポーネント

from ComponentArgFeatureDoSomeThing import ComponentArgFeatureDoSomeThing
from ActionComponentDoSomeThingTest import ActionComponentDoSomeThingTest
from ActionComponentDoSomeThingTest import ComponentArgDoSomeThing

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",  ".."))

from Component.IThinkComponent import IThinkComponent

class ThinkSubComponentDoSomeThingCalc(IThinkComponent):
    def __init__(self):
        self._state = "Init"
        pass
    # def __init__
    
    # ComponentArgsAction~をarrayで返す
    def execute(self, args, body):
        print("ThinkSubComponentDoSomeThingCalc : " + self._state)
        return_args = []
        if self._state == "Init":
            return self._state_init(args, body)
        elif self._state == "Add":
            return self._state_add(args, body)
        elif self._state == "Minus":
            pass
                
        return return_args
    # def execute

    def _state_init(self, args, body):
        return_args = []
        for arg in args:
            if arg.arg_type() == ComponentArgFeatureDoSomeThing.ARG_TYPE:
                print("Let's DoSomeThing")
                val = arg._feature
                return_args.append(ComponentArgDoSomeThing(val+1))
                self._state = "Add"
                #
            #
        return return_args
    # def _state_init

    def _state_add(self, args, body):
        return_args = []
        for arg in args:
            if arg.arg_type() == ComponentArgFeatureDoSomeThing.ARG_TYPE:
                if ComponentArgDoSomeThing.memory_key() in body._memory and body._memory[ComponentArgDoSomeThing.memory_key()] > 5:
                    print("DoSomeThing Finished!")
                    self._state = "Minus"
                else:
                    print("Let's Continue DoSomeThing")
                    val = arg._feature
                    return_args.append(ComponentArgDoSomeThing(val+1))
                #
            #
        return return_args
    # def _state_init

    def _state_minus(self, args, body):
        pass
    # def _state_init
# class ThinkSumComponentDoSomeThingCalc
