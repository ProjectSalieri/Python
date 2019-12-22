# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ILife
# @note

class ILife:

    def __init__(self):
        self._is_dead = False

        self._dulability = 1000
    # def __init__

    def init_from_setting(self, setting):
        self._dulability = setting["Dulability"]
    # def init_from_setting

    def is_dead(self):
        return self._is_dead
    # is_dead

    def get_dulability(self):
        return self._dulability
    # get_dulability

    def add_life(self, value):
        self._dulability = self._dulability + value
    # def add_life

    def update(self):
        if self._is_dead == True:
            return True

        # test TODO : マテリアルと環境の組み合わせで減少
        self._dulability = self._dulability - 1

        if self._dulability < 0:
            self._is_dead = True
    # def update

    def post_update(self):
        pass
    # def post_update

# class ILife

if __name__ == "__main__":
    pass
