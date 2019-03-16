# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ThinkSubComponentRestTest.py
# @note 休息系Component

from ComponentArgRest import ComponentArgRest

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",  ".."))

from Component.IThinkComponent import IThinkComponent

class ThinkSubComponentRestTest(IThinkComponent):
    def __init__(self):
        pass
    # def __init__

    def execute(self, args, body):
        # bodyを見て休憩する想定
        import random
        r = (int)(random.random()*10)
        if r < 1:
            return [ComponentArgRest()]
        else:
            return []
            
    # def execute
# class ThinkSubComponentRestTest
