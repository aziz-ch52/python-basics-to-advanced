"""
Core Concept: Organizing and ordering data.
Sorting arrays efficiently is a fundamental requirement. NumPy provides standard sorting, 
but more importantly, it provides "indirect sorting" (argsort), which is mandatory 
when you need to sort one array based on the values of another.
"""

import numpy as np

# ==========================================
# 1. SORTING 1D ARRAYS (np.sort)
# By default, np.sort() sorts in ascending order and returns a COPY.
# The original array is left completely untouched.
# ==========================================
print("--- 1. Sorting 1D Arrays ---")
arr = np.array([50, 10, 30, 20, 40])
print(f"Original Array: {arr}")

sorted_arr = np.sort(arr)
print(f"Sorted Array (Ascending): {sorted_arr}")
print(f"Notice the original is unchanged: {arr}")

# How to sort in DESCENDING order?
# NumPy doesn't have a built-in "reverse=True" like Python lists. 
# Instead, you sort it normally, and then slice it backwards [::-1].
descending_arr = np.sort(arr)[::-1]
print(f"Sorted Array (Descending): {descending_arr}")
print("-" * 40)


# ==========================================
# 2. SORTING 2D ARRAYS (Matrices)
# Just like aggregations, sorting a 2D matrix requires you to understand axes.
# ==========================================
print("\n--- 2. Sorting 2D Arrays ---")
matrix = np.array([[9, 2, 4], 
                   [3, 8, 1], 
                   [7, 5, 6]])
print(f"Original Matrix:\n{matrix}\n")

# Sorting along axis=1 (Sorts horizontally ACROSS the rows)
# Every row gets sorted independently.
sorted_rows = np.sort(matrix, axis=1)
print(f"Sorted across rows (axis=1):\n{sorted_rows}\n")

# Sorting along axis=0 (Sorts vertically DOWN the columns)
# Every column gets sorted independently.
sorted_cols = np.sort(matrix, axis=0)
print(f"Sorted down columns (axis=0):\n{sorted_cols}")
print("-" * 40)


# ==========================================
# 3. INDIRECT SORTING (np.argsort) - HIGHLY IMPORTANT
# args
