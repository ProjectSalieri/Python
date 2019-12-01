# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file Sense.py
# @note

class OdorSensor:

    def __init__(self):
        self._send_actors = []
    # def __init__

    def receive_msg(msg, send_actor):
        if msg == "":
            self._send_actors.append(send_actor)
            return True
        
        return False
    # def receive_msg

    def post_update(self):
        self._send_actors = []
# class OdorSensor

class Sense:

    def __init__(self):
        self.sense_components = {}
    # def __init__

    def init_from_setting(self, sense_settings):
        for sense_setting in sense_settings:
            type = sense_setting.get("Type")
            if type == "Odor":
                self.sense_components[type] = OdorSensor()
    # def init_from_setting

    def get_send_actors_pos(self, type):
        sense_component = self.sense_components.get(type)
        if sense_component == None:
            return []
        pos_arr = []
        for send_actor in sense_component._send_actors:
            pos_arr.append(send_actor.get_object_component("Physics").pos)
        return pos_arr
    # get_send_actors_pos

    def receive_msg(msg, send_actor):
        for sense_component in self.sense_components:
            if sense_component.receive_msg(msg, send_actor) == True:
                return True

        return False
    # def receive_msg

    def update(self):
        # 時間が経つと匂いがわからなくなるとか?
        # 目をつぶるとか？
        pass
    # def update

    def post_update(self):
        for sense_component in self.sense_components:
            sense_component.post_update()
    # def post_update
# class Sense

if __name__ == "__main__":
    pass
