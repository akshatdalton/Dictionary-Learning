# -*- coding: utf-8 -*-
"""OMP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17xDdUiDcBga_0PtPnHx1_hmrewfI9SLM
"""

import numpy as np

def find_sparse_representation(phi, y):
    iteration = 0
    max_iteration = phi.shape[1]
    epsilon = 1.0e-5

    A = np.empty((phi.shape[0], 0))
    A_index = np.array([], dtype="int")
    sparse = np.zeros(phi.shape[1])
    x = np.array([])
    residue = y.copy()

    while iteration < max_iteration and np.linalg.norm(residue, ord=1) > epsilon:
        projection = np.absolute(phi.T @ residue)
        argmax_index = np.argmax(projection)

        insert_index = np.searchsorted(A_index, argmax_index)

        A_index = np.insert(A_index, insert_index, argmax_index, axis=0)
        A = np.insert(A, insert_index, phi.T[argmax_index], axis=1)

        x = np.linalg.pinv(A) @ y
        residue = y - (A @ x)

        iteration += 1

    for idx, x_val in enumerate(x):
        sparse[A_index[idx]] = x_val
    
    return sparse

# phi = np.array([[1, 0, 1, 0, 0, 1],
#                [0, 1, 1, 1, 0, 0],
#                [1, 0, 0, 1, 1, 0],
#                [0, 1, 0, 0, 1, 1]])

# y = np.array([0, -10, -100, 0])

# sparse = find_sparse_representation(phi, y)
# print(sparse)

# print(phi @ sparse)
