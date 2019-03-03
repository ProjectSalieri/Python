# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ComponentArgExpress.py
# @note

from IComponentArg import IComponentArg

class ComponentArgExpress(IComponentArg):
    def __init__(self):
        self.speak_str = ""
        self.memory = None
    # def __init__

    def arg_type(self):
        return ComponentArgExpress.arg_type()
    # def arg_type

    def arg_type():
        return "Express"
# class ComponentArgExpress

if __name__ == '__main__':
    express_arg = ComponentArgExpress()
    express_arg.speak_str = "会話メッセージ"
    print("[ArgType]:" + express_arg.arg_type())
    print("[Arg]speak_str:" + express_arg.speak_str)
