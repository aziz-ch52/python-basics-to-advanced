"""
Core Concept: Changing the layout of your data without changing the data itself.
Reshaping is mandatory in data engineering. Often, a machine learning model will 
require a 2D matrix, but your data is currently a 1D vector. You must reshape it.
"""

import numpy as np

# ==========================================
# 1. RESHAPING 1D TO 2D
# The golden rule: The total number of elements must remain the same.
# If you have 12 items, you can make a 3x4 matrix or 4x3 matrix, but not a 3x5.
# ==========================================
print("--- 1. Reshaping 1D to 2D ---")
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(f"Original 1D Array (Shape {arr_1d.shape}):\n{arr_1d}\n")

# Reshape into 4 rows and 3 columns (4 * 3 = 12 elements)
arr_4x3 = arr_1d.reshape(4, 3)
print(f"Reshaped to 4x3 Matrix:\n{arr_4x3}\n")

# Reshape into 2 rows and 6 columns (2 * 6 = 12 elements)
arr_2x6 = arr_1d.reshape(2, 6)
print(f"Reshaped to 2x6 Matrix:\n{arr_2x6}")
print("-" * 40)


# ==========================================
# 2. RESHAPING 1D TO 3D
# Adding depth. We need 3 dimensions that multiply together to equal 12.
# Let's do 2 layers, 2 rows, 3 columns (2 * 2 * 3 = 12).
# ==========================================
print("\n--- 2. Reshaping 1D to 3D ---")
arr_3d = arr_1d.reshape(2, 2, 3)
print(f"Reshaped to 3D (2 layers of 2x3):\n{arr_3d}")
print("-" * 40)


# ==========================================
# 3. THE "UNKNOWN DIMENSION" TRICK (-1)
# Sometimes you know how many columns you want, but you don't want to do the math 
# to figure out how many rows that requires. You can pass -1, and NumPy will calculate it.
# ==========================================
print("\n--- 3. Using -1 for Unknown Dimensions ---")

# Let's say we have 16 elements.
arr_16 = np.arange(1, 17) # Numbers 1 through 16

# We want 4 columns. We let NumPy figure out the rows by passing -1.
auto_rows = arr_16.reshape(-1, 4)
print(f"NumPy calculated the rows automatically:\n{auto_rows}")
print("-" * 40)


# ==========================================
# 4. FLATTENING ARRAYS (2D/3D back to 1D)
# When you need to feed an image (2D/3D) into a standard algorithm, you often 
# have to flatten it back into a single straight line of data (1D vector).
# ==========================================
print("\n--- 4. Flattening Arrays ---")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original Matrix:\n{matrix}\n")

# Method 1: Using reshape(-1)
flat_reshape = matrix.reshape(-1)
print(f"Flattened using reshape(-1): {flat_reshape}")

# Method 2: Using .flatten()
# NOTE: flatten() always creates a COPY of the data. reshape() tries to create a VIEW.
flat_copy = matrix.flatten()
print(f"Flattened using .flatten():  {flat_copy}")
