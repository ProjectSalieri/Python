# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file AIBase.py
# @note

import AIUtil

class AIBase:

    def __init__(self):
        pass

    # 外部刺激関係ないupdate
    def update(self):
        pass
    # def update

    def get_status(self):
        return {}
    # def get_status

    #
    # 見せる
    #
    def force_look(self, image_file):
        self._look_core(image_file)
    # def force_look

    #
    # 聴かせる
    #
    def force_listen(self, sound_file):
        self._listen_core(sound_file)
    # def force_look
    
    #
    # 見る(スレッド実行想定 overwride禁止)
    #
    def look(self):
        while True:
            image_file = None
            # 探すsearch関数みたいなの実装するか...
            self._look_core(image_file)
    # def look

    #
    # 聴く(スレッド実行想定 overwride禁止)
    #	
    def listen(self, sound_file):
        while True:
            sound_file = None
            # 探すsearch関数みたいなの実装するか
            self._listen_core(sound_file)
    # def listen

    #
    # 考える(スレッド実行想定 overwride禁止)
    #
    def think(self):
        AIUtil.refresh_old_ai_image_memory() # tmpファイルリフレッシュ
        while True:
            try:
                self._think_core()
            except:
                import sys
                print("Unexpected error at _think_core:", sys.exc_info()[0])
    # def think

    #
    # 考える(スレッド実行想定 overwride禁止)
    #
    def action(self):
        while True:
            try:
                self._action_core()
            except:
                import sys
                print("Unexpected error at action_core:", sys.exc_info()[0])
    # def action

    def _look_core(self, image_file):
        print("AIBase:_look_core")

    def _listen_core(self, sound_file):
        print("AIBase:_listen_core")

    def _think_core(self):
        print("AIBase:_think_core")

    def _action_core(self):
        print("AIBase:_action_core")

    # static関数
    def create():
        _initialize()
        return AIBase()
    # def create

    def _initialize():
        # .pycを生成しない
        import sys
        sys.dont_write_bytecode = True

        # AI初期化
        AIUtil.initialize()
        
# class AIBase
