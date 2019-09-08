# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file NodeStatus.py
# @note

from enum import Enum

class NodeStatus(Enum):
    INIT = 0
    SUCCESS = 1
    FAILUER = 2
    RUNNING = 3
# class NodeStatus

def is_status_finish(status):
    return status == NodeStatus.SUCCESS or status == NodeStatus.FAILUER
# def is_status_finish

if __name__ == "__main__":
    status = NodeStatus.SUCCESS
    print("%s(=%d)" % (status, status.value))
    print("is_status_finish=" + str(is_status_finish(status)))

    status = NodeStatus.INIT
    print("%s(=%d)" % (status, status.value))
    print("is_status_finish=" + str(is_status_finish(status)))
