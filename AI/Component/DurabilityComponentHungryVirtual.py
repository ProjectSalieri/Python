# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file DurabilityComponentPCVirtual.py
# @note テスト用の仮想空腹度

import time

from IDurabilityComponent import IDurabilityComponent

# TODO : BodyComponentPCVirtualに組み込む
#      : sin -> cos -> sin位相違いと問題が変わるものを定期的い解く
#      :  => 正解率が一定を超えたら達成とみなしてBodyComponentにパラメータ渡してupdateで回復してもらう
class DurabilityComponentHungryVirtual(IDurabilityComponent):
    def __init__(self):
        self._durability = 100.0
        self._prev_time = time.time()
    # def __init__

    def _getName(self):
        return "DurabilityComponentHungryVirtual"
    # def _getName

    def _getDurability(self):
        return self._durability
    # def _getDurability

    def _setDurability(self, value):
        self._durability = value
    # def _setDurability

    DEC_PER_60SEC = 2.0 / 60.0
    def _update(self):
        cur_time = time.time()
        # 1時間に2%ずつ減っていく => 60秒に2.0/60.0ずつ減っていく => 30秒に
        if cur_time - self._prev_time > 60:
            cycle = (int)((cur_time - self._prev_time) / 60.0)
            self._durability -= DurabilityComponentHungryVirtual.DEC_PER_60SEC*cycle
            self._prev_time = self._prev_time + 60.0*cycle # 処理落ちするかもしれないので、確実に経過したであろうところまで追加
    # def _update
    
# class DurabilityComponentHungryVirtual

if __name__ == "__main__":
    hungry = DurabilityComponentHungryVirtual()
    start_t = time.time()
    while time.time() - start_t < 70:
        hungry.update()
        print(hungry.getDurability())
        time.sleep(5)
