"""
========================================
RANGE FUNCTION - COMPLETE GUIDE
========================================

WHAT IS range()?

range() generates a sequence of numbers.
It is commonly used with for-loops.

Syntax:
range(stop)
range(start, stop)
range(start, stop, step)


IMPORTANT:
✔ stop is EXCLUDED (not included)
✔ default start = 0
✔ default step = 1
"""


# ========================================
# 1. BASIC RANGE (ONLY STOP)
# ========================================

# Generates numbers from 0 to 4
for i in range(5):
    print(i)

# Output: 0 1 2 3 4


# ========================================
# 2. START AND STOP
# ========================================

# Generates numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Output: 1 2 3 4 5


# ========================================
# 3. STEP VALUE
# ========================================

# Skip numbers (step = 2)
for i in range(1, 10, 2):
    print(i)

# Output: 1 3 5 7 9


# ========================================
# 4. REVERSE LOOP
# ========================================

# Counting backwards
for i in range(5, 0, -1):
    print(i)

# Output: 5 4 3 2 1


# ========================================
# 5. RANGE WITH LIST INDEX
# ========================================

numbers = [10, 20, 30]

for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])


# ========================================
# 6. REAL-LIFE SCENARIO
# ========================================

# Print multiplication table of 5

num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# ========================================
# 7. CONVERT RANGE TO LIST
# ========================================

r = list(range(5))
print(r)   # [0, 1, 2, 3, 4]


# ========================================
# 8. COMMON MISTAKES
# ========================================

# ❌ Expecting range(5) → 1 to 5 (wrong)
# It is 0 to 4

# ❌ Forgetting stop is excluded

# ❌ Wrong step direction
# range(1, 5, -1) ❌ (won’t run)


# ========================================
# 9. BEST PRACTICES
# ========================================

"""
✔ Always remember stop is excluded
✔ Use meaningful ranges
✔ Use negative step for reverse loops
✔ Prefer direct iteration when possible
"""


# ========================================
# 10. MINI PRACTICE
# ========================================

# Print even numbers from 2 to 20

for i in range(2, 21, 2):
    print(i)
