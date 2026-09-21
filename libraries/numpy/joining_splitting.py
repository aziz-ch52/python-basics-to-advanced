"""
NumPy - Joining and Splitting Arrays
File: joining_array.py

Topics covered:
1. concatenate()
2. stack()
3. hstack()
4. vstack()
5. split()
6. hsplit()
7. vsplit()
"""

import numpy as np

# 1. concatenate()
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("concatenate():", np.concatenate((a, b)))

# 2D concatenate
a_2d = np.array([[1, 2], [3, 4]])
b_2d = np.array([[5, 6], [7, 8]])
print("concatenate(axis=0):\n", np.concatenate((a_2d, b_2d), axis=0))
print("concatenate(axis=1):\n", np.concatenate((a_2d, b_2d), axis=1))

# 2. stack()
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("stack(axis=0):\n", np.stack((a, b), axis=0))
print("stack(axis=1):\n", np.stack((a, b), axis=1))

# 3. hstack()
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("hstack():\n", np.hstack((a, b)))

# 4. vstack()
print("vstack():\n", np.vstack((a, b)))

# 5. split()
arr = np.array([10, 20, 30, 40, 50, 60])
print("split():", np.split(arr, 3))
print("split([2, 4]):", np.split(arr, [2, 4]))

# 6. hsplit()
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("hsplit():", np.hsplit(arr, 2))

# 7. vsplit()
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print("vsplit():", np.vsplit(arr, 2))
