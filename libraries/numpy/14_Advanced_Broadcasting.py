"""
Core Concept: How NumPy executes math on arrays of different shapes without copying data.
Broadcasting is the engine that makes NumPy fast and memory-efficient when working with mismatched dimensions.
"""

import numpy as np

# ==========================================
# 1. THE BROADCASTING RULE
# NumPy compares dimensions starting from the RIGHT (trailing dimensions) and works left.
# Dimensions are compatible ONLY if:
#   1. They are equal, OR
#   2. One of them is 1.
# ==========================================
print("--- 1. The Broadcasting Rule ---")

# Let's say we have a 3x3 matrix (Image pixels, for example)
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
print(f"Matrix shape: {matrix.shape}")

# And a 1D vector (e.g., color adjustments)
vector = np.array([10, 20, 30])
print(f"Vector shape: {vector.shape}\n")

# The shapes are (3, 3) and (3,). 
# NumPy looks at the right-most dimension. Both are 3. Compatible!
# It temporarily "stretches" the vector into a 3x3 matrix in memory to do the math.
result = matrix + vector
print(f"Result of Matrix + Vector:\n{result}")
print("-" * 40)


# ==========================================
# 2. INCOMPATIBLE SHAPES (And how to fix them)
# What if we want to add [10, 20, 30] vertically, down the rows instead of across columns?
# ==========================================
print("\n--- 2. Fixing Incompatible Shapes with np.newaxis ---")

col_vector = np.array([10, 20, 30])

# If we just add it, it adds to the columns. 
# We must explicitly tell NumPy to turn this 1D vector into a 2D column vector (3x1).
# np.newaxis inserts a temporary dimension of size 1.
reshaped_vector = col_vector[:, np.newaxis] 

print(f"Original vector shape: {col_vector.shape}")
print(f"Reshaped vector shape: {reshaped_vector.shape}")
print(f"Reshaped vector:\n{reshaped_vector}\n")

# Now the shapes are (3, 3) and (3, 1). 
# The right-most dimensions are 3 and 1. Compatible! (Because one of them is 1).
# NumPy stretches the '1' to become a '3'.
row_addition = matrix + reshaped_vector
print(f"Result after explicitly broadcasting across rows:\n{row_addition}")
print("-" * 40)


# ==========================================
# 3. CREATING GRIDS (1D to 2D magic)
# You can use broadcasting to generate coordinate grids or multiplication tables instantly,
# without writing nested loops.
# ==========================================
print("\n--- 3. Creating Grids (Outer Operations) ---")

# We want a multiplication table from 1 to 5
a = np.array([1, 2, 3, 4, 5]) # Shape (5,)
b = np.array([1, 2, 3, 4, 5]) # Shape (5,)

# We reshape 'a' to be a column (5, 1) and leave 'b' as a row (5,).
# Shapes: (5, 1) and (5,). 
# NumPy stretches BOTH arrays simultaneously to make a (5, 5) matrix!
multiplication_table = a[:, np.newaxis] * b

print(f"5x5 Multiplication Table generated via Broadcasting:\n{multiplication_table}")
