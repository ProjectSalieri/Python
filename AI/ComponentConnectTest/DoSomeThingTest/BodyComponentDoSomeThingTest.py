# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file BodyComponentDoSomeThingTest.py
# @note

from ComponentArgStimulusMemoryCnt import ComponentArgStimulusMemoryCnt
from SensorComponentStimulusDoSomeThing import SensorComponentStimulusDoSomeThing

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",  ".."))

from Component.IBodyComponent import IBodyComponent
from Component.ComponentArgCollection import ComponentArgCollection

class BodyComponentDoSomeThingTest(IBodyComponent):
    def __init__(self):
        self._memory = {}

        # 刺激情報スタック
        self._stimuli = ComponentArgCollection()

        # センサー処理した特徴量スタック
        self._features = ComponentArgCollection()

        # 行動情報スタック
        self._actions = ComponentArgCollection()
    # def __init__

    def is_enable(self):
        return True
    # def is_enable

    def enable(self):
        pass
    # def eable

    def disable(self):
        pass
    # def disable

    def try_stimulate(self, component_arg):
        self._stimuli.append(component_arg)
    # def stimulate

    def try_action(self, component_arg):
        self._actions.append(component_arg)
    # def try_action

    # ThinkComponentに渡す情報を
    def pop_features(self, query_arg_types):
        return self._features.pop_by_query(query_arg_types)
    # def pop_to_brain

    def pop_to_body_component(self):
        pass
    # def pop_to_body_component

    def update(self):
        args = self._stimuli.pop()

        for arg in args:
            if arg.arg_type() == ComponentArgStimulusMemoryCnt.ARG_TYPE:
                self._features.append(SensorComponentStimulusDoSomeThing.execute(arg))
        
        self._update_self()
    # def update

    def execute_action(self):
        args = self._actions.pop()
        for arg in args:
            arg.execute_class().execute(args, self)
    # def execute_action
# class BodyComponentDoSomeThingTest
