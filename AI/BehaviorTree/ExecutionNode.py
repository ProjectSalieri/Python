# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ExecutionNode.py
# @note

from NodeBase import NodeBase
from NodeStatus import NodeStatus
from NodeStatus import is_status_finish

class ExecutionNode(NodeBase):

    def __init__(self):
        NodeBase.__init__(self)

        self.__next_node = None
        self.is_finish_self = False
    # def __init__

    def initialize(self):
        super()

        # 実行するnodeがセットされてなかったら失敗
        if self.is_exist_children() == False:
            self.status = NodeStatus.FAILUER
            return self.status

        self.is_finish_self = False
        
        return self.status
    # def initialize

    def execute(self):
        if is_status_finish(self.status) == True:
            return False
        #
        self.status = NodeStatus.RUNNING

        # TODO : 低位スレッドでタイムスライス

        # 自分自信の処理を実行
        if self.is_finish_self == False:
            self.execute_self()
            if self.is_finish_self:
                tuple_ret = self.find_next_node_and_status_result()
                self.__next_node = tuple_ret[0]
                self.status = tuple_ret[1]
            return True

        # 子ノードの実行を待つ
        if self.__next_node != None:
            self.__next_node.execute()
        tuple_ret = self.find_next_node_and_status_result()
        self.__next_node = tuple_ret[0]
        self.status = tuple_ret[1]

        return True
    # def executep

    def execute_self(self):
        pass
    # def __execute_self

# class ExecutionNode

if __name__ == "__main__":
    node = ExecutionNode()
    status = node.get_status()
    print(node.is_exist_children())
    node.append_child(ExecutionNode())
    print(node.is_exist_children())
