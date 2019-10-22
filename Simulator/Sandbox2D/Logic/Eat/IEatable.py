# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IEatable.py
# @note

# @note
# IEatからメッセージが送られてきたら食べられるかどうかを返す
# 食べれられる場合は食べられ状態に遷移(Eatedアクション発行?)
class IEatable:

    def __init__(self):
        self.is_enable_eat = False
    # def __init__

    def init_from_setting(self, setting):
        if "IsEnableEat" in setting : self.is_enable_eat = setting["IsEnableEat"]
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
