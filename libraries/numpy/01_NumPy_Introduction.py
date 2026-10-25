"""
Core Concept: What is NumPy and why do we use it instead of standard Python lists?
"""

import numpy as np

# ==========================================
# 1. PYTHON LISTS VS NUMPY ARRAYS
# Python lists can hold anything, but they are slow and take up a lot of memory.
# NumPy arrays are tightly packed memory blocks designed for math.
# ==========================================
print("--- 1. The Visual Difference ---")
python_list = [1, 2, 3, 4, 5]
numpy_array = np.array([1, 2, 3, 4, 5])

print(f"Standard Python List: {python_list}")
print(f"NumPy Array: {numpy_array}")
# Notice the NumPy array prints without commas between the numbers. 
# This is how you quickly tell them apart on your screen.

# ==========================================
# 2. VECTORIZATION (Math without loops)
# If you want to multiply every number in a Python list by 2, you have to write a loop.
# In NumPy, you just multiply the whole array at once. This is called "Vectorization".
# ==========================================
print("\n--- 2. Doing Math (Vectorization) ---")

# Python way: Requires a loop
python_math = [x * 2 for x in python_list]
print(f"Python loop result: {python_math}")

# NumPy way: Instant math across the entire array
numpy_math = numpy_array * 2
print(f"NumPy vectorized result: {numpy_math}")
# Note: This isn't just shorter to write; under the hood, NumPy uses C code to run this 
# much faster than Python ever could.

# ==========================================
# 3. STRICT TYPING (Homogeneous Data)
# Python lists let you mix text, decimals, and whole numbers.
# NumPy hates mixed data. It forces everything to be the same type to keep memory organized.
# ==========================================
print("\n--- 3. Strict Data Types ---")

mixed_list = [1, 2.5, "text"]
print(f"Python allows mixed data: {mixed_list}")

# If you force mixed data into NumPy, it converts everything into strings to make them match.
mixed_array = np.array([1, 2.5, "text"])
print(f"NumPy forces them all to be the same type (strings): {mixed_array}")
