# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file AIFactory
# @note

from . import SampleEnemyAI
from . import SampleMoveAI

class AIFactory:

    def __init__(self):
        pass
    # def __init__

    def create_ai_component_from_setting(self, setting, actor):
        class_name = setting["Class"]
        parameter = {}
        if setting.get("Parameter") != None:
            parameter = setting.get("Parameter")
        
        if class_name == "PlayerControl":
            return None
        elif class_name == "SampleEnemyAI":
            return SampleEnemyAI.SampleEnemyAI(actor, parameter)
        elif class_name == "SampleMoveAI":
            return SampleMoveAI.SampleMoveAI(actor)
        else:
            assert False, "Class=%sはAIFactoryで未実装です" % class_name
    # def create_ai_component_from_setting
# class AIFactory
