"""
=========================================================
RAVEL VS FLATTEN (VIEWS VS COPIES)
=========================================================
Both methods convert a multi-dimensional array into a 1D array.
However, their memory management is completely different:

- flatten(): Returns a DEEP COPY. Safe, but consumes extra RAM.
- ravel(): Returns a VIEW (if possible). Extremely memory efficient, 
           but altering the raveled array alters the original data.
=========================================================
"""
import numpy as np

print("--- 1. THE FLATTEN() BEHAVIOR (SAFE COPY) ---")

# Create a 2D matrix
original_matrix_a = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original A before flatten:\n{original_matrix_a}")

# Flatten it
flattened_array = original_matrix_a.flatten()

# Modify the flattened array
flattened_array[0] = 999

print(f"\nModified flattened array: {flattened_array}")
print(f"Original A after flatten (UNCHANGED):\n{original_matrix_a}")


print("\n--- 2. THE RAVEL() BEHAVIOR (MEMORY VIEW) ---")

original_matrix_b = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original B before ravel:\n{original_matrix_b}")

# Ravel it
raveled_array = original_matrix_b.ravel()

# Modify the raveled array
raveled_array[0] = 999

print(f"\nModified raveled array: {raveled_array}")
# WARNING: The original matrix was mutated because 'raveled_array' 
# is just a window looking at the exact same blocks of RAM.
print(f"Original B after ravel (MUTATED):\n{original_matrix_b}")
