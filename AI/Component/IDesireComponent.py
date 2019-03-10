# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IDesireComponent.py
# @note 欲求を扱うコンポーネント

from IArgExecuteModule import IArgExecuteModule

class IDesireComponent:
    def __init__(self):
        pass
    # def __init__

    def get_name(self):
        return self._get_name()
    # def get_name

    # 度合い
    def get_value(self):
        return self._get_value()
    # def get_value

    def set_value(self, value):
        return self._set_value(value)
    # def set_value

    # private
    
    def _get_name(self):
        return "IDesireComponent"
    # def _get_name

    def _get_value(self):
        return 0.0
    # def _get_value

    def _set_value(self, value):
        pass
    # def _set_value
    
# class IDesireComponent

if __name__ == '__main__':
    pass
