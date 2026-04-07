"""
========================================
PYTHON INDENTATION - COMPLETE GUIDE
========================================
"""

# ========================================
# 1. WHAT IS INDENTATION?
# ========================================

"""
Indentation = spaces before code

Python uses indentation instead of {}
Standard = 4 spaces
"""


# ========================================
# 2. BASIC EXAMPLE
# ========================================

if True:
    print("Correct indentation")


# ========================================
# 3. WRONG INDENTATION
# ========================================

# if True:
# print("Error") ❌


# ========================================
# 4. INDENTATION IN LOOPS
# ========================================

for i in range(3):
    print("Inside loop:", i)

print("Outside loop")


# ========================================
# 5. NESTED INDENTATION
# ========================================

age = 20

if age >= 18:
    print("Adult")

    if age >= 21:
        print("Eligible for special category")


# ========================================
# 6. COMMON MISTAKES
# ========================================

# ❌ Mixing tabs and spaces
# ❌ Missing indentation
# ❌ Over-indentation

# Always use 4 spaces


# ========================================
# 7. REAL SCENARIO
# ========================================

marks = 85

if marks >= 50:
    print("Pass")

    if marks >= 80:
        print("Distinction")
else:
    print("Fail")


# ========================================
# 8. BEST PRACTICES
# ========================================

"""
✔ Always use 4 spaces
✔ Keep structure clean
✔ Follow consistent indentation
"""


# ========================================
# 9. MINI PRACTICE
# ========================================

num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
