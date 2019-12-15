# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file Salieri.py
# @note

import threading

from .SalieriVirtualScene import SalieriVirtualScene

from Logic.Input import PlayerController

# Debug
from .SalieriDebugger import SalieriDebugger

class Salieri:

    def __init__(self):
        self._stop_event = threading.Event()
        self._update_thread = threading.Thread(target=self.update)
        self._virtual_scene = SalieriVirtualScene()

        self._keys = []
        self._actor = None

        self._debugger = SalieriDebugger(self._virtual_scene)

        self._stop_event.clear()
        self._update_thread.start()
    # def __init__

    def set_control_actor(self, actor):
        self._actor = actor
    # set_control_actor

    def update(self):
        import time
        msec_per_frame = 1000.0 / 120.0
        while self._stop_event.is_set() == False:
            frame_start = time.time()

            self._update_frame()

            frame_end = time.time()
            sleep_time_ms = msec_per_frame - (frame_end-frame_start)*1000.0
            if sleep_time_ms > 0:
                time.sleep(sleep_time_ms/1000.0)
    # def update

    def send_network_inputs(self):
        # Salieriの更新によるclearとタイミングあってない
        return self._keys
    # def send_network_inputs

    def shutdown(self):
        self._stop_event.set()
        self._update_thread.join(0.1)

        self._debugger.shutdown()
    # def shutdown

    def _update_frame(self):
        self._keys.clear()
        
        self._virtual_scene.update()

        eye_sense_objects = []
        if self._actor != None:
            eye_sense_objects = self._actor.get_object_component("Sense").try_get_eye_sensor().sense_objects
        if len(eye_sense_objects) > 0:
            eye_sense_object = eye_sense_objects[0]
            diff = eye_sense_object.get_pos() - self._actor.get_pos()
            if diff[0] > 0.0:
                self._keys.append(PlayerController.PlayerController.KEY_RIGHT)
            elif diff[0] < 0.0:
                self._keys.append(PlayerController.PlayerController.KEY_LEFT)

            if diff[2] < 0.0:
                self._keys.append(PlayerController.PlayerController.KEY_UP)
            elif diff[2] > 0.0:
                self._keys.append(PlayerController.PlayerController.KEY_DOWN)                

        # デバッグ用
    # def _update_frame

# class Salieri

if __name__ == "__main__":
    pass
