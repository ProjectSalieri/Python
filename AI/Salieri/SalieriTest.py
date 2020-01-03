# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file SalieriTest.py
# @note

from BodyPartsVirtualHp import BodyPartsVirtualHp
from ThinkLayer1st import ThinkLayer1st

class SalieriBody:
    def __init__(self):
        self.mBodyParts = []
        self.mBodyParts.append(BodyPartsVirtualHp(500, 1000))
    # def __init__

    def getParam(self):
        param = []
        for parts in self.mBodyParts:
            param.append(parts.getParam())
        # for
        return param
    # def getParam

    def update(self):
        for parts in self.mBodyParts:
            parts.update()
        # for
    # def update
        

class SalieriTest:

    def __init__(self):
        self.mBody = SalieriBody()
        self.mThinkLayer1st = ThinkLayer1st()
    # def __init__

    def update(self):
        self.mBody.update()

        params = self.mBody.getParam()
        self.mThinkLayer1st.update(params)
    # def update

if __name__ == "__main__":
    salieri = SalieriTest()
    while True:
        salieri.update()
