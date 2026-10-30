"""
Core Concept: Locating specific data points or indices based on conditions.
In data engineering, you rarely look at data manually. You write scripts to find 
where the errors, outliers, or specific targets are located inside massive arrays.
"""

import numpy as np

# ==========================================
# 1. FINDING INDICES WITH np.where()
# np.where() is arguably one of the most important functions in NumPy.
# It returns the INDEX POSITIONS where a specific condition is True.
# ==========================================
print("--- 1. np.where() : Locating based on conditions ---")
arr = np.array([10, 25, 30, 45, 50, 15, 60])
print(f"Original Array: {arr}\n")

# Find the indices where the value is exactly 30
# Note: It returns a tuple containing an array of indices.
index_30 = np.where(arr == 30)
print(f"Index where value is 30: {index_30[0]}")

# Find indices where values are greater than 40
indices_high = np.where(arr > 40)
print(f"Indices where values > 40: {indices_high[0]}")
# If you want the actual numbers, pass those indices back into the array!
print(f"The actual values > 40: {arr[indices_high]}")
print("-" * 40)


# ==========================================
# 2. TERNARY OPERATIONS WITH np.where()
# np.where(condition, value_if_true, value_if_false)
# This is heavily used in data cleaning to replace bad data or create flags.
# ==========================================
print("\n--- 2. Data Cleaning with np.where() ---")
test_scores = np.array([85, 42, 90, 30, 75])
print(f"Raw Scores: {test_scores}")

# Let
