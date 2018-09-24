# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file DataConvert.py
# @note

import tensorflow as tf
import numpy as np

class ComfortModule:
    def __init__(self):
        self.num_clusters = 7
        self.kmeans = tf.contrib.factorization.KMeansClustering(
            num_clusters = self.num_clusters,
            distance_metric=tf.contrib.factorization.KMeansClustering.SQUARED_EUCLIDEAN_DISTANCE,
            use_mini_batch=False)

        # train parameter
        self.batch_size = 10
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
        for i, point in enumerate(raw_data_arr):
            cluster_index = cluster_indices[i]
            cluster_center = cluster_centers[cluster_index]
            plt.plot(point[0], point[1], color=color_arr[cluster_index], marker=".")
            plt.plot([point[0], cluster_center[0]], [point[1], cluster_center[1]], color=color_arr[cluster_index])
        # for i, point
        plt.show()
    # def predict_and_visualize

    def _input_func(self, raw_data_arr):
        dataset = tf.data.Dataset.from_tensor_slices(raw_data_arr).batch(batch_size=self.batch_size)
        return dataset.make_one_shot_iterator().get_next()
# def _input_func

# class ComfortModule

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

# test code
if __name__ == '__main__':
    comfort = ComfortModule()

    # https://ja.wikipedia.org/wiki/%E8%AD%A6%E5%91%8A%E8%89%B2
    comfort_color = [
        [124.0, 252.0, 0.0], # lawngreen 7cfc00
        [173.0, 255.0, 47.0], # greenyellow adff2f
        [0.0, 255.0, 0.0], # lime 00ff00
        [0.0, 176.0, 107.0], # 緑 00b06b
        [25.0, 113.0, 255.0], # 青 1971ff
        [0.0, 0.0, 255.0], # blue 0000ff
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
    ]

    rgb_arr = comfort_color + uncomfort_color + normal_color
    raw_data_arr = rgb_array_to_raw_data_array(rgb_arr)
    
    comfort.train(raw_data_arr)
    comfort.predict_and_2d_visualize(raw_data_arr)
    pass

