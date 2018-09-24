# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MockAI.py
# @note AIのモック

from SensorModule import SimpleEyeSensor
from ThinkModule import ComfortModule

class MockAI:
    def __init__(self):
        self.eye_sensor = SimpleEyeSensor.SimpleEyeSensor(256, 256)

        self.comfort_module = ComfortModule.create_color_comfort_module_from_sample_param()
        pass
    # def __init__
    
    #
    # 見る
    #
    def look(self, image_file):
        feature = self.eye_sensor.execute(image_file)

        comfort_ret = self.comfort_module.predict(ComfortModule.rgb_array_to_raw_data_array([feature[0:3]]))[0]
        comfort_response_str = ""
        if self.comfort_module.is_comfort(comfort_ret):
            comfort_response_str = "快"
        elif self.comfort_module.is_uncomfort(comfort_ret):
            comfort_response_str = "不快"
        else:
            comfort_response_str = "普通"

        speak_str = "この画像" + str(comfort_response_str)
        print(speak_str)

        import subprocess, os, tempfile
        from PIL import Image
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=True) as fp:
            img = AIUtil.create_paste_img_h(Image.open(image_file),
                                      self.eye_sensor.create_feature_img(feature))
            img.save(fp.name)
            cmd_arr = [
                "ruby",
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "ExpressModule", "TwitterAccessor.rb"),
                "--post_text",
                speak_str,
                "--image_path",
                fp.name
            ]
            # subprocess.call(cmd_arr)
        pass
    # def look
    
    #
    # 聴く
    #	
    def listen(self, sound_file):
    	pass
    # def listen
    
    #
    # 表現する
    #
    def express(self, text, image_file):
    	pass
    # def express
# end class MockAI

if __name__ == '__main__':
    # .pycを生成しない
    import sys
    sys.dont_write_bytecode = True

    # AI初期化
    import AIUtil
    AIUtil.initialize()

    input_files = [
        "./EyeSensor/SampleImage/Apple.jpg",
        "./EyeSensor/SampleImage/Forest.jpg",
#        "./EyeSensor/SampleImage/Red.jpg",
    ]

    ai = MockAI()
    for input_file in input_files:
        ai.look(input_file)
