"""
========================================
PYTHON VARIABLES - COMPLETE GUIDE
========================================

A variable is a container used to store data in memory.

Python is dynamically typed → you don't need to declare type explicitly.
"""

# ========================================
# 1. CREATING VARIABLES
# ========================================

# Simple assignment
x = 10
name = "Aziz"
price = 99.99
is_active = True

print(x, name, price, is_active)


# ========================================
# 2. DYNAMIC TYPING
# ========================================

# Same variable can hold different types
x = 10
print(type(x))  # int

x = "Now I am string"
print(type(x))  # str


# ========================================
# 3. VARIABLE TYPES (DATA TYPES)
# ========================================

# Integer
a = 10

# Float
b = 10.5

# String
c = "Hello"

# Boolean
d = True

print(type(a), type(b), type(c), type(d))


# ========================================
# 4. MULTIPLE VARIABLE ASSIGNMENT
# ========================================

# Assign multiple values at once
x, y, z = 1, 2, 3
print(x, y, z)

# Assign same value to multiple variables
a = b = c = 100
print(a, b, c)


# ========================================
# 5. TYPE CASTING (IMPORTANT)
# ========================================

# Convert types
x = int("10")     # string → int
y = float(5)      # int → float
z = str(100)      # int → string

print(x, y, z)


# ========================================
# 6. VARIABLE NAMING RULES
# ========================================

"""
RULES:
✔ Must start with letter (a-z, A-Z) or underscore (_)
✔ Cannot start with number
✔ Can contain letters, numbers, underscore
✔ Case-sensitive (age ≠ Age)
✔ Cannot use Python keywords
"""

# VALID
name = "Aziz"
_age = 20
user1 = "A"

# INVALID (will cause error)
# 1name = "Wrong"
# user-name = "Wrong"
# class = "Wrong"   # keyword


# ========================================
# 7. VARIABLE NAMING CONVENTIONS
# ========================================

# Snake case (recommended in Python)
user_name = "Aziz"

# Constant (uppercase)
PI = 3.14

# Avoid
# a = 10  ❌ (not descriptive)
age = 20  # ✔


# ========================================
# 8. CHECKING VARIABLE TYPE
# ========================================

x = 10
print(type(x))


# ========================================
# 9. MEMORY REFERENCE (IMPORTANT CONCEPT)
# ========================================

a = 10
b = a

print(a, b)

# Change a
a = 20

print(a, b)  # b is unchanged → different reference now


# ========================================
# 10. DELETING VARIABLES
# ========================================

x = 100
del x

# print(x)  # ERROR → variable deleted


# ========================================
# 11. KEYWORDS (RESERVED WORDS)
# ========================================

"""
You CANNOT use these as variable names:

False, True, None,
and, or, not,
if, else, elif,
for, while, break, continue,
def, return,
class, try, except, etc.
"""


# ========================================
# 12. BEST PRACTICES
# ========================================

"""
✔ Use meaningful names → user_age instead of x
✔ Follow snake_case
✔ Avoid overwriting built-ins → don't use 'list', 'str' as variable names
✔ Keep variables readable
"""


# ========================================
# 13. COMMON MISTAKES
# ========================================

# 1. Forgetting type conversion
age = input("Enter age: ")
# print(age + 10) ❌ ERROR

age = int(age)
print(age + 10)  # ✔

# 2. Case sensitivity issue
name = "Aziz"
# print(Name) ❌ ERROR


# ========================================
# 14. MINI PRACTICE
# ========================================

# Create variables and print them
name = "Aziz"
age = 20
height = 5.5

print(f"My name is {name}, age is {age}, height is {height}")
