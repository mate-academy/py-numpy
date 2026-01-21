import numpy as np
import sys

py_array = [0] * 1000
np_array = np.zeros(1000, dtype=np.uint8)

print(py_array)
print(np_array)

arr = np.array([1.1, 2.2, 3.6,  3.5, 6.8, 2.0, 9.1, 4.6])
selected = arr[[0, 1, -1]]
print(selected)

A = np.array([ [1, 6], [2, 8], [3, 11], [3, 10], [1, 7] ])
mean_columns = np.mean(A, axis=0)
print(mean_columns)
