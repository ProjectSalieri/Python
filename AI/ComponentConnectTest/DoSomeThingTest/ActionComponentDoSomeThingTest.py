# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ActionComponentDoSomeThingTest
# @note BodyComponentを使って何かするテスト

from ComponentArgStimulusMemoryCnt import ComponentArgStimulusMemoryCnt

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",  ".."))

from Component.IComponentArg import IComponentArg

class ComponentArgDoSomeThing(IComponentArg):
    ARG_TYPE = "ComponentArgDoSomeThing"
    
    def __init__(self, add_cnt):
        self._add_cnt = add_cnt
    # def __init__

    def arg_type(self):
        return ComponentArgDoSomeThing.ARG_TYPE
    # def arg_type

    def execute_class(self):
        return ActionComponentDoSomeThingTest
    # def execute_class

    def memory_key():
        return "DoSomeThingMemory"
    # def memory_key
# class ComponentArgDoSomeThing

from Component.IActionComponent import IActionComponent

class ActionComponentDoSomeThingTest(IActionComponent):
    def execute(args, body):
        for arg in args:
            if arg.arg_type() == ComponentArgDoSomeThing.ARG_TYPE:
                if (ComponentArgDoSomeThing.memory_key() in body._memory) == False:
                    body._memory[ComponentArgDoSomeThing.memory_key()] = 0
                body._memory[ComponentArgDoSomeThing.memory_key()] += arg._add_cnt
                body.try_stimulate(ComponentArgStimulusMemoryCnt())
    # def execute

# class ActionComponentDoSomeThingTest
