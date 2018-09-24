# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file DataConvert.py
# @note

import tensorflow as tf
import numpy as np

class ComfortModule:
    def __init__(self):
        self.num_clusters = 3
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

# test code
if __name__ == '__main__':
    comfort = ComfortModule()
    data_0 = np.array([0.0, 1.0],
                      dtype = 'float32')
    data_1 = np.array([0.0, 1.0],
                      dtype = 'float32')
    data_2 = np.array([0],
                      dtype = 'float32')
    raw_data_arr = np.c_[data_0, data_1]

    data_x = np.array([100.0, 110.0, 120.0, 150.0, 155.0, 150.0, 178.0, 180.0, 300.0],
                      dtype = 'float32')
    data_y = np.array([20.0, 25.0, 30.0, 48.0, 45.0, 50.0, 78.0, 75.0, 180.0],
                      dtype = 'float32')
    raw_data = np.c_[data_x, data_y]
    
    comfort.train(raw_data)
    comfort.predict_and_2d_visualize(raw_data)
    pass

