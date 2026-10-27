"""
Core Concept: Extracting sections of an array.
Slicing allows you to carve out chunks of data without writing loops. 
CRITICAL RULE: In NumPy, slicing creates a "View", not a copy. If you change the slice, 
you permanently change the original array. Beginners mess this up constantly.
"""

import numpy as np

# ==========================================
# 1. 1D ARRAY SLICING
# Syntax: array[start : stop : step]
# Just like Python lists, the 'stop' index is EXCLUSIVE.
# ==========================================
print("--- 1. 1D Array Slicing ---")
arr_1d = np.array([10, 20, 30, 40, 50, 60, 70])
print(f"Base Array: {arr_1d}")

# Slice from index 1 to 5 (Grabs index 1, 2, 3, 4)
print(f"Slice [1:5]: {arr_1d[1:5]}")

# Slice from index 3 to the very end
print(f"Slice [3:]: {arr_1d[3:]}")

# Slice from the beginning up to index 4
print(f"Slice [:4]: {arr_1d[:4]}")

# Step slicing: Grab every 2nd element
print(f"Slice [::2]: {arr_1d[::2]}")
print("-" * 40)


# ==========================================
# 2. 2D ARRAY SLICING (Matrices)
# Syntax: array[row_start : row_stop, col_start : col_stop]
# You slice the rows, put a comma, then slice the columns.
# ==========================================
print("\n--- 2. 2D Array Slicing ---")
arr_2d = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12]])
print("Base 2D Array:\n", arr_2d)

# Slice the first two rows, and the first three columns
print("\nFirst 2 rows, First 3 columns [0:2, 0:3]:")
print(arr_2d[0:2, 0:3])

# Slice ALL rows, but only grab column index 1 and 2
print("\nAll rows, Middle 2 columns [:, 1:3]:")
print(arr_2d[:, 1:3])

# Slice just the last row, and all columns
print("\nLast row, All columns [-1, :]:")
print(arr_2d[-1, :])
print("-" * 40)


# ==========================================
# 3. THE "VIEW" TRAP (Extremely Important)
# When you slice a Python list, it creates a brand new independent list.
# When you slice a NumPy array, it just looks at the original memory.
# ==========================================
print("\n--- 3. Views vs Copies ---")
original_arr = np.array([1, 2, 3, 4, 5])
print(f"Original before slice edit: {original_arr}")

# Let's create a slice and change the first number to 99
my_slice = original_arr[1:4]
my_slice[0] = 99  

# The original array is now ruined/modified!
print(f"Original AFTER slice edit:  {original_arr}")

# How to fix this? If you need a true independent copy, use .copy()
safe_arr = np.array([1, 2, 3, 4, 5])
safe_slice = safe_arr[1:4].copy() # This allocates new memory
safe_slice[0] = 99
print(f"\nOriginal after .copy() edit remains safe: {safe_arr}")
