# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SequenceNode.py
# @note

from NodeBase import NodeBase
from NodeStatus import NodeStatus
from NodeStatus import is_status_finish

class SequenceNode(NodeBase):

    def __init__(self):
        NodeBase.__init__(self)

        self.__current_node = None
    # def __init__

    def initialize(self):
        super()

        # 実行するnodeがセットされてなかったら失敗
        if self.is_exist_children() == False:
            self.status = NodeStatus.FAILUER
            return self.status

        # 最初に実行するnodeを選択
        tuple_ret = self.find_next_node_and_status_result()
        self.__current_node = tuple_ret[0]
        self.status = tuple_ret[1]
        return self.status
    # def initialize

    def execute(self):
        if is_status_finish(self.status) == True:
            return False
        #
        self.status = NodeStatus.RUNNING

        # TODO : 低位スレッドでタイムスライス
        self.__current_node.execute()

        tuple_ret = self.find_next_node_and_status_result()
        self.__current_node = tuple_ret[0]
        self.status = tuple_ret[1]

        return True
    # def execute
# class SequenceNode

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

    node = SequenceNode()
    node.append_child(SampleExecutionNode(1, 0))
    child = SampleExecutionNode(1, 1)
    child.append_child(SampleExecutionNode(2, 2))
    node.append_child(child)
    node.append_child(SampleExecutionNode(1, 3))

    node.initialize()
    cnt = 0
    print(node.get_status())
    while is_status_finish(node.get_status()) == False:
        print("Turn : %d" % (cnt))
        node.execute()
        cnt = cnt + 1
    # while

