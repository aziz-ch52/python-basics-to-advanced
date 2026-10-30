"""
Core Concept: Understanding the anatomy of your arrays.
Before you can manipulate data, you need to know its shape, size, and how much memory it uses. 
You will use these attributes constantly to debug errors when arrays don't align properly.
"""

import numpy as np

# ==========================================
# SETUP: Creating three different arrays to inspect
# ==========================================
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# A 3D array is like a stack of matrices (e.g., layers of an image)
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("--- The Arrays ---")
print("2D Array:\n", arr_2d)
print("\n3D Array:\n", arr_3d)
print("-" * 40)

# ==========================================
# 1. DIMENSIONS (.ndim)
# Tells you how many axes (directions) the array has.
# 1D = Vector, 2D = Matrix, 3D = Tensor / Cube.
# ==========================================
print("\n--- 1. Dimensions (.ndim) ---")
print(f"1D Array Dimensions: {arr_1d.ndim}")
print(f"2D Array Dimensions: {arr_2d.ndim}")
print(f"3D Array Dimensions: {arr_3d.ndim}")


# ==========================================
# 2. SHAPE (.shape)
# The most important attribute. It returns a tuple showing the size along each dimension.
# (Rows, Columns) for 2D. (Depth, Rows, Columns) for 3D.
# ==========================================
print("\n--- 2. Shape (.shape) ---")
# Returns (3, 3) because it has 3 rows and 3 columns.
print(f"2D Array Shape: {arr_2d.shape}") 

# Returns (2, 2, 2) because it has 2 layers, each containing 2 rows and 2 columns.
print(f"3D Array Shape: {arr_3d.shape}")


# ==========================================
# 3. TOTAL SIZE (.size)
# The total number of individual elements inside the array.
# It is simply the multiplication of the numbers in the .shape tuple.
# ==========================================
print("\n--- 3. Total Elements (.size) ---")
print(f"Total elements in 2D array: {arr_2d.size}") # 3 * 3 = 9
print(f"Total elements in 3D array: {arr_3d.size}") # 2 * 2 * 2 = 8


# ==========================================
# 4. DATA TYPE (.dtype)
# Tells you exactly what type of data is stored inside.
# Remember: NumPy arrays are homogeneous. Everything inside is exactly this type.
# ==========================================
print("\n--- 4. Data Type (.dtype) ---")
print(f"Data type of 2D array: {arr_2d.dtype}")

# Let's create an array of decimals to see the difference
float_arr = np.array([1.5, 2.5, 3.5])
print(f"Data type of float array: {float_arr.dtype}")


# ==========================================
# 5. MEMORY CONSUMPTION (.itemsize and .nbytes)
# Critical for data engineering. If you load a 10GB dataset, you need to know 
# if your RAM can handle it before your computer crashes.
# ==========================================
print("\n--- 5. Memory Footprint ---")

# .itemsize tells you how many bytes a SINGLE element takes up.
# An int32 takes 4 bytes. An int64 takes 8 bytes.
print(f"Size of one element in 2D array: {arr_2d.itemsize} bytes")

# .nbytes tells you the total memory consumed by the ENTIRE array.
# It is exactly equal to (.size * .itemsize)
print(f"Total memory of 2D array: {arr_2d.nbytes} bytes")
