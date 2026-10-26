"""
Core Concept: Accessing specific elements inside your arrays.
NumPy indexing is similar to Python lists for 1D arrays, but it introduces 
a much cleaner "coordinate" system for 2D and 3D arrays.
"""

import numpy as np

# ==========================================
# 1. 1D ARRAY INDEXING
# Exactly the same as standard Python lists.
# ==========================================
print("--- 1. 1D Array Indexing ---")
arr_1d = np.array([10, 20, 30, 40, 50])
print(f"Base 1D Array: {arr_1d}")

# Getting the first element (Index 0)
print(f"First element: {arr_1d[0]}")

# Getting the third element (Index 2)
print(f"Third element: {arr_1d[2]}")

# Negative indexing grabs from the end of the array (-1 is the last item)
print(f"Last element: {arr_1d[-1]}")
print("-" * 40)


# ==========================================
# 2. 2D ARRAY INDEXING (Matrices)
# This is where NumPy shines. Instead of ugly chained brackets like arr[row][col],
# NumPy uses a clean comma-separated coordinate system: arr[row, col]
# ==========================================
print("\n--- 2. 2D Array Indexing ---")
arr_2d = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
print("Base 2D Array:\n", arr_2d)

# Grab the element in the first row (0) and first column (0)
print(f"\nElement at row 0, col 0: {arr_2d[0, 0]}")

# Grab the element in the second row (1) and third column (2)
print(f"Element at row 1, col 2: {arr_2d[1, 2]}")

# Grab the very last element using negative indexing for both row and column
print(f"Last element (bottom right): {arr_2d[-1, -1]}")
print("-" * 40)


# ==========================================
# 3. 3D ARRAY INDEXING (Tensors)
# The coordinate system just adds another axis: arr[layer, row, col]
# ==========================================
print("\n--- 3. 3D Array Indexing ---")
# 2 layers, each containing a 2x2 matrix
arr_3d = np.array([[[10, 20], 
                    [30, 40]], 
                   
                   [[50, 60], 
                    [70, 80]]])

# Let's extract the number 70. 
# It is in the second layer (1), second row (1), first column (0).
print(f"Extracting 70: {arr_3d[1, 1, 0]}")
print("-" * 40)


# ==========================================
# 4. MODIFYING ELEMENTS
# You can use indexing to permanently change the values inside the array.
# ==========================================
print("\n--- 4. Modifying Elements ---")
mutating_arr = np.array([5, 10, 15, 20])
print(f"Original Array: {mutating_arr}")

# Change the second item (index 1) to 99
mutating_arr[1] = 99
print(f"Modified Array: {mutating_arr}")

# IMPORTANT WARNING: NumPy arrays are strictly typed!
# If you try to push a decimal into an integer array, NumPy will silently chop off the decimal.
mutating_arr[0] = 3.14159
print(f"After trying to insert 3.14159: {mutating_arr}")
# Notice it became 3, not 3.14159, because the array type is integer.
