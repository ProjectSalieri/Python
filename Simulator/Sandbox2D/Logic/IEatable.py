# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IEatable.py
# @note

class IEatable:

    def __init__(self):
        self.is_enable_eat = False
    # def __init__

    def init_from_setting(self, setting):
        self.is_enable_eat = setting["IsEnableEat"]
    # def __init__
# class IEatable

if __name__ == "__main__":
    pass
