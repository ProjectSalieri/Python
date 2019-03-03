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

class MockAI(AIBase.AIBase):
    def __init__(self):
        # read_onlyなexecute可能
        self.eye_sensor = SimpleEyeSensor.SimpleEyeSensor(256, 256)
        # read_onlyなexecute可能
        self.comfort_module = ComfortModule.create_color_comfort_module_from_sample_param()

        # multiprocessing
        self.manager = Manager()
        self.stimulus_stack = self.manager.list()
        self.action_stack = self.manager.list()
        # multiprocessing デバッグ用に近い
        self.tmp_memory_look = self.manager.list()
    # def __init__
    
    #
    # 見る(刺激関数)
    #
    def _look_core(self, image_file):
        # 刺激情報をスタック
        feature = self.eye_sensor.execute(image_file)
        self.stimulus_stack.append({"look" : feature}) # fixme : ロック
        self.tmp_memory_look.append({"image_file" : image_file, "feature" : feature})
        print("[look]" + "self=" + hex(id(self)) + " stimulus_stack(" + str(len(self.stimulus_stack)) + ")=" + hex(id(self.stimulus_stack)))
    # def look

    #
    # 考える
    #
    def _think_core(self):
        # 何もしない
        if len(self.stimulus_stack) <= 0:
            print("[think]" + "(None)" + "self=" + hex(id(self)) + " stimulus_stack(" + str(len(self.stimulus_stack))+ ")=" + hex(id(self.stimulus_stack)))
            #AIUtil.refresh_old_ai_image_memory() # tmpファイルリフレッシュ / HDD/SSD消耗するのでテスト実行はコメントアウト
            sleep(5) # 5秒ぼーっと
            return None
        print("[think]" + "(think)" + "self=" + hex(id(self)))

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
            print("[action]" + "(None)" + "self=" + hex(id(self)))
            sleep(5) # 5秒ぼーっと
            return None
        print("[action]" + "(action)" + "self=" + hex(id(self)))

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
        "./EyeSensor/SampleImage/Apple.jpg",
        "./EyeSensor/SampleImage/Forest.jpg",
#        "./EyeSensor/SampleImage/Red.jpg",
    ]

    ai = MockAI.create()
    for input_file in input_files:
        ai.force_look(input_file)