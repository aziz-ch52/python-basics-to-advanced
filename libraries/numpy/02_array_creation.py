"""
Core Concept: How to generate arrays from scratch.
In real data work, you rarely type out numbers by hand. You generate them.
"""

import numpy as np

# ==========================================
# 1. CREATING ARRAYS FROM PYTHON LISTS
# ==========================================
print("--- 1. From Python Lists ---")

# 1D Array (A single row of numbers, like a vector)
arr_1d = np.array([10, 20, 30, 40])
print(f"1D Array:\n{arr_1d}\n")

# 2D Array (A grid of numbers with rows and columns, like a matrix)
# You make this by passing a list of lists.
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array (Matrix):\n{arr_2d}\n")
print("-" * 40)


# ==========================================
# 2. PRE-FILLED ARRAYS
# Sometimes you just need an empty canvas to fill with data later.
# You define the size by giving it a tuple: (rows, columns).
# ==========================================
print("\n--- 2. Pre-filled Allocations ---")

# np.zeros: Fills the entire grid with 0.
zeros_arr = np.zeros((3, 4)) # 3 rows, 4 columns
print(f"Zeros Array:\n{zeros_arr}\n")

# np.ones: Fills the entire grid with 1.
ones_arr = np.ones((2, 3)) # 2 rows, 3 columns
print(f"Ones Array:\n{ones_arr}\n")

# np.full: Fills the grid with a specific number you choose.
full_arr = np.full((2, 2), 99) # 2 rows, 2 columns, all filled with 99
print(f"Full Array (Filled with 99):\n{full_arr}\n")
print("-" * 40)


# ==========================================
# 3. GENERATING SEQUENCES OF NUMBERS
# Fast ways to create a counting sequence without typing it out.
# ==========================================
print("\n--- 3. Numerical Sequences ---")

# np.arange(start, stop, step)
# Exactly like Python's range(). The 'stop' number is NOT included.
sequence_arr = np.arange(0, 10, 2)
print(f"arange (0 to 8, stepping by 2): {sequence_arr}")

# np.linspace(start, stop, count)
# Gives you a specific number of evenly spaced points between two numbers.
# The 'stop' number IS included here.
linear_space = np.linspace(0, 100, 5) # Give me exactly 5 numbers between 0 and 100
print(f"linspace (5 evenly spaced points): {linear_space}")
print("-" * 40)


# ==========================================
# 4. CONTROLLING DATA TYPES (dtype)
# By default, zeros() and ones() use decimals (floats) like 0.0 or 1.0.
# You can force them to be whole numbers (integers) to save computer memory.
# ==========================================
print("\n--- 4. Forcing Integers ---")

# Notice there are no decimal points here because we added dtype=np.int32
int_zeros = np.zeros((2, 2), dtype=np.int32)
print(f"Integer Zeros:\n{int_zeros}")
