"""
========================================
PYTHON OPERATORS - COMPLETE GUIDE
========================================

Operators are used to perform operations on variables and values.

Types:
1. Arithmetic
2. Comparison
3. Logical
4. Assignment
5. Identity
6. Membership
"""

# ========================================
# 1. ARITHMETIC OPERATORS
# ========================================

a = 10
b = 3

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.33
print(a // b)  # Floor division → 3
print(a % b)   # Modulus → 1
print(a ** b)  # Power → 1000


# ========================================
# 2. REAL-LIFE SCENARIO (CALCULATIONS)
# ========================================

# Example 1: Total bill calculation
price = 499
quantity = 3

total = price * quantity
print("Total Bill:", total)

# Example 2: Discount calculation
discount = 10  # %
final_price = total - (total * discount / 100)
print("Final Price after discount:", final_price)

# Example 3: Average marks
marks1 = 80
marks2 = 90
marks3 = 85

average = (marks1 + marks2 + marks3) / 3
print("Average Marks:", average)

# Example 4: Even/Odd check using modulus
num = 7
print("Is Even?", num % 2 == 0)


# ========================================
# 3. COMPARISON OPERATORS
# ========================================

a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


# ========================================
# 4. LOGICAL OPERATORS
# ========================================

age = 20
has_id = True

# AND → both must be True
print(age >= 18 and has_id)

# OR → at least one True
print(age < 18 or has_id)

# NOT → reverse
print(not has_id)


# ========================================
# 5. REAL-LIFE LOGICAL SCENARIO
# ========================================

# Eligibility check
age = 22
income = 30000

eligible = age >= 18 and income >= 25000
print("Loan Eligible:", eligible)


# ========================================
# 6. ASSIGNMENT OPERATORS
# ========================================

x = 10

x += 5   # x = x + 5
print(x)

x -= 3   # x = x - 3
print(x)

x *= 2
print(x)

x /= 4
print(x)


# ========================================
# 7. IDENTITY OPERATORS
# ========================================

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)    # True (same memory)
print(a is c)    # False (different object)
print(a == c)    # True (same value)


# ========================================
# 8. MEMBERSHIP OPERATORS
# ========================================

numbers = [1, 2, 3, 4]

print(2 in numbers)       # True
print(5 not in numbers)   # True


# ========================================
# 9. COMMON MISTAKES
# ========================================

# 1. Using = instead of ==
# if a = 10 ❌ ERROR

# 2. Division confusion
print(5 / 2)   # 2.5
print(5 // 2)  # 2

# 3. Logical misunderstanding
print(True and False)  # False


# ========================================
# 10. BEST PRACTICES
# ========================================

"""
✔ Use meaningful variable names
✔ Be careful with division vs floor division
✔ Use parentheses in complex expressions
✔ Keep logic simple and readable
"""


# ========================================
# 11. MINI PRACTICE
# ========================================

# Calculate total expense
food = 200
travel = 150
shopping = 500

total_expense = food + travel + shopping
print("Total Expense:", total_expense)

# Check budget condition
budget = 1000
print("Within Budget?", total_expense <= budget)
