# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file EyeSensor
# @note

class EyeSensor:

    def __init__(self):
        self.sense_objects = []
    # def __init__

    def init_from_setting(self, eye_settings):
        pass
    # def init_from_setting

    def clear(self):
        self.sense_objects.clear()
    # def clear

    def calc_enable_sense(self, dist):
        # TODO : 視認距離のパラメータ化
        return True
    # def calc_enable_sense

    def add_sense_object(self, _object):
        self.sense_objects.append(_object)
    # add_sense_object

# class SenseKeeper

if __name__ == "__main__":
    pass
