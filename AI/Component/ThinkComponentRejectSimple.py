# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file ThinkComponentRejectSimple.py
# @note

# 親ディレクトリ
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from BodyModule import SampleDurabilityModule

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

class ThinkComponentRejectSimple:

    INPUT_NUM = 10

    def __init__(self):
        # パラメータ初期化
        self.record_buf = []
        self.clf = LinearDiscriminantAnalysis()
        import pickle
        with open(ThinkComponentRejectSimple.param_path(), "rb") as f:
            self.clf = pickle.load(f)
        pass
    # def __init__

    def calc_reject(self, current_durability):
        self.record_buf.append(current_durability)
        # データが足りない場合はとりあえず許可
        if len(self.record_buf) < ThinkComponentRejectSimple.INPUT_NUM:
            return False

        if len(self.record_buf) > ThinkComponentRejectSimple.INPUT_NUM:
            self.record_buf.pop(0)

        tmp_x = self.record_buf[0:ThinkComponentRejectSimple.INPUT_NUM:1]
        tmp_x.reverse() # 最新時刻が1次元目になるように

        y = self.clf.predict([tmp_x]) # numpyの配列にしなくてもいいみたい
        return y[0]
    # def calc_reject

    def param_path():
        import os
        # Componentフォルダの上にParamter
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Parameter", "ThinkComponentRejectSimple.pickle")
    # def param_path
# class ThinkComponentRejectSimple

if __name__ == '__main__':

    is_predict_test = False
    if is_predict_test:
        reject_module = ThinkComponentRejectSimple()
        for i in [200, 100, 99, 89, 79, 69, 59, 49, 39, 29, 200, 10]:
            print("durability:" + str(i), end="")
            if reject_module.calc_reject(i):
                print(" => reject")
            else:
                print(" => permit")
            # if
        # for
        import sys
        sys.exit(0)
    
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

        # ある程度のサンプル数は取得
        if durability <= 0.0 and len(record_buf) > ThinkComponentRejectSimple.INPUT_NUM+30:
            print(len(record_buf))
            load_thr.stop()
            module.stop()
            break
    # while
    load_thr.join(1)

    import numpy as np
    x = np.empty((0, ThinkComponentRejectSimple.INPUT_NUM), float)
    y = np.empty((0, 1), int)
    for i in range(len(record_buf)-ThinkComponentRejectSimple.INPUT_NUM):
        # 現在フレーム含め過去10フレーム分を入力とする。古いものからpushされているのでreverse
        x_tmp = record_buf[i:i+ThinkComponentRejectSimple.INPUT_NUM:1]
        x_tmp.reverse() 
        label = 0
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

    print("pickle")
    import pickle
    with open(ThinkComponentRejectSimple.param_path(), mode="wb") as f:
        pickle.dump(clf, f)
    print("load pickle")
    with open(ThinkComponentRejectSimple.param_path(), "rb") as f:
        clf = pickle.load(f)
    
    print("Sample Predict")
    print(clf.predict([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]]))

    # TODO : パラメータ保存

