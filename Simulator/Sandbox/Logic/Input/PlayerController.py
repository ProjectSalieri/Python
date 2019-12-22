# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file PlayerController.py
# @note ネットワーク操作/AI操作/ユーザー操作を束ねるクラス

class PlayerController:

    KEY_UP = 1
    KEY_RIGHT = 2
    KEY_DOWN = 3
    KEY_LEFT = 4
    KEY_A = 5
    KEY_U = 25

    def __init__(self):
        self.inputs = []
    # def __init__

    def clear(self):
        self.inputs = []
    # def __clear__

    def input(self, key):
        if (key in self.inputs) == False:
            self.inputs.append(key)
    # def input

    
# class PlayerController

if __name__ == "__main__":
    pass
