# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file BodyComponentPCVirtual.py
# @note PC情報をBodyとして扱う

import threading

from IBodyComponent import IBodyComponent
from IDurabilityComponent import IDurabilityComponent
from ComponentArgCollection import ComponentArgCollection
from ComponentArgStimulusLook import ComponentArgStimulusLook

from ActionComponentLookWebPage import ActionComponentLookWebPage

import psutil # pip install psutil
# PC情報から仮想のCpuDurabilityを設定
class DurabilityComponentCpuVitual(IDurabilityComponent):
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

# 標準的なPC情報を使った仮想ボディ
class BodyComponentPCVirtual(IBodyComponent):
    def __init__(self):
        # TODO : 他のdurabilityも平行で
        self._virtual_durability = DurabilityComponentCpuVitual(2000.0)
        
        # 刺激情報スタック
        self._stimuli = ComponentArgCollection()

        # センサー処理した特徴量スタック
        self._features = ComponentArgCollection()

        # 条件反射行動
        self._self_update_features = ComponentArgCollection()
        self._actions = ComponentArgCollection()

        # ActionComponents
        self._action_components = [
            ActionComponentLookWebPage(self),
            ]

        self._stop_event = threading.Event()
        self._update_thread = threading.Thread(target=self._update_by_thread)

        # 初期状態は停止
        self._stop_event.set() # NOTE : threadの状態を直接取得できないので、diable関数のためにフラグを合わせておく
        self.disable()
    # def __init__

    def is_enable(self):
        return self._stop_event.is_set() == False
    # def is_enable

    def enable(self):
        if self.is_enable():
            return True
        self._stop_event.clear() # NOTE : スレッド回す前に設定すること
        self._update_thread.start()
        return True
    # def enable

    def disable(self):
        if self.is_enable():
            self._stop_event.set()
            self._update_thread.join(0.1)
        return True
    # def disable

    def try_stimulate(self, component_arg):
        # FIXME : 上限儲けたほうがいいかも
        self._stimuli.append(component_arg)
    # def stimulate

    def pop_features(query_arg_types):
        return self._features.pop_by_query(query_arg_types)
    # def pop_to_brain

    def pop_to_body_component(self):
        pass
    # def pop_to_body_component

    def update(self):
        pass
    # def update

    def execute_action(self):
        args = self._actions.pop()
        
        for action in self._action_components:
            action.execute(args)
    # def execute_action
    
    # private

    def _update_self(self):
        if self._self_update_features.is_exist():
            # 条件反射(BodyComponentがBodyComponentを操作)を実装するならここで
            # self._action_stack.append(ComponentArgAction~)
            pass

    def _update_by_thread(self):
        while self.is_enable():
            # Durabilityのupdate
            self._virtual_durability.update()

            # センサー類のupdate
            # TODO : 刺激の種類に応じて並列処理してもいいかも ex)ハードで処理するケースとか
            if self._stimuli.is_exist():
                self._try_process_look()
                
            self._update_self()
    # def _update_thread

    def _try_process_look(self):
        stimuli_look  = self._stimuli.pop_by_query(ComponentArgStimulusLook.ARG_TYPE)
        if len(stimuli_look) > 0:
            # なにがしかのセンサー処理を行って ComponentArgFeatureImage(画像特徴量 直接視覚じゃなくても使えるように) のようなクラスを返す
            # self._feature_stack.append(ComponentArgFeatureImage)
            # self._self_update_feature_stack.append(ComponentArgFeatureImage)
            pass        
    # def _try_process_look
# class BodyComponentPCVirtual

# test code
if __name__ == '__main__':
    body = BodyComponentPCVirtual()

    assert body.is_enable() == False, "IBodyComponentの初期値はdisableです"

    print("=====DebugPrint=====")
    print("%s\ndurability:%f" % (body._virtual_durability.getName(), body._virtual_durability.getDurability()))

    init_durability = body._virtual_durability.getDurability()
    body._virtual_durability.setDurability(init_durability - 5.0)
    assert body._virtual_durability.getDurability() == init_durability - 5.0, "getDurability() / setDurability()のテスト失敗"
    
    print("=====enable=====")
    body.enable()

    def print_current_durability(body_comp):
        cur_durability = body_comp._virtual_durability.getDurability()
        print("\rCurrent Durability:\t\t%f" % (cur_durability), end="")
        return cur_durability

    import time
    while True:
        body.update()
        cur_durability = print_current_durability(body)

        if cur_durability > init_durability - 15.0 :
            import math
            for i in range(10000):
                tmp = math.exp(math.exp(3.0))
            print(" --> active", end="")
        else:
            print(" --> rest 5sec\n", end="")
            time.sleep(5)
            break

    print("=====disable=====")
    body.disable()
    print_current_durability(body)
# test code
