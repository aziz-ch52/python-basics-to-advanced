"""
========================================
PYTHON TYPE CASTING - COMPLETE GUIDE
========================================

Type Casting = Converting one data type to another

Types:
1. Implicit (automatic)
2. Explicit (manual)
"""

# ========================================
# 1. IMPLICIT TYPE CASTING
# ========================================

# Python automatically converts type
a = 10      # int
b = 5.5     # float

result = a + b   # int → float automatically
print(result)    # 15.5
print(type(result))  # float


# ========================================
# 2. EXPLICIT TYPE CASTING
# ========================================

# Manually converting types

# int()
x = int("10")
print(x, type(x))

# float()
y = float(5)
print(y, type(y))

# str()
z = str(100)
print(z, type(z))

# bool()
print(bool(1))    # True
print(bool(0))    # False


# ========================================
# 3. COMMON TYPE CONVERSIONS
# ========================================

# string → int
num = int("25")

# string → float
num2 = float("10.5")

# int → string
text = str(100)

print(num, num2, text)


# ========================================
# 4. INPUT + TYPE CASTING (MOST IMPORTANT)
# ========================================

# input always returns string
age = input("Enter age: ")

# Wrong way
# print(age + 5) ❌ ERROR

# Correct way
age = int(age)
print(age + 5)

# Best practice (direct conversion)
num = int(input("Enter number: "))
print(num * 2)


# ========================================
# 5. REAL-LIFE SCENARIOS
# ========================================

# Example 1: Bill calculation
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity
print("Total:", total)

# Example 2: Percentage calculation
marks = int(input("Enter marks: "))
total_marks = int(input("Enter total marks: "))

percentage = (marks / total_marks) * 100
print("Percentage:", percentage)

# Example 3: String number addition
a = "10"
b = "20"

print(int(a) + int(b))   # 30


# ========================================
# 6. INVALID CONVERSIONS (ERRORS)
# ========================================

# int("abc") ❌ ValueError
# float("xyz") ❌ ValueError

# Safe example
value = "123"

if value.isdigit():
    print(int(value))
else:
    print("Invalid number")


# ========================================
# 7. TYPE CASTING WITH LIST
# ========================================

# Convert input to a list of integers
numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)


# ========================================
# 8. BOOLEAN CONVERSION RULES
# ========================================

print(bool(""))       # False
print(bool("Hello"))  # True
print(bool(0))        # False
print(bool(10))       # True
print(bool([]))       # False


# ========================================
# 9. COMMON MISTAKES
# ========================================

# 1. Forgetting conversion
num = "10"
# print(num + 5) ❌ ERROR

# 2. Wrong type conversion
# int("10.5") ❌ ERROR

# Correct:
print(int(float("10.5")))  # 10


# ========================================
# 10. BEST PRACTICES
# ========================================

"""
✔ Always convert input to the required type
✔ Validate before converting
✔ Use int() for whole numbers
✔ Use float() for decimals
✔ Avoid unnecessary conversions
"""


# ========================================
# 11. MINI PRACTICE
# ========================================

# Take two numbers and print the sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
