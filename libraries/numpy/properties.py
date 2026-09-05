import numpy as np

# 1. Variable definitions (all created first)
a = np.array([1, 2, 3], dtype=np.float32)
b = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
zeros = np.zeros((3, 4))
ones = np.ones((2, 3), dtype=int)
full = np.full((2, 2), 7)
empty = np.empty((2, 3))
seq1 = np.arange(0, 10, 2)
seq2 = np.linspace(0, 1, 5)
log_s = np.logspace(1, 3, 3)
eye = np.eye(3)
diag = np.diag([10, 20, 30])

# 2. Output prints with actual values in comments
print("a:\n", a)
# [1. 2. 3.]

print("\nb:\n", b)
# [[1 2 3]
#  [4 5 6]]

print("\nzeros:\n", zeros)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

print("\nones:\n", ones)
# [[1 1 1]
#  [1 1 1]]

print("\nfull:\n", full)
# [[7 7]
#  [7 7]]

print("\nempty:\n", empty)
# Note: arbitrary uninitialized values from RAM, e.g.:
# [[0.00000000e+000 0.00000000e+000 0.00000000e+000]
#  [0.00000000e+000 2.45785055e-312 2.45785055e-312]]

print("\nseq1:\n", seq1)
# [0 2 4 6 8]

print("\nseq2:\n", seq2)
# [0.   0.25 0.5  0.75 1.  ]

print("\nlog_s:\n", log_s)
# [  10.  100. 1000.]

print("\neye:\n", eye)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

print("\ndiag:\n", diag)
# [[10  0  0]
#  [ 0 20  0]
#  [ 0  0 30]]
