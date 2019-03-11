# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file DurabilityComponentPCVirtual.py
# @note PC情報から仮想のCpuDurabilityを設定

import psutil # pip install psutil

from IDurabilityComponent import IDurabilityComponent


# PC情報から仮想のCpuDurabilityを設定
class DurabilityComponentCpuVirtual(IDurabilityComponent):
    def __init__(self, max_value):
        self._durability = max_value
        self._durability_max = max_value
    # def __init__
    # private

    def _getName(self):
        return "DurabilityComponentCpuVitual"
    # def _getName

    def _getDurability(self):
        return self._durability
    # def _getDurability

    def _setDurability(self, value):
        self._durability = value
    # def _setDurability

    def _update(self):
        calc_interval=10
        
        # 全体CPU
        cpu_per = psutil.cpu_percent(interval=calc_interval)
        # Python関連のCPU
        process = filter(lambda p: p.name() == "Python", psutil.process_iter())
        process_cpu_per = []
        for i in process:
            process_cpu_per.append(i.cpu_percent(interval=calc_interval))
        sum = 0.0
        for per in process_cpu_per:
            sum += per

        rate = sum/100.0 # 100%に近いほど減る
        if rate < 0.15:
            self._durability += calc_interval*len(process_cpu_per)*(1.0-rate) # ほぼ何もしてない場合は回復
        else:
            self._durability -= calc_interval*len(process_cpu_per)*rate

        if self._durability > self._durability_max:
            self._durability = self._durability_max
    # _update

# class DurabilityComponentCpuVitual
