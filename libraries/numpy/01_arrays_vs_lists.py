"""
=========================================================
01. NUMPY ARRAYS VS PYTHON LISTS
=========================================================
NumPy's core object is the ndarray (N-dimensional array). 
Unlike Python lists, which can hold mixed data types (slow), 
NumPy arrays hold a single data type (incredibly fast).

This script proves the speed difference in execution.
=========================================================
"""
import numpy as np
import time

print("--- PROVING NUMPY SUPERIORITY ---")

size = 10_000_000

# 1. Standard Python Lists
list_a = list(range(size))
list_b = list(range(size))

start_time = time.time()
# Python requires a for-loop to add lists element-by-element
list_c = [list_a[i] + list_b[i] for i in range(len(list_a))]
python_time = time.time() - start_time
print(f"Standard Python List addition took: {python_time:.4f} seconds")

# 2. NumPy Arrays
arr_a = np.arange(size)
arr_b = np.arange(size)

start_time = time.time()
# NumPy performs "Vectorization" - adding the arrays instantly without a loop
arr_c = arr_a + arr_b
numpy_time = time.time() - start_time
print(f"NumPy Array addition took:          {numpy_time:.4f} seconds")

print(f"\n[CONCLUSION] NumPy was {python_time / numpy_time:.1f}x faster.")
