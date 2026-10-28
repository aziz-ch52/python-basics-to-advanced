"""
Core Concept: Combining multiple arrays into one.
In data pipelines, you constantly receive data in chunks (e.g., daily sales files). 
You must stitch these chunks together along specific axes (rows or columns).
"""

import numpy as np

# ==========================================
# 1. JOINING 1D ARRAYS (Concatenation)
# np.concatenate() takes a TUPLE or LIST of arrays and stitches them together.
# ==========================================
print("--- 1. Joining 1D Arrays ---")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])

# Notice the double parentheses. We are passing a single tuple containing the arrays.
joined_1d = np.concatenate((arr1, arr2, arr3))
print(f"Concatenated 1D: {joined_1d}")
print("-" * 40)


# ==========================================
# 2. JOINING 2D ARRAYS (Axes Matter)
# When joining matrices, you must specify the 'axis'.
# axis=0 means joining vertically (stacking rows on top of each other).
# axis=1 means joining horizontally (stitching columns side-by-side).
# ==========================================
print("\n--- 2. Joining 2D Arrays (axis=0 vs axis=1) ---")
matrix1 = np.array([[1, 2], 
                    [3, 4]])

matrix2 = np.array([[5, 6], 
                    [7, 8]])

# Axis 0 (Vertical Join) - Adding more rows
# Think of this like appending new records to a database table.
joined_axis_0 = np.concatenate((matrix1, matrix2), axis=0)
print(f"Joined along Axis 0 (Vertical):\n{joined_axis_0}\n")

# Axis 1 (Horizontal Join) - Adding more columns
# Think of this like adding a new feature/column to an existing dataset.
joined_axis_1 = np.concatenate((matrix1, matrix2), axis=1)
print(f"Joined along Axis 1 (Horizontal):\n{joined_axis_1}")
print("-" * 40)


# ==========================================
# 3. HELPER FUNCTIONS: vstack and hstack
# Because writing `axis=0` and `axis=1` can get tedious and hard to read,
# NumPy provides shortcut functions for stacking vertically and horizontally.
# ==========================================
print("\
