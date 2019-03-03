# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MockAIThinkComponent.py
# @note AIのモック

import time

from ThinkModule import ComfortModule
from Component import ComponentArgExpress

class MockAIThinkComponent:
    def __init__(self):
        self.comfort_module = ComfortModule.create_color_comfort_module_from_sample_param()
        self.start_t = time.time()
        pass
    # def __init__

    def reload(self):
        # FIXME : self.start_tがreloadと利用で初期化と参照が発生するので注意
        import importlib
        tmp = importlib.reload(importlib.import_module(".", "MockAIThinkComponent"))
        new_inst = tmp.MockAIThinkComponent()
        return new_inst
    # def reload

    def start(self):
        self.start_t = time.time()
    # def start

    def try_sleep(self):
        end_t = time.time()
        time_diff = end_t - self.start_t
        if time_diff < 5.0:
            time.sleep(5.0 - time_diff)
    # def try_sleep

    def comfort(self, look_arg):        
        feature = look_arg["feature"]
        comfort_ret = self.comfort_module.predict(ComfortModule.rgb_array_to_raw_data_array([feature[0:3]]))[0]
        comfort_response_str = ""
        if self.comfort_module.is_comfort(comfort_ret):
            comfort_response_str = "快"
        elif self.comfort_module.is_uncomfort(comfort_ret):
            comfort_response_str = "不快"
        else:
            comfort_response_str = "普通"

        speak_str = "この画像" + str(comfort_response_str)

        express_arg = ComponentArgExpress.ComponentArgExpress()
        express_arg.speak_str = speak_str
        express_arg.memory = look_arg["memory"]
        return express_arg
# class MockAIThinkComponent
