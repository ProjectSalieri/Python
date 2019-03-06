# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file MockAI.py
# @note AIのモック

import AIBase
import AIUtil

import MockAIActionComponent
import MockAIThinkComponent

from Component import SampleDurabilityComponent
from SensorModule import SimpleEyeSensor
from Component import IComponentArg
from Component import ComponentArgDurability
from Component import ComponentArgExpress


from multiprocessing import Manager

from time import sleep

class MockAIBridgeModule:
    def __init__(self, stimulus_stack, action_stack):
        self.stimulus_stack = stimulus_stack
        self.action_stack = action_stack
        pass
    # def __init__

    def reload(self):
        import importlib
        tmp = importlib.reload(importlib.import_module(".", "MockAI"))
        new_inst = tmp.MockAIBridgeModule(self.stimulus_stack, self.action_stack)
        return new_inst
    #def reload

    def look_to_think(self, feature, image_file):
        self.stimulus_stack.append({"look" : {"feature" : feature, "memory" : {"image_file" : image_file, "feature" : feature}}}) # fixme : ロック
    # def look_to_think

    def try_get_stimulus(self):
        if len(self.stimulus_stack) <= 0:
            return None
        return self.stimulus_stack.pop(0) # fixme : ロック

    def is_stimulus_look(self, stimulus):
        return "look" in stimulus
    # def is_stimulus_look
    def get_look_arg(self, stimulus):
        return {"feature" : stimulus["look"]["feature"], "memory" : stimulus["look"]["memory"]}
    # def get_look_arg

    def think_to_action(self, component_arg):
        # 受けた刺激情報を処理。
        self.action_stack.append(component_arg)
    # def think_to_express

    def try_get_action(self):
        if len(self.action_stack) <= 0:
            return None
        return self.action_stack.pop(0) # fixme : ロック
    
    def is_action_express(self, action):
        return action.arg_type() == ComponentArgExpress.ComponentArgExpress.ARG_TYPE
    # def is_action_express

# class MockAIBridgeModule

class MockAI(AIBase.AIBase):
    def __init__(self):
        # read_onlyなexecute可能
        self.eye_sensor = SimpleEyeSensor.SimpleEyeSensor(256, 256)
        self.body = SampleDurabilityComponent.SampleDurabilityComponent(2000.0)
        
        # read_onlyなexecute可能
        self.think_component = MockAIThinkComponent.MockAIThinkComponent()
        self.action_component = MockAIActionComponent.MockAIActionComponent()

        # スレッド実行
        import threading
        self.think_thread = threading.Thread(target=self.think)
        self.action_thread = threading.Thread(target=self.action)

        # multiprocessing
        self.manager = Manager()
        self.bridge_module = MockAIBridgeModule(
            self.manager.list(), # stimulus_stack
            self.manager.list()  # action_stack
            )

        # 生成が終わるまで待つので最後
        self.think_thread.start()
        self.action_thread.start()
    # def __init__

    def reload(self):
        self.bridge_module = self.bridge_module.reload()
        self.think_component = self.think_component.reload()
        self.action_component = self.action_component.reload()
        self.eye_sensor = self.eye_sensor.reload()
    # def reload

    def update(self):
        self.body.update()
    # def update

    def get_status(self):
        return { "durability" : self.body.getDurability() }
    # def get_status
    
    #
    # 見る(刺激関数)
    #
    def _look_core(self, image_file):
        feature = self.eye_sensor.execute(image_file)
        self.bridge_module.look_to_think(feature, image_file)
    # def look

    #
    # 考える
    #
    def _think_core(self):
        self.think_component.start()

        # Durabilityが不足しているので何もしない
        durability_arg = ComponentArgDurability.ComponentArgDurability(self.body.getDurability(), "Sample")
        if self.think_component.calc_enable_think(durability_arg) == False:
            self.think_component.try_sleep()
            return None
        
        stimulus = self.bridge_module.try_get_stimulus()
        # 何もしない FIXME : 自発的な思考
        if stimulus == None:
            #AIUtil.refresh_old_ai_image_memory() # tmpファイルリフレッシュ / HDD/SSD消耗するのでテスト実行はコメントアウト
            self.think_component.try_sleep()
            return None
        
        if self.bridge_module.is_stimulus_look(stimulus):
            look_arg = self.bridge_module.get_look_arg(stimulus)
            action_arg = self.think_component.comfort(look_arg)
            self.bridge_module.think_to_action(action_arg)

        self.think_component.try_sleep()
    # def _think_core

    #
    # 行動関数
    #
    def _action_core(self):
        self.action_component.start()
        
        action = self.bridge_module.try_get_action()
        # 何もしない
        if action == None:
            self.action_component.try_sleep()
            return None

        if self.bridge_module.is_action_express(action):
            self.action_component.express(action)

        # elifにしない、並行実行
        if action.arg_type == "other action":
            pass

        self.action_component.try_sleep()
        return None
    # def _action_core

    # static関数
    def create():
        AIBase.AIBase._initialize()
        return MockAI()
# end class MockAI

# def 

if __name__ == '__main__':
    ai = MockAI.create()

    while True:
        ai.reload()
        ai.update()
        sleep(1.0 / 30.0) # 30fps風


'''
    ai.force_look("../EyeSensor/SampleImage/Apple.jpg")
    ai._think_core()
    ai._action_core()
'''
