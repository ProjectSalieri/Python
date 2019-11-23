# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file AIFactory
# @note

from . import SampleMove
from . import SamplePlayerChase

class AIFactory:

    def __init__(self):
        pass
    # def __init__

    def create_ai_component_from_setting(self, setting, actor):
        class_name = setting["Class"]
        if class_name == "SamplePlayerChase":
            return SamplePlayerChase.SamplePlayerChase(actor)
        elif class_name == "SampleMove":
            return SampleMove.SampleMove(actor)
        else:
            assert False, "Class=%sはAIFactoryで未実装です" % class_name
    # def create_ai_component_from_setting
# class AIFactory
