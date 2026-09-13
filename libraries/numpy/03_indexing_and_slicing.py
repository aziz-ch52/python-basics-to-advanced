"""
=========================================================
03. SLICING MATRICES (2D DATA)
=========================================================
Data usually comes in rows and columns (2D matrices). 
You must know how to slice out specific columns or rows 
for analysis.
=========================================================
"""
import numpy as np

print("--- MATRIX SLICING ---")

# Creating a 2D array (Think of this as 3 rows, 4 columns of data)
# Example: 3 stores, 4 quarters of sales
sales_matrix = np.array([
    [100, 150, 200, 250],  # Store A
    [90,  110, 140, 170],  # Store B
    [300, 320, 350, 400]   # Store C
])

print("Full Sales Matrix:\n", sales_matrix)

# Syntax: matrix[row_slice, column_slice]

print("\n1. Isolate Store B (Row index 1, all columns):")
print(sales_matrix[1, :])

print("\n2. Isolate Quarter 3 (All rows, Column index 2):")
print(sales_matrix[:, 2])

print("\n3. Isolate Store A & B, Quarters 1 & 2 (Subset):")
print(sales_matrix[0:2, 0:2])
