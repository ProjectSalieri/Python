# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ILife
# @note

class ILife:

    def __init__(self):
        self._is_dead = False

        self.cnt = 0
    # def __init__

    def init_from_setting(self, setting):
        pass
    # def init_from_setting

    def is_dead(self):
        return self._is_dead
    # is_dead

    def update(self):
        if self._is_dead == True:
            return True

        # test
        self.cnt = self.cnt + 1
        if self.cnt > 1000:
            self._is_dead = True
    # def update

    def post_update(self):
        pass
    # def post_update

# class ILife

if __name__ == "__main__":
    pass
