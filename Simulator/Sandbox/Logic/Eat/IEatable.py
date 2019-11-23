# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IEatable.py
# @note

class EatableParam:
    def __init__(self):
        self.is_enable_eat = False
        self.is_default = False
    # def __init__

    def init_from_setting(self, one_setting):
        if "IsEnableEat" in one_setting : self.is_enable_eat = one_setting["IsEnableEat"]
        if "IsDefault" in one_setting : self.is_default = one_setting["IsDefault"]
    # init_from_setting
# class EatParam

# @note
# IEatからメッセージが送られてきたら食べられるかどうかを返す
# 食べれられる場合は食べられ状態に遷移(Eatedアクション発行?)
# コンポーネントが刺さってない場合は食べられない扱い
class IEatable:

    def __init__(self):
        self.params = {}
        self.current = None # self.paramsのキーのいずれかを設定
    # def __init__

    def init_from_setting(self, setting):
        settings = setting["EatableParams"]
        for one_setting in settings:
            param = EatableParam()
            param.init_from_setting(one_setting)
            condition_name = one_setting["Condition"]
            self.params[condition_name] = param
            if param.is_default == True:
                self.current = condition_name
        # for setting
    # def init_from_setting

    def update(self):
        pass
    # def update

    def post_update(self):
        pass
    # def post_update

    # if is_use_sensor_message_component -> component.receive_msg
    def is_use_sensor_message_component(self):
        return True
    # def is_use_sensor_message_component

    def send_msg(self, sender, receiver):
        # 食べられたので食べた人に効果メッセージ送信
        # send_msg_to_host("RecoverLife:10", self.ead_host_info["sender"], ead_host_info["receiver"])
        #  receiver.get_host.receive_msg(msg, sender, receiver) ??
        #    for component in components: ret |= component.receive_msg(msg, sender, receiver) ?? send_msg側はどのコンポーネントが答えたかわからないけど、sensor(1とアクターはわかるからいいか)
        pass
    # send_msg

    # AI(かアクター層で)
    #   for component in components:
    #     ret |= component.receive_msg
    #   if ret_one:
    #     if msg == "Eat":
    #       startAction("Eated")
    def receive_msg(self, msg, sender, receiver):
        # Eatableというセンサーがあればそれ、なければBodyをデフォルト反応にするとかかな。。
        # Componentごとにセンサー持っていて、デフォルトはBody(かPhysics)と同じ値が入るとかのほうが依存は少ないか(処理大きいけど)
        # ↑そう考えるとcomponentを並列にするよりPhysicsやセンサーはアクター基本設定が上位にあって、下位に渡していくイメージがいいかも
        # または、RefSensorName : "Body" みたいな感じで参照をデータ化するか
        if msg == "IsEnableEat":
            # 食べられますか確認メッセージ 主にUI表示
            return self.params[self.current].is_enable_eat
        elif msg == "Eat":
            # 食べるアクションを受ける
            # self.eat_host_info = {"sender" : sender, "receiver" : receiver}
            return self.params[self.current].is_enable_eat
        # if msg
    # def receive_msg

# class IEatable

if __name__ == "__main__":
    pass
