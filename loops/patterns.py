"""
========================================
PATTERNS - COMPLETE GUIDE
========================================

WHAT ARE PATTERNS?

Patterns are problems where you print shapes
(stars, numbers, pyramids) using loops.

WHY IMPORTANT?

✔ Builds logic
✔ Strengthens nested loops
✔ Improves thinking ability

CORE IDEA:
Outer loop → rows
Inner loop → columns / elements per row
"""


# ========================================
# 1. BASIC SQUARE PATTERN
# ========================================

"""
* * *
* * *
* * *
"""

for i in range(3):          # rows
    for j in range(3):      # columns
        print("*", end=" ")
    print()


# ========================================
# 2. RIGHT TRIANGLE (INCREASING)
# ========================================

"""
*
* *
* * *
* * * *
"""

for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()


# ========================================
# 3. RIGHT TRIANGLE (DECREASING)
# ========================================

"""
* * * *
* * *
* *
*
"""

for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# ========================================
# 4. NUMBER PATTERN
# ========================================

"""
1
1 2
1 2 3
1 2 3 4
"""

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ========================================
# 5. CONSTANT NUMBER PATTERN
# ========================================

"""
1
2 2
3 3 3
4 4 4 4
"""

for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()


# ========================================
# 6. PYRAMID PATTERN
# ========================================

"""
   *
  * *
 * * *
* * * *
"""

n = 4

for i in range(1, n + 1):
    # spaces
    for j in range(n - i):
        print(" ", end="")

    # stars
    for j in range(i):
        print("*", end=" ")

    print()


# ========================================
# 7. INVERTED PYRAMID
# ========================================

"""
* * * *
 * * *
  * *
   *
"""

n = 4

for i in range(n, 0, -1):
    # spaces
    for j in range(n - i):
        print(" ", end="")

    # stars
    for j in range(i):
        print("*", end=" ")

    print()


# ========================================
# 8. DIAMOND PATTERN (ADVANCED)
# ========================================

"""
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
"""

n = 4

# Upper half
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()

# Lower half
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()


# ========================================
# 9. COMMON MISTAKES
# ========================================

"""
❌ Not understanding rows vs columns
❌ Forgetting end=" " (everything prints in new line)
❌ Wrong loop ranges
❌ Not visualizing pattern before coding
"""


# ========================================
# 10. BEST PRACTICES
# ========================================

"""
✔ First draw pattern on paper
✔ Count rows and columns
✔ Break into spaces + elements
✔ Build step by step
"""


# ========================================
# 11. MINI PRACTICE
# ========================================

"""
Try yourself:

1. Reverse number triangle
2. Floyd's triangle
3. Hollow square
4. Right-aligned triangle
"""
