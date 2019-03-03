# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MockAI.py
# @note AIのモック

import AIBase
import AIUtil
from SensorModule import SimpleEyeSensor
from ThinkModule import ComfortModule


from multiprocessing import Manager

from time import sleep

class MockAIBridgeModule:
    def __init__(self, stimulus_stack, action_stack):
        self.stimulus_stack = stimulus_stack
        self.action_stack = action_stack
        pass
    # def __init__

    def look_to_think(self, feature, image_file):
        self.stimulus_stack.append({"look" : {"feature" : feature, "memory" : {"image_file" : image_file, "feature" : feature}}}) # fixme : ロック
    # def look_to_think

    def try_get_stimulus(self):
        if len(self.stimulus_stack) <= 0:
            return None
        return self.stimulus_stack.pop(0) # fixme : ロック

    def is_stimulus_look(self, stimulus):
        return "look" in stimulus
    # def is_stimulus_look
    def get_look_arg(self, stimulus):
        return {"feature" : stimulus["look"]["feature"], "memory" : stimulus["look"]["memory"]}
    # def get_look_arg

    def think_to_express(self, speak_str, memory):
        # 受けた刺激情報を処理。
        self.action_stack.append({"express" : {"speak" : speak_str, "memory": memory}})
    # def think_to_express

    def try_get_action(self):
        if len(self.action_stack) <= 0:
            return None
        return self.action_stack.pop(0) # fixme : ロック
    
    def is_action_express(self, action):
        return "express" in action
    # def is_action_express
    def get_express_arg(self, action):
        return {"speak" : action["express"]["speak"], "memory" : action["express"]["memory"]}
    # def get_express_arg
# class MockAIBridgeModule

class MockAI(AIBase.AIBase):
    def __init__(self):
        # read_onlyなexecute可能
        self.eye_sensor = SimpleEyeSensor.SimpleEyeSensor(256, 256)
        # read_onlyなexecute可能
        self.comfort_module = ComfortModule.create_color_comfort_module_from_sample_param()

        # multiprocessing
        self.manager = Manager()
        self.bridge_module = MockAIBridgeModule(
            self.manager.list(), # stimulus_stack
            self.manager.list()  # action_stack
            )
    # def __init__
    
    #
    # 見る(刺激関数)
    #
    def _look_core(self, image_file):
        feature = self.eye_sensor.execute(image_file)
        self.bridge_module.look_to_think(feature, image_file)
    # def look

    #
    # 考える
    #
    def _think_core(self):
        stimulus = self.bridge_module.try_get_stimulus()
                # 何もしない FIXME : 自発的な思考
        if stimulus == None:
            #AIUtil.refresh_old_ai_image_memory() # tmpファイルリフレッシュ / HDD/SSD消耗するのでテスト実行はコメントアウト
            sleep(5) # 5秒ぼーっと
            return None
        
        if self.bridge_module.is_stimulus_look(stimulus):
            look_arg = self.bridge_module.get_look_arg(stimulus)
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
            self.bridge_module.think_to_express(speak_str, look_arg["memory"])
    # def _think_core

    #
    # 行動関数
    #
    def _action_core(self):
        action = self.bridge_module.try_get_action()
        # 何もしない
        if action == None:
            sleep(5) # 5秒ぼーっと
            return None

        if self.bridge_module.is_action_express(action):
            express_arg = self.bridge_module.get_express_arg(action)
            self._express(express_arg["speak"], express_arg["memory"])

        # elifにしない、並行実行
        if "other_action" in action:
            pass
        return None
    # def _action_core

    #
    # 表現する
    #
    def _express(self, text, tmp_memory):
        import tempfile
        from PIL import Image
        with tempfile.NamedTemporaryFile(suffix=".jpg", dir=AIUtil.ai_image_memory_path(), delete=False) as fp:
            img = AIUtil.create_paste_img_h(Image.open(tmp_memory["image_file"]),
                                        self.eye_sensor.create_feature_img(tmp_memory["feature"]))
            img.save(fp.name)
            AIUtil.tweet(text, fp.name)
    # def express

    # static関数
    def create():
        AIBase.AIBase._initialize()
        return MockAI()
# end class MockAI

# def 

if __name__ == '__main__':
    input_files = [
        ".././EyeSensor/SampleImage/Apple.jpg",
#        "./EyeSensor/SampleImage/Forest.jpg",
#        "./EyeSensor/SampleImage/Red.jpg",
    ]

    ai = MockAI.create()
    for input_file in input_files:
        ai.force_look(input_file)
    import time
    time.sleep(10)
