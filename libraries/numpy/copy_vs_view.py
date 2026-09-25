"""
NumPy: Copy vs. View

This script demonstrates the critical difference between copying an array 
and creating a view of an array in NumPy.

Key Differences:
1. COPY: A deep copy of the original array. It owns its data. Changes to the 
   copy do NOT affect the original array, and vice versa.
2. VIEW: A shallow reference to the original array. It does NOT own its data. 
   Changes to the view DIRECTLY affect the original array. (Note: Slicing a 
   NumPy array creates a view, unlike standard Python lists where slicing creates a copy).
"""

import numpy as np

def before():
    print("\n" + "-" * 10 + " BEFORE MODIFICATION " + "-" * 10)


def after():
    print("\n" + "-" * 10 + " AFTER MODIFICATION " + "-" * 10)

# Initialize original arrays
a = np.array([23, 43, 65, 87, 45])
b = np.array([54, 36, 87, 34, 97, 11])

before()
print(f"Original a: {a}")
print(f"Original b: {b}")

# 1. DEEP COPY: Independent clone
# Changing 'c' will NOT affect 'a'
c = a.copy()
c[3] = 234

# 2. VIEW / REFERENCE: Shared memory
# Changing 'd' WILL directly change 'a'
d = a
d[3] = 999

after()
print(f"a (Changed! d modified this): {a}")
print(f"b (Unchanged)               : {b}")
print(f"c (Isolated Deep Copy)      : {c}")
print(f"d (Reference to a)          : {d}")

# Quick confirmation test
print("\n" + "-" * 10 + " MEMORY CHECK " + "-" * 10)
print(f"Do 'a' and 'd' share memory? {np.shares_memory(a, d)}")
print(f"Do 'a' and 'c' share memory? {np.shares_memory(a, c)}")
