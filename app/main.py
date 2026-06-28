## Task 1

import numpy as np
import sys

## Task 2

py_array = [0] * 1000
print("Python array size:", sys.getsizeof(py_array), "bytes")

np_array = np.zeros(1000, dtype=np.int8)
print("NumPy array size:", np_array.nbytes, "bytes")

## Task 3

arr = np.array([1.5, 4.2, 7.9, 3.3, 9.8, 0.5], dtype=float)
selected = arr[[0, 2, -1]]
print("Original array:", arr)
print("Selected elements:", selected)

## Task 4

array = np.array([2.3, 7.8, 3.2, 1.1, 5.8, 9.5, 17.6, 11.1])
selected = array[[1, 4, 7, 0]]
print("Selected elements:", selected)
print("Sum:", selected.sum())

## Task 5

A = np.array([
    [1, 6],
    [2, 8],
    [3, 11],
    [3, 10],
    [1, 7]
])

### Task 5.1 Find the mean for each column by `x` axis

mean_cols = A.mean(axis=0)
print(mean_cols)

### Task 5.2 Get the standard deviation by `y` axis

std_rows = A.std(axis=1)
print(std_rows)

### Task 5.3 Get the sum of all elements in `A` by `y` axis

sum_rows = A.sum(axis=1)
print(sum_rows)

### Task 5.4 Get the following result using multi-dim selection:

part1 = A[[0, 1], :]
print(part1)

##  Task 5.5. Get the following result using multi-dim selection:

part2 = A[[0, 2, 4], :]
print(part2)

## Task 6

### Task 6.1

# Python code
print([i for i in range(1000000)])


# %time np.arange(1_000_000)

### Task 6.2

# Python code
def vector_dot(vector1, vector2):
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result


vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
result = 0
print(vector_dot(vector1, vector2))


# %time vector_dot(vector1, vector2)
# result

# v1 = np.array([1, 2, 3])
# v2 = np.array([4, 5, 6])

# %time np.dot(v1, v2)

### Task 6.3

# Python code
def hadamard_product(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] * matrix2[i][j])
        result.append(row)
    return result


matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
print(hadamard_product(matrix1, matrix2))


# m1 = np.array([[1, 2], [3, 4]])
# m2 = np.array([[5, 6], [7, 8]])

# %time m1 * m2

### Task 6.4

# Python code
def compute_mean(lst):
    total = 0
    for num in lst:
        total += num
    result = total / len(lst)
    return result


lst = [1, 2, 3, 4, 5]
print(compute_mean(lst))


# arr = np.array([1, 2, 3, 4, 5])
# %time arr.mean()

## Task 7

### Task 7.1

# Python code
def mask_update(lst, mask, new_value):
    for i in range(len(lst)):
        if mask[i]:
            lst[i] = new_value


lst = [1, 2, 3, 4, 5]
mask = [True, False, True, False, True]
new_value = 0
mask_update(lst, mask, new_value)
print(lst)


# lst = np.array([1, 2, 3, 4, 5])
# mask = np.array([True, False, True, False, True])
# lst[mask] = 0
# lst

### Task 7.2

# Python code
def bitwise_vector_operations(lst1, lst2):
    bitwise_complement = [~x for x in lst1]
    bitwise_and = [x & y for x, y in zip(lst1, lst2)]
    bitwise_or = [x | y for x, y in zip(lst1, lst2)]
    return bitwise_complement, bitwise_and, bitwise_or


list1 = [5, 2, 7, 4, 9]
list2 = [3, 6, 1, 8, 10]
(result_bitwise_complement,
 result_bitwise_and,
 result_bitwise_or) = bitwise_vector_operations(list1, list2)
print(result_bitwise_complement, result_bitwise_and, result_bitwise_or)


# arr1 = np.array([5, 2, 7, 4, 9])
# arr2 = np.array([3, 6, 1, 8, 10])
# bitwise_complement = ~arr1
# bitwise_and = arr1 & arr2
# bitwise_or = arr1 | arr2
# bitwise_complement, bitwise_and, bitwise_or

### Task 7.3 Optional

# Python code
def process_filtered_numbers(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and (num % 3 == 0 or num > 10):
            modified_num = (num ^ 7) + 2
            result.append(modified_num)
    return result


my_list = [6, 9, 12, 14, 17, 20]
result_python_style = process_filtered_numbers(my_list)
print(result_python_style)

# arr = np.array([6, 9, 12, 14, 17, 20])
# mask = (arr % 2 == 0) & ((arr % 3 == 0) | (arr > 10))
# result_np = ((arr ^ 7) + 2)[mask]
# result_np
