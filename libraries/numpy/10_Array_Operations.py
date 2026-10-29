"""
Core Concept: Performing math on datasets efficiently.
This is where NumPy's C-backend truly pays off. You do not write loops to add or 
multiply numbers; you perform element-wise arithmetic and leverage "Broadcasting".
"""

import numpy as np

# ==========================================
# 1. ELEMENT-WISE ARITHMETIC
# Standard math operators apply to the exact corresponding elements in both arrays.
# Both arrays must be the same shape for this to work perfectly.
# ==========================================
print("--- 1. Element-wise Math ---")
arr_A = np.array([10, 20, 30])
arr_B = np.array([1, 2, 3])

print(f"Array A: {arr_A}")
print(f"Array B: {arr_B}\n")

# Addition
print(f"Addition (A + B): {arr_A + arr_B}")

# Subtraction
print(f"Subtraction (A - B): {arr_A - arr_B}")

# Multiplication
print(f"Multiplication (A * B): {arr_A * arr_B}")

# Division
print(f"Division (A / B): {arr_A / arr_B}")
print("-" * 40)


# ==========================================
# 2. UNIVERSAL FUNCTIONS (ufuncs)
# NumPy provides highly optimized mathematical functions that run across the 
# entire array instantly, without any explicit loops.
# ==========================================
print("\n--- 2. Universal Functions (ufuncs) ---")
base_arr = np.array([1, 4, 9, 16, 25])
print(f"Base Array: {base_arr}\n")

# Square root
print(f"Square Root: {np.sqrt(base_arr)}")

# Exponent (e^x)
print(f"Exponential (e^x): {np.exp(base_arr)}")

# Modulo (Remainder after division) - Let's get the remainder when dividing by 3
print(f"Modulo by 3: {np.mod(base_arr, 3)}")
print("-" * 40)


# ==========================================
# 3. AGGREGATION & AXIS OPERATIONS
# Summarizing data. You can summarize the whole array, or just specific rows/columns.
# ==========================================
print("\n--- 3. Aggregations (Sum, Min, Max) ---")
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6]])
print(f"Matrix:\n{matrix}\n")

# Aggregate the ENTIRE matrix
print(f"Total Sum: {np.sum(matrix)}")
print(f"Overall Minimum: {np.min(matrix)}")
print(f"Overall Maximum: {np.max(matrix)}")

# Aggregate along axes (CRITICAL FOR DATA ENGINEERING)
# axis=0 runs operations straight down the columns.
print(f"\nSum of each COLUMN (axis=0): {np.sum(matrix, axis=0)}")

# axis=1 runs operations horizontally across the rows.
print(f"Sum of each ROW (axis=1): {np.sum(matrix, axis=1)}")
print("-" * 40)


# ==========================================
# 4. BROADCASTING (The Magic Feature)
# What happens if you try to do math between arrays of DIFFERENT sizes?
# Normally, that throws an error. But NumPy will intelligently "stretch" (broadcast)
# the smaller array across the larger one if their dimensions are compatible.
# ==========================================
print("\n--- 4. Broadcasting ---")
matrix = np.array([[10, 10, 10], 
                   [20, 20, 20], 
                   [30, 30, 30]])
print(f"Original Matrix:\n{matrix}\n")

# We want to add this 1D vector to our 2D matrix
vector = np.array([1, 2, 3])
print(f"Vector to add: {vector}\n")

# NumPy automatically copies (broadcasts) the vector to match the 3 rows of the matrix.
broadcast_result = matrix + vector

print(f"Result after Broadcasting:\n{broadcast_result}")
# Notice that [1, 2, 3] was added to every single row automatically!
