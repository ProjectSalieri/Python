# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MetaAILogger.py
# @note

from threading import Lock

from Logic.System.MetaAI.MetaAIProcess import MetaAIProcess
from Logic.System.Logger.PlayLogger import PlayLogger

class MetaAILogger:

    def __init__(self):
        self._buffers = [ [], [] ]
        self._current_buf_idx = 0 # ダブルバッファ

        self._lock = Lock()
    # def __init__

    def put(self, play_log):
        if self._lock.acquire():
            self._buffers[self._current_buf_idx].append(play_log)
            self._lock.release()
    # def put

    # MetaAIProcess用のqueueへflush
    def flush(self, queue):
        flush_buf_idx = -1
        # Bufferのindex入れ替え
        if self._lock.acquire():
            flush_buf_idx = self._current_buf_idx
            self._current_buf_idx += 1
            if self._current_buf_idx >= len(self._buffers):
                self._current_buf_idx = 0
            self._lock.release()

        # flush
        for log in self._buffers[flush_buf_idx]:
            queue.put(log)
        queue.put(MetaAIProcess.PROCESS_MSG_QUEUE_END) # queueを共有しているのでemptyだと正確なemptyがわからない

        self._buffers[flush_buf_idx].clear()
    # def flush

        

# class MetaAILogger

if __name__ == "__main__":
    pass
