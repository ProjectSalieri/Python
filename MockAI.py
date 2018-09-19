# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MockAI.py
# @note AIのモック

from SensorModule import SimpleEyeSensor

class MockAI:
    def __init__(self):
        self.eye_sensor = SimpleEyeSensor.SimpleEyeSensor(256, 256)
        pass
    # def __init__
    
    #
    # 見る
    #
    def look(self, image_file):
        feature = self.eye_sensor.execute(image_file)

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
                "テスト投稿",
                "--image_path",
                fp.name
            ]
            subprocess.call(cmd_arr)
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

    input_file = "./EyeSensor/SampleImage/Apple.jpg"

    ai = MockAI()
    ai.look(input_file)
