# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SenseKeeper.py
# @note

from . import EyeSensor

class SenseKeeper:

    def __init__(self):
        self.eye_sensor = None
    # def __init__

    def init_from_setting(self, sense_settings):
        if sense_settings.get("Eye") != None:
            self.eye_sensor = EyeSensor.EyeSensor()
            self.eye_sensor.init_from_setting(sense_settings.get("Eye"))
    # def init_from_setting

    def try_get_eye_sensor(self):
        return self.eye_sensor
    # def try_get_eye_sensor

    def update(self):
        # 時間が経つと匂いがわからなくなるとか?
        # 目をつぶるとか？
        pass
    # def update

    def post_update(self):
        if self.eye_sensor != None:
            self.eye_sensor.clear()
    # def post_update
# class SenseKeeper

if __name__ == "__main__":
    pass
