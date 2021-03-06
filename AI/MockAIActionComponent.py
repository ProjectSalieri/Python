# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MockAIActionComponent.py
# @note AIのモック

import time

import AIUtil

from Component import ActionComponentLookWebPage
from Component import ComponentArgExpress

# いつか消すかも
from SensorModule import SimpleEyeSensor

class MockAIActionComponent:
    def __init__(self, virtual_body):
        self.start_t = time.time()

        self._virtual_body = virtual_body
        
        self._action_look_web_page = ActionComponentLookWebPage.ActionComponentLookWebPage(virtual_body)
        pass
    # def __init__

    def reload(self):
        # FIXME : self.start_tがreloadと利用で初期化と参照が発生するので注意
        import importlib
        tmp = importlib.reload(importlib.import_module(".", "MockAIActionComponent"))
        new_inst = tmp.MockAIActionComponent(self._virtual_body)
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

    def execute(self, args):
        for arg in args:
            if arg.arg_type() == ComponentArgLookWebPage.ARG_TYPE:
                self._action_look_web_page.execute(ComponentArgLookWebPage())
            if arg.arg_type() == ComponentArgLookWebPage.ARG_TYPE:
                self.express(arg)
        pass
    # def execute

    def express(self, express_arg):
        import tempfile
        from PIL import Image
        tmp_memory = express_arg.memory
        with tempfile.NamedTemporaryFile(suffix=".jpg", dir=AIUtil.ai_image_memory_path(), delete=False) as fp:
            img = AIUtil.create_paste_img_h(Image.open(tmp_memory["image_file"]),
                                        SimpleEyeSensor.SimpleEyeSensor.create_feature_img(tmp_memory["feature"]))
            img.save(fp.name)
            AIUtil.tweet(express_arg.speak_str, fp.name)
    # def express
# class MockAIThinkComponent
