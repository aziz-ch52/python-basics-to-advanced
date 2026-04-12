"""
========================================
TERNARY OPERATOR - COMPLETE GUIDE
========================================

WHAT IS A TERNARY OPERATOR?

A short way to write if-else in ONE LINE.

Syntax:
value_if_true if condition else value_if_false


WHEN TO USE?

Use ternary when:
✔ You have simple if-else logic
✔ You want shorter, cleaner code
✔ You are assigning a value based on a condition

DO NOT use when:
❌ Logic is complex
❌ Multiple conditions are involved

REAL-LIFE THINKING:
"Result = Adult if age ≥ 18 else Minor"
"""


# ========================================
# 1. BASIC EXAMPLE
# ========================================

age = 20

# Normal if-else
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(status)

# Ternary version (same logic)
status = "Adult" if age >= 18 else "Minor"
print(status)


# ========================================
# 2. EVEN OR ODD
# ========================================

num = 7

result = "Even" if num % 2 == 0 else "Odd"
print(result)


# ========================================
# 3. MAX OF TWO NUMBERS
# ========================================

a = 10
b = 20

maximum = a if a > b else b
print("Max:", maximum)


# ========================================
# 4. USING WITH INPUT
# ========================================

num = int(input("Enter number: "))

print("Positive") if num >= 0 else print("Negative")


# ========================================
# 5. MULTIPLE CONDITIONS (AVOID THIS)
# ========================================

marks = 85

# ❌ Hard to read (not recommended)
result = "A" if marks >= 90 else "B" if marks >= 75 else "C"

print(result)

# ✔ Better using if-elif-else
if marks >= 90:
    result = "A"
elif marks >= 75:
    result = "B"
else:
    result = "C"

print(result)


# ========================================
# 6. REAL-LIFE SCENARIO
# ========================================

age = 22
has_id = True

# Quick decision
entry = "Allowed" if age >= 18 and has_id else "Not Allowed"
print(entry)


# ========================================
# 7. COMMON MISTAKES
# ========================================

# ❌ Overusing ternary for complex logic
# ❌ Writing unreadable nested ternary
# ❌ Forgetting readability


# ========================================
# 8. BEST PRACTICES
# ========================================

"""
✔ Use ternary only for simple conditions
✔ Keep it readable
✔ Avoid nesting ternary operators
✔ Prefer clarity over short code
"""


# ========================================
# 9. MINI PRACTICE
# ========================================

# Check pass/fail
marks = int(input("Enter marks: "))

result = "Pass" if marks >= 50 else "Fail"
print(result)
