"""
Core Concept: Executing real mathematical matrix operations.
NumPy isn't just for moving data around; it is the backbone of machine learning 
math. You must know how to do dot products and matrix multiplications.
"""

import numpy as np

# ==========================================
# 1. DOT PRODUCT & MATRIX MULTIPLICATION
# The standard '*' operator does ELEMENT-WISE multiplication. 
# Real matrix multiplication requires np.dot() or the '@' operator.
# ==========================================
print("--- 1. Matrix Multiplication ---")
matrix_A = np.array([[1, 2], 
                     [3, 4]])

matrix_B = np.array([[5, 6], 
                     [7, 8]])

# Wrong way for linear algebra (Element-wise)
print(f"Element-wise (A * B):\n{matrix_A * matrix_B}\n")

# Correct way (Dot Product / Matrix Multiplication)
# Method 1: np.dot()
print(f"Dot Product (np.dot):\n{np.dot(matrix_A, matrix_B)}\n")

# Method 2: The '@' Operator (Modern Python standard for matrix math)
print(f"Matrix Math (A @ B):\n{matrix_A @ matrix_B}")
print("-" * 40)


# ==========================================
# 2. LINEAR ALGEBRA MODULE (np.linalg)
# NumPy has a dedicated submodule for advanced linear algebra.
# ==========================================
print("\n--- 2. Advanced Linear Algebra (np.linalg) ---")

# A. Matrix Determinant
# A scalar value that is a function of the entries of a square matrix.
det = np.linalg.det(matrix_A)
print(f"Determinant of Matrix A: {det:.2f}")

# B. Matrix Inverse
# Multiplying a matrix by its inverse results in the Identity Matrix (ones on the diagonal).
# NOTE: Not all matrices have an inverse (determinant must not be 0).
if det != 0:
    inverse_A = np.linalg.inv(matrix_A)
    print(f"\nInverse of Matrix A:\n{inverse_A}")
    
    # Prove it! A @ A_inverse should equal the Identity Matrix
    identity = np.round(matrix_A @ inverse_A)
    print(f"\nProof (A @ A_inv = Identity):\n{identity}")
else:
    print("Matrix A is singular and cannot be inverted.")
