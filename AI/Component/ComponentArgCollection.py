# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ComponentArgCollection.py
# @note 

class ComponentArgCollection:
    def __init__(self):
        self._args = [] # 最初はarrayから始める
    # def __init__

    def is_exist(self):
        return len(self._args) > 0
    # def is_exist

    def append(self, arg):
        # TODO : 上限数などもうけるかも
        self._args.append(arg)
    # def append

    def pop_by_query(self, query_arg_types):
        result = []
        tmp = []
        for i in range(len(self._args)):
            arg = self._args.pop(0)
            if arg.arg_type() in query_arg_types:
                result.append(arg)
            else:
                tmp.append(arg)
        # for
        self._args = self._args + tmp
        return result
    # def pop_by_query
# ComponentArgCollection

# test code
if __name__ == '__main__':
    from ComponentArgDurability import ComponentArgDurability
    from ComponentArgDirectAction import ComponentArgDirectAction
    
    collection = ComponentArgCollection()
    collection.append(ComponentArgDurability(100.0, "Durability1"))
    collection.append(ComponentArgDirectAction())
    collection.append(ComponentArgDurability(200.0, "Durability2"))

    query_args = collection.pop_by_query([ComponentArgDurability.ARG_TYPE])
    print("query:" + ComponentArgDurability.ARG_TYPE)
    for arg in query_args:
        print(arg.arg_type() + ":" + arg.durability_name())
    print("\n")

    query_args = collection.pop_by_query([ComponentArgDirectAction.ARG_TYPE])
    print("query:" + ComponentArgDirectAction.ARG_TYPE)
    for arg in query_args:
        print(arg.arg_type() + ":")
    print("\n")

    query_args = collection.pop_by_query(["None1", "None2"])
    print("None query:" + str(len(query_args)))
    print("\n")

    collection.append(ComponentArgDurability(100.0, "Durability3"))
    collection.append(ComponentArgDirectAction())
    collection.append(ComponentArgDurability(200.0, "Durability4"))

    query_args = collection.pop_by_query([ComponentArgDirectAction.ARG_TYPE, ComponentArgDurability.ARG_TYPE])
    print("query:" + "[" + ComponentArgDirectAction.ARG_TYPE + "," + ComponentArgDurability.ARG_TYPE + "]")
    for arg in query_args:
        print(arg.arg_type() + ":")
    print("\n")
# test code
