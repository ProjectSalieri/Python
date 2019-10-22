# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ISensor.py
# @note

class Sensor:

    def __init__(self):
        self.name = ""
        self.radius = 0.0
        self.offset = (0.0, 0.0)

        # メッセージ送信先を記憶
        self.hit_sensors = []
    # def __init__

    def init_from_setting(self, sensor_setting):
        self.name = sensor_setting.get("Name")
        self.radius = sensor_setting.get("Size").get("Radius")

        offset_setting = sensor_setting.get("Offset")
        if offset_setting != None:
            self.offset = (offset_setting.get("X"), offset_setting.get("Y"))
    # def init_from_setting

    def clear(self):
        self.hit_sensors = []
    # def clear
# class Sensor

class ISensor:

    def __init__(self):
        self.sensors = []
    # def __init__

    def init_from_setting(self, setting):
        sensor_settings = setting["Sensors"]
        for sensor_setting in sensor_settings:
            sensor = Sensor()
            sensor.init_from_setting(sensor_setting)
            self.sensors.append(sensor)
        # for sensor_settings
    # def init_from_setting

    def update(self):
        pass
    # def update

    # コンポーネント処理一周したあとの処理
    def post_update(self):
        for sensor in self.sensors:
            sensor.clear()
        # for self.sensors
    # def post_update

# class ISensor

if __name__ == "__main__":
    pass
