# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MockAI.py
# @note AIのモック

class MockAI:
    def __init__(self):
        pass
    # def __init__
    
    #
    # 見る
    #
    def look(self, image_file):
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

    input_file = "./SampleImage/Chris.jpg"

    ai = MockAI()
