# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MockAI.py
# @note AIのモック

from SensorModule import SimpleEyeSensor
from ThinkModule import ComfortModule

from time import sleep

import AIUtil

class MockAI:
    def __init__(self):
        self.eye_sensor = SimpleEyeSensor.SimpleEyeSensor(256, 256)

        self.comfort_module = ComfortModule.create_color_comfort_module_from_sample_param()

        self.stimulus_stack = []
        self.action_stack = []

        # デバッグ用に近い
        self.tmp_memory_look = []
        pass
    # def __init__
    
    #
    # 見る(刺激関数)
    #
    def look(self, image_file):
        # 刺激情報をスタック
        feature = self.eye_sensor.execute(image_file)
        self.stimulus_stack.append({"look" : feature}) # fixme : ロック
        self.tmp_memory_look.append({"image_file" : image_file, "feature" : feature})
    # def look
    
    #
    # 聴く(刺激関数)
    #	
    def listen(self, sound_file):
    	pass
    # def listen

    #
    # 考える(スレッド実行想定)
    #
    def think(self):
        while True:
            self._think_core()
    # def think

    #
    # 考える(スレッド実行想定)
    #
    def action(self):
        while True:
            self._action_core()
    # def think

    #
    # 考える
    #
    def _think_core(self):
        # 何もしない
        if len(self.stimulus_stack) <= 0:
            sleep(5) # 5秒ぼーっと
            return None

        # 受けた刺激情報を処理。
        stimulus = self.stimulus_stack.pop(0) # fixme : ロック
        if "look" in stimulus:
            feature = stimulus["look"]
            comfort_ret = self.comfort_module.predict(ComfortModule.rgb_array_to_raw_data_array([feature[0:3]]))[0]
            comfort_response_str = ""
            if self.comfort_module.is_comfort(comfort_ret):
                comfort_response_str = "快"
            elif self.comfort_module.is_uncomfort(comfort_ret):
                comfort_response_str = "不快"
            else:
                comfort_response_str = "普通"

            speak_str = "この画像" + str(comfort_response_str)
            self.action_stack.append({"express" : speak_str})
        pass
    # def _think_core

    #
    # 行動関数
    #
    def _action_core(self):
        # 何もしない
        if len(self.action_stack) <= 0:
            sleep(5) # 5秒ぼーっと
            return None

        action = self.action_stack.pop(0) # fixme : ロック
        if "express" in action:
            self._express(action["express"], self.tmp_memory_look.pop(0))

        # elifにしない、並行実行
        if "other_action" in action:
            pass
        return None
    # def _action_core

    #
    # 表現する
    #
    def _express(self, text, tmp_memory):
        import subprocess, os, tempfile
        from PIL import Image
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=True) as fp:
            img = AIUtil.create_paste_img_h(Image.open(tmp_memory["image_file"]),
                                        self.eye_sensor.create_feature_img(tmp_memory["feature"]))
            img.save(fp.name)
            cmd_arr = [
                "ruby",
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "ExpressModule", "TwitterAccessor.rb"),
                "--post_text",
                text,
                "--image_path",
                fp.name
            ]
            subprocess.call(cmd_arr)
    # def express

    # static関数
    def create_mock_ai():
        # .pycを生成しない
        import sys
        sys.dont_write_bytecode = True

        # AI初期化
        import AIUtil
        AIUtil.initialize()

        return MockAI()
# end class MockAI

# def 

if __name__ == '__main__':
    input_files = [
        "./EyeSensor/SampleImage/Apple.jpg",
        "./EyeSensor/SampleImage/Forest.jpg",
#        "./EyeSensor/SampleImage/Red.jpg",
    ]

    ai = MockAI.create_mock_ai()
    for input_file in input_files:
        ai.look(input_file)
