# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file BehaviorTreeExecutor.py
# @note

from NodeBase import NodeBase
from NodeStatus import is_status_finish
from NodeStatus import NodeStatus

def find_next_node_and_status_result(current_node):
    for child in current_node.children:
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
# find_next_node_and_status_result

class BehaviorTreeExecutor:

    def __init__(self, root_node):
        self.root_node = root_node
        self.cur_execute_node = None
        self.stack_cur_execute_node = []
        self.is_finish_all_nodes = False
    # def __init__

    def initialize(self):
        self.root_node.initialize()
        self.cur_execute_node = self.root_node
        self.stack_cur_execute_node = []
        self.is_finish_all_nodes = False
    # def initialize

    def execute(self):
        self.cur_execute_node.execute()

        stat = self.cur_execute_node.get_status()
        # 現在node処理が未完
        if is_status_finish(stat) == False:
            return True

        # 次のノードを探す
        self.find_next_node_recursive_and_update_stack()
        return True
    # def execute

    # 次のノードを探す
    # child_nodeに実行が移った場合は親を記憶する
    # cur_execute_nodeのchild全て実行していたら、親ノードから探す
    def find_next_node_recursive_and_update_stack(self):
        result = find_next_node_and_status_result(self.cur_execute_node)
        stat = result[1]
        if stat == NodeStatus.FAILUER:
            # 異常終了
            self.is_finish_all_nodes = True
            return False

        if stat == NodeStatus.SUCCESS:
            # 全てのchildがSUCCESSなら終了
            if len(self.stack_cur_execute_node) == 0:
                self.is_finish_all_nodes = True
                return True

            next_node = self.stack_cur_execute_node.pop() # 親ノードに処理を戻す
            self.cur_execute_node = next_node
            self.find_next_node_recursive_and_update_stack()
            return True
        else:
            # 未実行または、実行中のnodeが見つかった
            next_node = result[0]
            if next_node.get_status() == NodeStatus.INIT:
                self.stack_cur_execute_node.append(self.cur_execute_node)
                self.cur_execute_node = next_node
            else:
                assert next_node.get_status() == NodeStatus.RUNNING, "next_nodeの状態はINITかRUNNINGしか実装してません"
                self.cur_execute_node = self.cur_execute_node
            return True
    # find_next_node

    def is_finish(self):
        return self.is_finish_all_nodes
    # is_finish

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
            self.status = NodeStatus.SUCCESS
    # class SampleExecutionNode

    class RootNode(ExecutionNode):
        def __init__(self, layer, idx):
            ExecutionNode.__init__(self)

        def execute_self(self):
            self.status = NodeStatus.SUCCESS
    # RootNode

    root = SampleExecutionNode(0, 0)
    children = [
        SampleExecutionNode(1, 1),
        SampleExecutionNode(1, 2),
        SampleExecutionNode(1, 3),
    ]
    for child in children:
        root.append_child(child)
    children[1].append_child(SampleExecutionNode(2, 4))
    # idx 0 -> 1 -> 2 -> 4 -> 3

    executor = BehaviorTreeExecutor(root)
    executor.initialize()
    while executor.is_finish_all_nodes == False:
        executor.execute()
