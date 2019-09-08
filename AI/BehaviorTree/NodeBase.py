# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file NodeBase.py
# @note

from NodeStatus import NodeStatus

class NodeBase:

    def __init__(self):
        self.children = []
        self.status = NodeStatus.INIT
        pass
    # def __init__

    def initialize(self):
        self.status = NodeStatus.INIT

        for child in self.children:
            child.initialize()
        # for

        return self.status
    # def initialize

    def get_status(self):
        return self.status
    # def get_status

    def append_child(self, child_node):
        self.children.append(child_node)
    # append_child

    def is_exist_children(self):
        return len(self.children) > 0
    # def is_exist_children

    # default_result = (self.__current_node, NodeStatus.RUNNING)
    def find_next_node_and_status_result(self):
        for child in self.children:
            stat = child.get_status()
            # FAILUERになっているnodeがあれば中断
            if stat == NodeStatus.FAILUER:
                return (None, NodeStatus.FAILUER)

            # RUNNINGの場合はそのnode
            if stat == NodeStatus.RUNNING:
                return (child, NodeStatus.RUNNING)
            
            # INIT statusになっているnodeを探して実行
            if stat == NodeStatus.INIT:
                return (child, NodeStatus.RUNNING)
            #
        # for

        # 全てのnodeがSUCCESSならSUCCESSで終了
        return (None, NodeStatus.SUCCESS)
    # def __find_next_node_and_status_result

if __name__ == "__main__":
    pass
