# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ComponentArgDurability.py
# @note

from IComponentArg import IComponentArg

class ComponentArgDurability(IComponentArg):
    ARG_TYPE = "Durability"
    
    def __init__(self, durability, name):
        self.durability = durability
        self.name = name
    # def __init__

    def arg_type(self):
        return ComponentArgDurability.ARG_TYPE
    # def arg_type

    def durability_name(self):
        return self.name
    # def durability_name
# class ComponentArgDurability

if __name__ == '__main__':
    durability_arg = ComponentArgDurability(10, "Sample")
    print("[ArgType]:" + durability_arg.arg_type())
    print("[Arg]durability name:" + durability_arg.durability_name())
    print("[Arg]durability:" + str(durability_arg.durability))
