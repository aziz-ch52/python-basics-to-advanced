"""
========================================
PYTHON STRINGS - COMPLETE GUIDE
========================================
"""

# ========================================
# 1. CREATING STRINGS
# ========================================

name = "Aziz"
greeting = 'Hello'
multi_line = """This is
multi-line string"""

print(name, greeting)
print(multi_line)


# ========================================
# 2. STRING INDEXING
# ========================================

text = "Python"

print(text[0])    # P
print(text[1])    # y
print(text[-1])   # n


# ========================================
# 3. STRING SLICING
# ========================================

print(text[0:3])   # Pyt
print(text[2:])    # thon
print(text[:4])    # Pyth
print(text[::-1])  # reverse


# ========================================
# 4. STRING OPERATIONS
# ========================================

a = "Hello"
b = "World"

print(a + " " + b)   # concatenation
print(a * 3)         # repetition


# ========================================
# 5. STRING METHODS
# ========================================

msg = "  hello python  "

print(msg.upper())
print(msg.lower())
print(msg.strip())
print(msg.replace("python", "world"))
print(msg.split())


# ========================================
# 6. CHECK METHODS
# ========================================

num = "123"
print(num.isdigit())

text = "abc"
print(text.isalpha())


# ========================================
# 7. STRING FORMATTING
# ========================================

name = "Aziz"
age = 20

print(f"My name is {name} and age is {age}")


# ========================================
# 8. REAL SCENARIO
# ========================================

email = input("Enter email: ")

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")


# ========================================
# 9. COMMON MISTAKES
# ========================================

# Strings are immutable
# text[0] = 'A' ❌ ERROR


# ========================================
# 10. MINI PRACTICE
# ========================================

name = input("Enter name: ")
print("Reversed:", name[::-1])
