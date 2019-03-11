# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ISalieriStateAction.py
# @note Action系のハードコーディングステートのインターフェース

class ISalieriStateAction:
    def __init__(self):
        pass
    # def

    # ThinkComponentが次のStateActionの実行を開始していいかの判定関数
    def is_finish(self):
        return true # FIXME : 実装
    # def is_satisfied

    # ThinkComponentからの開始命令
    def start(self):
        pass
    # def start

    # ThinkComponentからの強制停止命令
    def stop(self):
        pass
    # def stop
# class SalieriStateActionGoogle
