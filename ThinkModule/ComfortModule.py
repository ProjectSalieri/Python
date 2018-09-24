# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file DataConvert.py
# @note

import tensorflow as tf
import numpy as np

def rgb_array_to_raw_data_array(rgb_arr):
    r_arr = list(map(lambda a: a[0], rgb_arr))
    g_arr = list(map(lambda a: a[1], rgb_arr))
    b_arr = list(map(lambda a: a[2], rgb_arr))

    data_0 = np.array(r_arr,
                      dtype = 'float32')
    data_1 = np.array(g_arr,
                      dtype = 'float32')
    data_2 = np.array(b_arr,
                      dtype = 'float32')
    raw_data_arr = np.c_[data_0, data_1, data_2]
    return raw_data_arr

def create_color_comfort_module_from_sample_param():
    import pickle
    import os

    comfort = None

    sample_param_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ColorComfortModule.pickle")
    if os.path.exists(sample_param_path):
        with open(sample_param_path, mode='rb') as f:
            comfort = pickle.load(f)
        return comfort

    comfort = ComfortModule(5)

    # https://ja.wikipedia.org/wiki/%E8%AD%A6%E5%91%8A%E8%89%B2
    comfort_color = [
        [124.0, 252.0, 0.0], # lawngreen 7cfc00
        [173.0, 255.0, 47.0], # greenyellow adff2f
        [0.0, 255.0, 0.0], # lime 00ff00
        [0.0, 176.0, 107.0], # 緑 00b06b
        [25.0, 113.0, 255.0], # 青 1971ff
        [0.0, 0.0, 255.0], # blue 0000ff
        [30.0, 144.0, 255.0], # dodgeblue 1e90ff
        [0.0, 128.0, 0.0], # green 008000
        [127.0, 255.0, 212.0], # aquamarine 7fffd4
        [0.0, 255.0, 255.0], # cyan 00ffff
    ]
    uncomfort_color = [
        [255.0, 0.0, 0.0], # red ff0000
        [220.0, 20.0, 60.0], # climson dc143c
        [255.0, 69.0, 0.0], # orangered ff4500
        [246.0, 170.0, 0.0], # 黄赤 f6aa00
        [242.0, 231.0, 0.0], # 黄 f2e700
        [255.0, 255.0, 0.0], # yellow ffff00
    ]
    normal_color = [
        [0.0, 0.0, 0.0], # black 000000
        [255.0, 255.0, 255.0], # white ffffff
        [255.0, 165.0, 0.0], # orange ffa500
        [128.0, 128.0, 128.0], # gray 808080
        [218.0, 165.0, 32.0], # goldenrod daa520
        [95.0, 95.0, 95.0], # whitesmoke 5f5f5f
        [255.0, 228.0, 181.0], # moccasin ffe4b5
        [138.0, 43.0, 226.0], #blueviolet 8a2be2
    ]

    rgb_arr = comfort_color + uncomfort_color# + normal_color
    raw_data_arr = rgb_array_to_raw_data_array(rgb_arr)

    # cluster_num = 5
    # comfort -> 0, 2, 3
    # uncomfort -> 1
    # normal -> 4
    comfort.train(raw_data_arr, 10)

    with open(sample_param_path, mode='wb') as f:
        pickle.dump(comfort, f)
    
    return comfort
    

class ComfortModule:
    def __init__(self, num_clusters):
        self.num_clusters = num_clusters
        self.kmeans = tf.contrib.factorization.KMeansClustering(
            num_clusters = self.num_clusters,
            distance_metric=tf.contrib.factorization.KMeansClustering.SQUARED_EUCLIDEAN_DISTANCE,
            use_mini_batch=False)

        # train parameter
        self.batch_size = 20
    # def __init__

    def train(self, raw_data_arr, itr_num = 5):
        for itr in range(itr_num):
            self.kmeans.train(lambda:self._input_func(raw_data_arr))
        # for itr
    # def train

    def predict(self, raw_data_arr):
        cluster_indices = list(self.kmeans.predict_cluster_index(lambda: self._input_func(raw_data_arr)))
        return cluster_indices
    # def predict

    def predict_and_2d_visualize(self, raw_data_arr):
        import matplotlib.pyplot as plt
        color_arr = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'][0:self.num_clusters]
        cluster_centers = self.kmeans.cluster_centers()
        cluster_indices = self.predict(raw_data_arr)
        # クラスター中心の描画
        for i, c in enumerate(cluster_centers):
            plt.plot(c[0], c[1], color=color_arr[i], marker="*")
        # for i, c
        
        # 予測点の描画
#        print(cluster_centers)
        print(cluster_indices)
        for i, point in enumerate(raw_data_arr):
            cluster_index = cluster_indices[i]
            cluster_center = cluster_centers[cluster_index]
            plt.plot(point[0], point[1], color=color_arr[cluster_index], marker=".")
            plt.plot([point[0], cluster_center[0]], [point[1], cluster_center[1]], color=color_arr[cluster_index])
        # for i, point
        plt.show()
    # def predict_and_visualize

    def is_comfort(self, prediction_idx):
        return prediction_idx in [0, 2, 3]
    # def is_comfort
    def is_uncomfort(self, prediction_idx):
        return prediction_idx in [1]

    def _input_func(self, raw_data_arr):
        dataset = tf.data.Dataset.from_tensor_slices(raw_data_arr).batch(batch_size=self.batch_size)
        return dataset.make_one_shot_iterator().get_next()
# def _input_func

# class ComfortModule

# test code
if __name__ == '__main__':
    comfort = create_color_comfort_module_from_sample_param()

    color_array = [
        [255.0, 0.0, 0.0],
        [0.0, 0.0, 255.0],
        [100.0, 100.0, 100.0]
    ]
    ret = comfort.predict(rgb_array_to_raw_data_array(color_array))
    for idx in ret:
        if comfort.is_comfort(idx):
            print("快")
        elif comfort.is_uncomfort(idx):
            print("不快")
        else:
            print("普通")

'''
    comfort.predict_and_2d_visualize(rgb_array_to_raw_data_array(comfort_color))
    comfort.predict_and_2d_visualize(rgb_array_to_raw_data_array(uncomfort_color))
    comfort.predict_and_2d_visualize(rgb_array_to_raw_data_array(normal_color))
'''

