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

class ThinkComponentDoSomeThing(IThinkComponent):
    # ComponentArgsAction~をarrayで返す
    def execute(args, body):
        return_args = []
        for arg in args:
            if arg.arg_type() == ComponentArgFeatureDoSomeThing.ARG_TYPE:
                # ThinkComponent内で条件判定等をして次のActionComponentを設定
                if ComponentArgDoSomeThing.memory_key() in body._memory and body._memory[ComponentArgDoSomeThing.memory_key()] > 5:
                    print("DoSomeThing Finished!")
                    pass
                else:
                    print("Let's DoSomeThing")
                    val = arg._feature
                    return_args.append(ComponentArgDoSomeThing(val+1))
                # if body._memory

                
        return return_args
    # def execute
# class ThinkComponentDoSomeThing
