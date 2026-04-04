"""
========================================
PYTHON INPUT & OUTPUT - COMPLETE GUIDE
========================================

Input → Taking data from user
Output → Displaying data to user

Core functions:
- input()
- print()
"""

# ========================================
# 1. BASIC OUTPUT (print)
# ========================================

print("Hello World")
print(10)
print(10, 20, 30)   # multiple values


# ========================================
# 2. SEPARATORS IN PRINT
# ========================================

print(1, 2, 3, sep="-")   # 1-2-3
print("A", "B", "C", sep=" | ")   # A | B | C


# ========================================
# 3. END PARAMETER
# ========================================

print("Hello", end=" ")
print("World")   # Hello World (same line)


# ========================================
# 4. BASIC INPUT
# ========================================

name = input("Enter your name: ")
print("Hello", name)

"""
IMPORTANT:
input() ALWAYS returns STRING
"""


# ========================================
# 5. TYPE CONVERSION WITH INPUT
# ========================================

age = input("Enter age: ")
print(type(age))   # str

# Convert to int
age = int(age)
print(age + 5)

# Direct conversion (best practice)
num = int(input("Enter number: "))
print(num * 2)


# ========================================
# 6. MULTIPLE INPUTS (SPACE SEPARATED)
# ========================================

# Example: 10 20 30
a, b, c = map(int, input("Enter 3 numbers: ").split())
print(a, b, c)


# ========================================
# 7. TAKING LIST INPUT
# ========================================

# Example: 1 2 3 4 5
numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)


# ========================================
# 8. FORMATTED OUTPUT (f-strings)
# ========================================

name = "Aziz"
age = 20

print(f"My name is {name} and age is {age}")


# ========================================
# 9. OTHER FORMATTING METHODS
# ========================================

# format()
print("My name is {} and age is {}".format(name, age))

# % formatting (old style)
print("My name is %s and age is %d" % (name, age))


# ========================================
# 10. PRINTING DIFFERENT DATA TYPES
# ========================================

print("Number:", 10)
print("Float:", 10.5)
print("Boolean:", True)
print("List:", [1, 2, 3])


# ========================================
# 11. ESCAPE CHARACTERS
# ========================================

print("Hello\nWorld")   # new line
print("Hello\tWorld")   # tab space
print("He said \"Hello\"")   # quotes


# ========================================
# 12. MULTILINE OUTPUT
# ========================================

print("""
This is
multi-line
output
""")


# ========================================
# 13. COMMON MISTAKES
# ========================================

# 1. Forgetting type conversion
num = input("Enter number: ")
# print(num + 5) ❌ ERROR

num = int(num)
print(num + 5)  # ✔

# 2. Wrong unpacking
# a, b = input("Enter two numbers: ").split() ❌ if not enough values


# ========================================
# 14. BEST PRACTICES
# ========================================

"""
✔ Always convert input to the required type
✔ Use f-strings for clean output
✔ Validate input in real applications
✔ Keep prompts clear for the user
"""


# ========================================
# 15. MINI PRACTICE
# ========================================

# Take name and age, print formatted output
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, you will be {age + 1} next year")
