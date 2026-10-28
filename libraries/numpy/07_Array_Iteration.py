"""
Core Concept: Going through elements one by one.
WARNING: Iterating through NumPy arrays using 'for' loops is slow. You should always try 
to use vectorization (math operations) first. But sometimes, you have no choice. 
When you must iterate, here is how you do it.
"""

import numpy as np

# ==========================================
# 1. ITERATING 1D ARRAYS
# This works exactly like a standard Python list.
# ==========================================
print("--- 1. Iterating 1D Arrays ---")
arr_1d = np.array([10, 20, 30])

print("Standard 1D loop:")
for x in arr_1d:
    print(x)
print("-" * 40)


# ==========================================
# 2. ITERATING 2D ARRAYS
# If you run a standard loop on a 2D array, it goes row by row, NOT element by element.
# ==========================================
print("\n--- 2. Iterating 2D Arrays ---")
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("Standard 2D loop (Goes row by row):")
for row in arr_2d:
    print(f"Row: {row}")

# If you actually want every single number, you would need a loop inside a loop (Nested Loop).
# This is very slow in Python.
print("\nNested loop (Element by element):")
for row in arr_2d:
    for element in row:
        print(element)
print("-" * 40)


# ==========================================
# 3. THE NUMPY WAY: np.nditer()
# Instead of writing ugly nested loops for 2D or 3D arrays, NumPy provides nditer().
# It flattens the array in memory and goes through every single element efficiently.
# ==========================================
print("\n--- 3. Using np.nditer() ---")
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("Iterating a 3D array element-by-element without nested loops:")
for element in np.nditer(arr_3d):
    print(element)
print("-" * 40)


# ==========================================
# 4. ITERATING WITH INDEX COORDINATES: np.ndenumerate()
# Sometimes you need the actual data AND its exact coordinate location (row, col).
# This is similar to Python's enumerate(), but works for multidimensional grids.
# ==========================================
print("\n--- 4. Getting Coordinates with np.ndenumerate() ---")
matrix = np.array([[10, 20], [30, 40]])

for coordinates, value in np.ndenumerate(matrix):
    print(f"Location {coordinates} contains value: {value}")
