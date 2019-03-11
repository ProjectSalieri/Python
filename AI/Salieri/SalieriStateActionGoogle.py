# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SalieriStateActionGoogle.py
# @note Googleで何か検索して、達成 or 諦めるまでをハードコーディングしたステート(Actionパート)

import SalieriImporter

from Component.ActionComponentLookWebPage import ActionComponentLookWebPage

class SalieriStateActionGoogle:
    def __init__(self):
        self._action_look_web_page = ActionComponentLookWebPage()
        pass
    # def

    def is_finish(self):
        return true # FIXME : 実装
    # def is_satisfied

    # ThinkComponentからの開始命令
    def start(self):
        pass
    # def start

    # ThinkComponentからの停止命令
    def stop(self):
        pass
    # def stop
# class SalieriStateActionGoogle

# test code
if __name__ == "__main__":
    pass
