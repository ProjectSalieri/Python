# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IBodyComponent.py
# @note 体用のComponentインターフェース

class IBodyComponent:

    def __init__(self):
        pass
    # def __init__

    def is_enable(self):
        return False
    # def is_enable

    def enable(self):
        pass
    # def eable

    def disable(self):
        pass
    # def disable

    # 刺激関数
    # NOTE : BodyComponentの状態によって刺激を拒否するかも( ex. Bodyの故障 / 仮想麻痺 )
    # TODO : 自身で処理できないCoponentArgは登録しない
    def try_stimulate(self, component_arg):
        pass
    # def stimulate

    # ThinkComponentに渡す情報を
    def pop_features(self, query_arg_types):
        pass
    # def pop_to_brain

    def pop_to_body_component(self):
        pass
    # def pop_to_body_component

    def update(self):
        pass
    # def update

    def execute_action(self):
        pass
    # def execute_action

    # 汎用AI作成時にBodyComponentから得られるパラメータを全て得る
    # ハードコーディングAI用にはget_durabilityなど、個別のget関数を実装してください
    def get_parameters(self):
        pass
    # def get_parameters

    # private

    # 条件反射などBodyComponent自身で判断して、何かする処理
    def _update_self(self):
        pass
    # def _update_self
        


# class IBodyComponent
