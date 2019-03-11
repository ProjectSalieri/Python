# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SalieriStateActionSatisfyHungryVirtual.py
# @note 仮想空腹を満たすテスト用アクションステート

import SalieriImporter

from ISalieriStateAction import ISalieriStateAction

# TODO : sin -> sin位相違いと変わっていく課題を学習、エラー率が低くなったらパラメータを渡してBodyComponent経由でHungryVirtualを回復してもらう
class SalieriStateActionSatisfyHungryVirtual(ISalieriStateAction):
    def __init__(self):
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
# class SalieriStateActionSatisfyHungryVirtual

# test code
if __name__ == "__main__":
    pass
