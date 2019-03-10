# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file DesireComponentKnowledge.py
# @note 知識欲求を扱うコンポーネント

from IDesireComponent import IDesireComponent

class DesireComponentKnowledge(IDesireComponent):

    def __init__(self):
        self._desire_value = 0.0
    # def __init__

    # private
    def _get_name(self):
        return "DesireComponentKnowledge"
    # def _get_name

    def _get_value(self):
        return self.desire_value
    # def __get_value

    def _set_value(self, value):
        self.desire_value = value
    # def _set_value
    
# clss DesireComponentKnowledge

if __name__ == "__main__":
    desire = DesireComponentKnowledge()

    print("DesireName:" + desire.get_name())
    desire.set_value(10.0)
    print("DesireValue:" + str(desire.get_value()))
