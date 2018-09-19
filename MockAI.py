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

    input_file = "./EyeSensor/SampleImage/Chris.jpg"

    ai = MockAI()
    ai.look(input_file)
