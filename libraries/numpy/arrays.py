import numpy as np

# From existing Python sequences
a = np.array([1, 2, 3], dtype=np.float32)         # 1D array
b = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)   # 2D array (matrix)

# Constant value initialization
zeros = np.zeros((3, 4))                          # 3x4 filled with 0.0
ones = np.ones((2, 3), dtype=int)                # 2x3 filled with 1
full = np.full((2, 2), 7)                        # 2x2 filled with 7
empty = np.empty((2, 3))                          # Uninitialized memory (fast)

# Range and sequence generation
# [0, 2, 4, 6, 8] (start, stop, step)
seq1 = np.arange(0, 10, 2)
# 5 evenly spaced values from 0 to 1
seq2 = np.linspace(0, 1, 5)
log_s = np.logspace(1, 3, 3)                      # [10^1, 10^2, 10^3]

# Identity & diagonal matrices
eye = np.eye(3)                                 # 3x3 identity matrix
diag = np.diag([10, 20, 30])                     # Diagonal matrix