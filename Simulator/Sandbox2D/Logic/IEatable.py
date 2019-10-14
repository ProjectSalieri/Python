# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IEatable.py
# @note

class IEatable:

    def __init__(self):
        self.is_enable_eat = False
        self.is_enable_action_eat = False
    # def __init__

    def init_from_setting(self, setting):
        if "IsEnableEat" in setting : self.is_enable_eat = setting["IsEnableEat"]
        if "IsEnableActionEat" in setting : self.is_enable_action_eat = setting["IsEnableActionEat"]
    # def __init__

    def update(self):
        pass
    # def update

# class IEatable

if __name__ == "__main__":
    pass
