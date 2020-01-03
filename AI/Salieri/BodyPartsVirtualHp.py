# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file BodyPartsVirtualHp.py
# @note 仮想体力

from datetime import datetime, timedelta
import threading

class BodyPartsVirtualHp:

    def __init__(self, init_hp, max_hp):
        self.mHp = init_hp
        self.mMaxHp = max_hp

        self.mInterval = timedelta(milliseconds=5000)
        self.mLastUpdateTime = None
        self.mSemaphore = threading.Semaphore()
    # def __init__

    def getParam(self):
        ret = None
        with self.mSemaphore:
            ret = { "Hp" : self.mHp, "MaxHp" : self.mMaxHp }
        return ret
    # def getParam

    def addHp(self, add_hp):
        with self.mSemaphore:
            self.mHp = self.mHp + add_hp
            if self.mHp < self.mMaxHp:
                self.mHp = self.mMaxHp
    # def addHp

    def update(self):
        # 定期実行条件
        curTime = datetime.now()
        if self.mLastUpdateTime == None:
            pass
        else:
            if curTime - self.mLastUpdateTime < self.mInterval:
                return False

        self._update_core()
        #print(str(curTime) + " Hp : " + "(%d / %d)" % (self.mHp, self.mMaxHp))

        self.mLastUpdateTime = curTime
        return True
    # def update

    # private
    def _update_core(self):
        with self.mSemaphore:
            #self.mHp = self.mHp - 0.5
            self.mHp = self.mHp - 10
    # def _update_core
    

# test code
if __name__ == "__main__":
    parts = BodyPartsVirtualHp(100, 2000)
    print(parts.getParam())
    parts.addHp(10)
    while True:
        parts.update()
