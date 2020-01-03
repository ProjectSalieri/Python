# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MetaAIProcess.py
# @note

import multiprocessing
import time
import signal

import Object
import pygame

class MetaAIProcess(multiprocessing.Process):

    def __init__(self, queue, result_queue):
        multiprocessing.Process.__init__(self)
        self._queue = queue
        self._result_queue = result_queue

        self._is_end = False
        signal.signal(signal.SIGTERM, self._signal_handler)
    # def __init__

    def run(self):
        msec_per_frame = 2000.0 # 処理しなかったときに2秒後に確認
        while self._is_end == False:
            frame_start = time.time()

            self._update_frame()

            frame_end = time.time()
            sleep_time_ms = msec_per_frame - (frame_end-frame_start)*1000.0
            if sleep_time_ms > 0:
                time.sleep(sleep_time_ms/1000.0)
    # def run

    def _update_frame(self):
        if self._queue.empty():
            return True
    # def _update_frame

    def _signal_handler(self, signum, frame):
        self._is_end = True
    # def _signal_handler

# class MetaAIProcess

