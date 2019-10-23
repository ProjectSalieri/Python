# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IEatable.py
# @note

class EatableParam:
    def __init__(self):
        self.is_enable_eat = False
    # def __init__

    def init_from_setting(self, one_setting):
        if "IsEnableEat" in one_setting : self.is_enable_eat = one_setting["IsEnableEat"]
    # init_from_setting
# class EatParam

# @note
# IEatからメッセージが送られてきたら食べられるかどうかを返す
# 食べれられる場合は食べられ状態に遷移(Eatedアクション発行?)
# コンポーネントが刺さってない場合は食べられない扱い
class IEatable:

    def __init__(self):
        self.params = {}
    # def __init__

    def init_from_setting(self, setting):
        settings = setting["EatableParams"]
        for one_setting in settings:
            param = EatableParam()
            param.init_from_setting(one_setting)
            condition_name = one_setting["Condition"]
            self.params[condition_name] = param
        # for setting
    # def __init__

    def update(self):
        pass
    # def update

    def post_update(self):
        pass
    # def post_update

# class IEatable

if __name__ == "__main__":
    pass
