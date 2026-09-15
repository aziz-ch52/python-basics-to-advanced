"""
=========================================================
04. DATA SHAPING
=========================================================
Machine Learning models and analytics functions often require 
data to be in a very specific 'shape' (e.g., converting a flat 
list of 12 months into a 3x4 grid of quarters).
=========================================================
"""
import numpy as np

print("--- UNDERSTANDING SHAPE ---")

# A flat 1D array of 12 elements
flat_data = np.arange(1, 13)
print(f"Flat Data: {flat_data}")
print(f"Current Shape: {flat_data.shape} (1D array)")

print("\n--- RESHAPING DATA ---")
# Reshape the 12 elements into a 2D matrix: 3 rows, 4 columns
matrix_3x4 = flat_data.reshape(3, 4)
print(f"3x4 Matrix:\n{matrix_3x4}")
print(f"New Shape: {matrix_3x4.shape}")

# Reshape into a 3D tensor (2 blocks, 2 rows, 3 columns)
# (Used heavily in Deep Learning / TensorFlow)
tensor_3d = flat_data.reshape(2, 2, 3)
print(f"\n3D Tensor:\n{tensor_3d}")
print(f"New Shape: {tensor_3d.shape}")
