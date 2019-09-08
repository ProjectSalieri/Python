# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file RandomSelectorNode.py
# @note

import random

from NodeBase import NodeBase
from NodeStatus import NodeStatus
from NodeStatus import is_status_finish

class RandomSelectorNode(NodeBase):

    def __init__(self):
        NodeBase.__init__(self)

        self.__selected_node = None
        self.__random_param = []
    # def __init__

    def initialize(self):
        super()

        self.__selected_node = None
    # def initialize

    def init_connection(self, children, params):
        assert len(children) == len(params), "子ノードの数(=%d)とランダムパラメータ数(=%d)が一致してません" % (len(children), len(params))
        
        sum_v = sum(params)
        for v in params:
            self.__random_param.append(v / sum_v)

        for child in children:
            self.append_child(child)
    # def init_connection

    def execute(self):
        if is_status_finish(self.status):
            return False
        
        self.status = NodeStatus.RUNNING
        
        # 選択ノード
        if self.__selected_node == None:
            selected_idx = len(self.__random_param)-1
            r = random.random()
            tmp_v = 0.0
            for i in range(len(self.__random_param)):
                tmp_v = tmp_v + self.__random_param[i]
                if r <= tmp_v:
                    selected_idx = i
                    break
                #
            #
            self.__selected_node = self.children[selected_idx]
        # if selected_node

        self.__selected_node.execute()

        stat = self.__selected_node.get_status()
        if is_status_finish(stat):
            self.status = stat

        return True
    # def execute

# class RandomSelectorNode

if __name__ == "__main__":
    from ExecutionNode import ExecutionNode
    from datetime import datetime
    class SampleExecutionNode(ExecutionNode):
        def __init__(self, layer, idx):
            ExecutionNode.__init__(self)
            self.v = datetime.now()
            self.layer = layer
            self.idx = idx

        def execute_self(self):
            print("idx=%d  layer=%d  " % (self.idx, self.layer), end="")
            print(self.v)
            self.is_finish_self = True
    # class SampleExecutionNode
    
    node = RandomSelectorNode()
    children = [
        SampleExecutionNode(1, 0),
        SampleExecutionNode(1, 1),
        SampleExecutionNode(1, 2),
    ]
    children[0].append_child(SampleExecutionNode(2, 3))
    
    node.init_connection(
        children,
        [2, 1, 1]
    )

    while is_status_finish(node.get_status()) == False:
        node.execute()
    # while
