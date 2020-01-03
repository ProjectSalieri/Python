# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ThinkSubComponentJudgeSomeThing.py
# @note 何かを見たときに判別するコンポーネント

from ComponentArgFeatureDoSomeThing import ComponentArgFeatureDoSomeThing

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",  ".."))

from Component.IThinkComponent import IThinkComponent

class ThinkSubComponentJudgeSomeThing(IThinkComponent):
    def __init__(self):
        pass
    # def __init__

    def execute(self, args, body):
        for arg in args:
            if arg.arg_type() == ComponentArgFeatureDoSomeThing.ARG_TYPE:
                pass
            # elif arg.arg_type() == ComponentArgFeatureImage.ARG_TYPE:
            # 知らない画像だったらDesireComponentに働きかける;
        # for args
    # def execute
# class ThinkSubComponentJudgeSomeThing
