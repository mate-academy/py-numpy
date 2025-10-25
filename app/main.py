# Task 1
import sys
import time
import numpy as np

# Task 2
py_arr = [i for i in range(1_000)]
print(sys.getsizeof(py_arr))
arr = np.arange(1000)
np_arr = np.array(arr, dtype=np.int8)
print(sys.getsizeof(np_arr))
print(np_arr.nbytes)

# Task 3
np_array = np.arange(10, dtype="f")
print(np_array)
print(np_array[[0, 2, -1]])

# Task 4
array = np.array([2.3, 7.8, 3.2, 1.1, 5.8, 9.5, 17.6, 11.1])[[0, 1, 4, 7]]
print(int(array.sum()))

# Task 5

A = np.array([
    [1, 6],
    [2, 8],
    [3, 11],
    [3, 10],
    [1, 7]
])
print("------------------------------------------------------------")

# 5.1
print(A.mean(axis=1))

# 5.2
print(A.std(axis=0))

# 5.3
print(A.sum(axis=0))

# 5.4
print(A[:2])

# 5.5
print(A[::2])


# Task 6

print("--------------------------------------------------")

# 6.1

start_time = time.time()
A = np.arange(1_000_000)
end_time = time.time()
print("EXECUTION TIME: ", end_time - start_time)


def sum_vectors(vector1, vector2):
    start_time = time.time()
    len_vector = len(vector1)
    vector_range = np.arange(len_vector)
    result = sum(vector1[vector_range] * vector2[vector_range])
    end_time = time.time()
    print("EXECUTION TIME OF SUM: ", end_time - start_time)
    return result


vector10 = np.array([1, 2, 3])
vector20 = np.array([4, 5, 6])
print("VECTORS SUM: ", sum_vectors(vector10, vector20))

# 6.3

def matrix_multiplication(matrix1, matrix2):
    start_time = time.time()
    result = np.array(matrix1) * np.array(matrix2)
    end_time = time.time()
    print(end_time - start_time)
    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
print(matrix_multiplication(matrix1, matrix2))

# 6.4

def numpy_mean(lst):
    start_time = time.time()
    result = np.array(lst).mean()
    end_time = time.time()
    print(end_time - start_time)
    return result

lst = [1, 2, 3, 4, 5]

print(numpy_mean(lst))


# 7

print("-----------------------------------------------------------")

# 7.1


def list_transformation(lst, mask, new_value):
    a = np.array(lst)
    if any(a[mask]):
        a[mask] = new_value
    return a


result_list = [1, 2, 3, 4, 5]
result_mask = [True, False, True, False, True]
result_new_value = 0
print(list_transformation(result_list, result_mask, result_new_value))

# 7.2


def bitwise_expressions(lst1, lst2):
    return (
        np.bitwise_not(lst1).tolist(),
        np.bitwise_and(lst1, lst2).tolist(),
        np.bitwise_or(lst1, lst2).tolist()
    )


list1 = [5, 2, 7, 4, 9]
list2 = [3, 6, 1, 8, 10]

print(bitwise_expressions(list1, list2))

