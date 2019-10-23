# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file IAI.py
# @note

class IAI:

    def __init__(self):
        pass
    # def __init__

    def init_from_setting(self, setting):
        type = setting["Type"] # Behavior, Native
        
        pass
    # def __init__

    # Actor -> AI -> Componentという階層になりそうなのでAIはcomponentという概念から外したほうが良さそう
    # Actor.update()
    #   AI.update()
    #   for component in components:
    #     component.update()
    #   for component in components:
    #     component.post_update()
    # StateBase(BehaviorTree)な挙動と、長期的にリスケジュールする処理は分けたほうがいいかも
    #   後者はやるとしたら別スレッドで余った処理でタイムスライス。適当なタイミングでBehaviorTreeを再構成(or再選択)
    def update(self):
        pass
    # def update

# class IAI

if __name__ == "__main__":
    pass
