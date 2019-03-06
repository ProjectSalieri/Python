# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IDurabilityComponent.py
# @note 耐久度モジュール

class IDurabilityComponent():
    def __init__(self):
        pass
    # def __init__

    #
    # 名前
    #
    def getName(self):
        return self._getName()
    # def getName

    #
    # 耐久度を取得
    #
    def getDurability(self):
        return self._getDurability()
    # def getDurability

    #
    # 耐久度を設定
    #
    def setDurability(self, value):
        self._setDurability(value)
    # def setDuralibity

    #
    # 毎フレーム処理(耐久度の自然減少など)
    #
    def update(self):
        self._update()
    # def update

    # private method

    def _getName(self):
        return "IDurabilityComponent"
    # def _getName

    def _getDurability(self):
        pass
    # def getDurability

    def _setDurability(self, value):
        pass
    # def _setDurability

    def _update(self):
        pass
    # def _update

# class IDurabilityModule

# test code
if __name__ == '__main__':
    module = IDurabilityComponent()
# test code
