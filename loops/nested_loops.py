"""
========================================
NESTED LOOPS - COMPLETE GUIDE
========================================

WHAT ARE NESTED LOOPS?

A loop inside another loop.

Outer loop → controls rows
Inner loop → controls columns / repeated work


WHEN TO USE?

✔ Working with 2D data (matrix, grid)
✔ Patterns (stars, numbers)
✔ Comparing combinations

REAL THINKING:
"For each row → run another loop."
"""


# ========================================
# 1. BASIC NESTED LOOP
# ========================================

# Outer loop runs 3 times
# Inner loop runs 2 times for each outer loop

for i in range(3):           # Outer loop
    for j in range(2):       # Inner loop
        print(f"i={i}, j={j}")


# ========================================
# 2. GRID / MATRIX STYLE
# ========================================

# Print a 3x3 grid

for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()   # move to next line


# Output:
# * * *
# * * *
# * * *


# ========================================
# 3. MULTIPLICATION TABLE (1 to 3)
# ========================================

for i in range(1, 4):   # outer loop (table number)
    for j in range(1, 6):   # inner loop (multipliers)
        print(f"{i} x {j} = {i*j}")
    print()   # blank line between tables


# ========================================
# 4. COMPARISON (PAIRING)
# ========================================

# Compare each element with others
nums = [1, 2, 3]

for i in nums:
    for j in nums:
        print(i, j)


# ========================================
# 5. REAL-LIFE SCENARIO
# ========================================

# Search for a pair that sums to target
numbers = [2, 4, 6, 8]
target = 10

for i in numbers:
    for j in numbers:
        if i + j == target:
            print("Pair found:", i, j)


# ========================================
# 6. BREAK IN NESTED LOOP (IMPORTANT)
# ========================================

# Break only exits the INNER loop

for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)


# ========================================
# 7. COMMON MISTAKES
# ========================================

# ❌ Confusing inner vs outer loop
# ❌ Not understanding how many times it runs
# ❌ Forgetting indentation
# ❌ Wrong placement of print()


# ========================================
# 8. BEST PRACTICES
# ========================================

"""
✔ Always visualize rows and columns
✔ Keep nesting levels minimal
✔ Use meaningful variable names (i, j ok for small loops)
✔ Avoid unnecessary nested loops (can be slow)
"""


# ========================================
# 9. MINI PRACTICE
# ========================================

# Print this pattern:
# 1 2 3
# 1 2 3
# 1 2 3

for i in range(3):
    for j in range(1, 4):
        print(j, end=" ")
    print()
