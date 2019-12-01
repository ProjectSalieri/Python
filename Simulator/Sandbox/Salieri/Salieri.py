# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file Salieri.py
# @note

import threading

class Salieri:

    def __init__(self):
        self._stop_event = threading.Event()
        self._update_thread = threading.Thread(target=self.update)

        self._stop_event.clear()
        self._update_thread.start()
    # def __init__

    def update(self):
        while self._stop_event.is_set() == False:
            pass
    # def update

    def send_network_inputs(self):
        from Logic.Input import PlayerController
        
        return [PlayerController.PlayerController.KEY_DOWN]

    def shutdown(self):
        self._stop_event.set()
        self._update_thread.join(0.1)
    # def shutdown

# class Salieri

if __name__ == "__main__":
    pass
