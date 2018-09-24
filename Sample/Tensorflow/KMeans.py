# -*- coding: utf-8 -*-
# @author Masakaze Sato
# @file KMeans.py
# @note

import tensorflow as tf
import numpy as np

# Input function for Estimator
def input_fn(raw_data):
    dataset = tf.data.Dataset.from_tensor_slices(raw_data).batch(batch_size=10)
    return dataset.make_one_shot_iterator().get_next()

# test code
if __name__ == '__main__':
    # Test Data
    data_x = np.array([100.0, 110.0, 120.0, 150.0, 155.0, 150.0, 178.0, 180.0, 300.0],
                      dtype = 'float32')
    data_y = np.array([20.0, 25.0, 30.0, 48.0, 45.0, 50.0, 78.0, 75.0, 180.0],
                      dtype = 'float32')
    raw_data = np.c_[data_x, data_y]

    #### main ####
    num_clusters = 5
    kmeans = tf.contrib.factorization.KMeansClustering(
        num_clusters=num_clusters,
        distance_metric=tf.contrib.factorization.KMeansClustering.SQUARED_EUCLIDEAN_DISTANCE,
        use_mini_batch=False)

    # train
    num_iterations = 10
    for i in range(num_iterations):
        print('iteration: ', i)
        kmeans.train(lambda:input_fn(raw_data))
    print('Final cluster centers:', kmeans.cluster_centers())
    print()

    # map the input points to their clusters
    cluster_indices = list(kmeans.predict_cluster_index(lambda:input_fn(raw_data)))
    cluster_centers = kmeans.cluster_centers()
    for i, point in enumerate(raw_data):
        cluster_index = cluster_indices[i]
        center = cluster_centers[cluster_index]
        print('point:', point, 'is in cluster', cluster_index, 'centered at',center)

    # plot
    import matplotlib.pyplot as plt
    plt.grid(True)
    color_arr = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    for i, c in enumerate(cluster_centers):
        plt.plot(c[0], c[1], color=color_arr[i], marker="*")
        
    for i, point in enumerate(raw_data):
        cluster_index = cluster_indices[i]
        center = cluster_centers[cluster_index]
        plt.plot(point[0], point[1], color=color_arr[cluster_index], marker=".")
        plt.plot([point[0], center[0]], [point[1], center[1]], color=color_arr[cluster_index])
    plt.show()
