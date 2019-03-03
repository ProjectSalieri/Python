# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SampleDurabilityModule.py
# @note サンプル耐久度モジュール

from . import IDurabilityModule
import threading
import psutil # pip install psutil

class SampleDurabilityModule(IDurabilityModule.IDurabilityModule):
    def __init__(self, max_value):
        self._durability = 1000.0
        self._durability_max = max_value
        self.update_thread = threading.Thread(target=self._update_by_thread)
        self.update_thread.start()
    # def __init__

    # private

    def _getName(self):
        return "SampleDurabilityModule"
    # def _getName

    def _getDurability(self):
        return self._durability
    # def _getDurability

    def _setDurability(self, value):
        self._durability = value
    # def _setDurability

    def _update(self):
        pass
    # def _update

    def _update_by_thread(self):
        import time
        calc_interval=10
        while True:
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
            if rate < 0.01:
                self._durability += 1.0 # ほぼ何もしてない場合は回復
            else:
                self._durability -= calc_interval*len(process_cpu_per)*rate

            if self._durability > self._durability_max:
                self._durability = self._durability_max
    # def _update_by_thread

# class SampleDurabilityModule

# test code
if __name__ == '__main__':
    module = SampleDurabilityModule(1000.0)
    print("Name:\t\t" + module.getName())
    print("Durability:\t\t%f" % (module.getDurability()))
    module.setDurability(module.getDurability() - 10.0)
    print("Durability:\t\t%f" % (module.getDurability()))

    print("Update Start")
    import time
    while True:
        module.update()
        print("\rCurrent Durability:\t\t%f" % (module.getDurability()), end="")

        if module.getDurability() > 30.0:
            import math
            tmp = math.exp(math.exp(3.0))
            tmp = math.exp(math.exp(3.0))
            tmp = math.exp(math.exp(3.0))
        else:
            time.sleep(1)
            
        #time.sleep(1)
# test code
