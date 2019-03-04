# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ThinkComponentRejectSimple.py
# @note

# 親ディレクトリ
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BodyModule import SampleDurabilityModule

class ThinkComponentRejectSimple:

    def __init__(self):
        pass
    # def __init__
# class ThinkComponentRejectSimple

if __name__ == '__main__':

    # 別スレッドで実行する負荷関数
    import threading
    class TestLoadThread(threading.Thread):
        def __init__(self):
            super(TestLoadThread, self).__init__()
            self.stop_event = threading.Event()
            self.setDaemon(True)
        #
        def stop(self):
            self.stop_event.set()
        #
        def run(self):
            import random, time, math
            while not self.stop_event.is_set():
                r = random.randrange(3)
                if r == 0:
                    time.sleep(5) # 何もしない
                elif r == 1:
                    # 小タスク
                    for i in range(100000):
                        for k in range(3):
                            math.exp(1+k)
                elif r == 2:
                    # 重めのタスク
                    for j in range(100):
                        for i in range(100000):
                            for k in range(3):
                                math.exp(1+k)
                            #
                        #
                    #
                # if
            # while
        # class
    
    module = SampleDurabilityModule.SampleDurabilityModule(200.0)
    record_buf = []

    import time
    load_thr = TestLoadThread()
    load_thr.start()
    while True:
        module.update()
        time.sleep(1) # 5秒間隔
        durability = module.getDurability()
        print("\rDurability:" + str(durability), end="")
        # 150個バッファを持っておく
        record_buf.append(durability)
        if len(record_buf) > 150:
            record_buf.pop(0)

        if durability <= 0.0:
            load_thr.stop()
            module.stop()
            break
    # while
    load_thr.join(1)
    
    import numpy as np    
    x = np.empty((0, 10), float)
    y = np.empty((0, 1), int)
    for i in range(len(record_buf)-10):
        # 現在フレーム含め過去10フレーム分を入力とする。古いものからpushされているのでreverse
        x_tmp = record_buf[i:i+10:1]
        x_tmp.reverse() 
        label = 1
        if i >= 100:
            # 最後50個はrejectしておいた方がよさそう
            label = 1
        x = np.append(x, np.array([x_tmp]), axis=0)
        y = np.append(y, label)
    # for

    print("LDA learn start")
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    clf = LinearDiscriminantAnalysis()
    clf.fit(x, y)
    print("Sample Predict")
    print(clf.predict([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]]))


