# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MockAIActionComponent.py
# @note AIのモック

import AIUtil

from Component import ComponentArgExpress

# いつか消すかも
from SensorModule import SimpleEyeSensor

class MockAIActionComponent:
    def __init__(self):
        pass
    # def __init__

    def reload(self):
        import importlib
        tmp = importlib.reload(importlib.import_module(".", "MockAIActionComponent"))
        new_inst = tmp.MockAIActionComponent()
        return new_inst
    # def reload

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
