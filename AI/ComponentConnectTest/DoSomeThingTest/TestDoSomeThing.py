# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file DoSomeThingTest.py
# @note

from BodyComponentDoSomeThingTest import BodyComponentDoSomeThingTest
from ComponentArgFeatureDoSomeThing import ComponentArgFeatureDoSomeThing
from ComponentArgStimulusMemoryCnt import ComponentArgStimulusMemoryCnt
from ThinkComponentDoSomeThing import ThinkComponentDoSomeThing

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",  ".."))



if __name__ == "__main__":
    body = BodyComponentDoSomeThingTest()
    body.try_stimulate(ComponentArgStimulusMemoryCnt())
    think_component = ThinkComponentDoSomeThing()

    for i in range(10):
        body.update()
        features =  body.pop_features([ComponentArgFeatureDoSomeThing.ARG_TYPE])
        actions = think_component.execute(features, body)
        for action in actions:
            body.try_action(action)

        body.execute_action()
