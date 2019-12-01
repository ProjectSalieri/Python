# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file Salieri.py
# @note

import threading

from .SalieriVirtualScene import SalieriVirtualScene

class Salieri:

    def __init__(self):
        self._stop_event = threading.Event()
        self._update_thread = threading.Thread(target=self.update)
        self._virtual_scene = SalieriVirtualScene()

        self._stop_event.clear()
        self._update_thread.start()
    # def __init__

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
        from Logic.Input import PlayerController

        return [PlayerController.PlayerController.KEY_DOWN]
    # def send_network_inputs

    def shutdown(self):
        self._stop_event.set()
        self._update_thread.join(0.1)
    # def shutdown

    def _update_frame(self):
        self._virtual_scene.update()
    # def _update_frame

# class Salieri

if __name__ == "__main__":
    pass
