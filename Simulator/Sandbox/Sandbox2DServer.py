# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file Sandbox2DServer.py
# @note

import time

class Sandbox2DServer:

    def __init__(self):
        pass
    # def __init__

    def main_loop(self):
        msec_per_frame = 1000.0 / 60.0
        
        while True:
            frame_start = time.time()

#            print("main")

            frame_end = time.time()

            elapsed_time = frame_end - frame_start
            sleep_time_ms = msec_per_frame - elapsed_time*1000.0
            if sleep_time_ms > 0:
                print("sleep_time:%f[msec]" % (sleep_time_ms))
                time.sleep(sleep_time_ms/1000.0)
    # def main_loop

# class Sandbox2DServer

if __name__ == "__main__":
    server = Sandbox2DServer()
    server.main_loop()
