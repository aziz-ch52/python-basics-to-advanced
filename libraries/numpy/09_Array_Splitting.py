"""
Core Concept: Breaking a large array into smaller, manageable chunks.
This is the exact opposite of joining. In data engineering, you often split 
massive datasets into batches for processing or machine learning (like train/test splits).
"""

import numpy as np

# ==========================================
# 1. SPLITTING 1D ARRAYS
# We use np.array_split() instead of np.split(). 
# Why? If the array doesn't divide equally, np.split() will throw an error and crash, 
# but np.array_split() will intelligently adjust the chunk sizes automatically.
# ==========================================
print("--- 1. Splitting 1D Arrays ---")
arr_1d = np.array([1, 2, 3, 4, 5, 6])
print(f"Original Array: {arr_1d}")

# Split into 3 equal parts
split_3 = np.array_split(arr_1d, 3)
print(f"Split into 3 parts: {split_3}")

# Notice it returns a Python LIST containing the new NumPy arrays.
# Let's see what happens with an unequal split (6 elements into 4 parts)
split_4 = np.array_split(arr_1d, 4)
print(f"Unequal split into 4 parts: {split_4}")
print("-" * 40)


# ==========================================
# 2. ACCESSING THE SPLIT ARRAYS
# Since array_split returns a standard Python list containing NumPy arrays, 
# you just use standard list indexing ([0], [1], etc.) to grab the chunk you want.
# ==========================================
print("\n--- 2. Accessing Split Arrays ---")
print(f"First chunk: {split_3[0]}")
print(f"Second chunk: {split_3[1]}")
print(f"Third chunk: {split_3[2]}")
print("-" * 40)


# ==========================================
# 3. SPLITTING 2D ARRAYS (vsplit and hsplit)
# Just like vstack and hstack for joining, we have intuitive shortcuts for splitting matrices.
# ==========================================
print("\n--- 3. Splitting 2D Matrices ---")
matrix = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12], 
                   [13, 14, 15, 16]])
print(f"Original 4x4 Matrix:\n{matrix}\n")

# np.vsplit (Vertical Split)
# Slices horizontally through the rows (like cutting a sandwich top to bottom).
# Let's split it into 2 pieces (top half and bottom half).
top_half, bottom_half = np.vsplit(matrix, 2)
print(f"vsplit (Top Half - first two rows):\n{top_half}\n")
print(f"vsplit (Bottom Half - last two rows):\n{bottom_half}\n")

# np.hsplit (Horizontal Split)
# Slices vertically through the columns (separating left columns from right columns).
left_half, right_half = np.hsplit(matrix, 2)
print(f"hsplit (Left Half - first two columns):\n{left_half}\n")
print(f"hsplit (Right Half - last two columns):\n{right_half}")
