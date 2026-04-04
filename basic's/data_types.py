"""
========================================
PYTHON DATA TYPES - COMPLETE GUIDE
========================================

Data Types define the type of data a variable can hold.

Python has built-in data types:
1. Numeric
2. Sequence
3. Set
4. Mapping
5. Boolean
6. NoneType
"""

# ========================================
# 1. NUMERIC DATA TYPES
# ========================================

# Integer (int)
a = 10

# Float (decimal)
b = 10.5

# Complex (rarely used in basics)
c = 2 + 3j

print(type(a), type(b), type(c))


# ========================================
# 2. SEQUENCE DATA TYPES
# ========================================

# 2.1 STRING (str)
name = "Aziz"
print(name[0])      # Indexing
print(name[0:3])    # Slicing

# 2.2 LIST (mutable)
numbers = [1, 2, 3, 4]
numbers.append(5)   # Add element
numbers[0] = 10     # Modify
print(numbers)

# 2.3 TUPLE (immutable)
coords = (10, 20)
# coords[0] = 5 ❌ ERROR
print(coords)


# ========================================
# 3. SET DATA TYPE
# ========================================

# Unordered & unique elements
my_set = {1, 2, 3, 3, 4}
print(my_set)  # duplicates removed

my_set.add(5)
print(my_set)


# ========================================
# 4. MAPPING DATA TYPE (DICTIONARY)
# ========================================

# Key-value pairs
student = {
    "name": "Aziz",
    "age": 20,
    "marks": 85
}

print(student["name"])   # Access
student["age"] = 21      # Update
student["city"] = "Bharuch"  # Add
print(student)


# ========================================
# 5. BOOLEAN DATA TYPE
# ========================================

is_active = True
is_logged_in = False

print(type(is_active))


# ========================================
# 6. NONE TYPE
# ========================================

x = None
print(type(x))


# ========================================
# 7. TYPE CHECKING
# ========================================

x = 10
print(type(x))

# Check specific type
print(isinstance(x, int))  # True


# ========================================
# 8. TYPE CASTING (CONVERSION)
# ========================================

# Convert between types
a = int("10")
b = float(5)
c = str(100)

print(a, b, c)


# ========================================
# 9. MUTABLE vs IMMUTABLE (VERY IMPORTANT)
# ========================================

"""
MUTABLE (can change):
✔ list
✔ dict
✔ set

IMMUTABLE (cannot change):
✔ int
✔ float
✔ str
✔ tuple
"""

# Example
lst = [1, 2, 3]
lst[0] = 100  # ✔ allowed

tup = (1, 2, 3)
# tup[0] = 100 ❌ ERROR


# ========================================
# 10. COMMON OPERATIONS
# ========================================

# String
text = "hello"
print(text.upper())

# List
nums = [3, 1, 2]
nums.sort()
print(nums)

# Set
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))

# Dictionary
d = {"a": 1, "b": 2}
print(d.keys())
print(d.values())


# ========================================
# 11. NESTED DATA TYPES
# ========================================

data = {
    "name": "Aziz",
    "skills": ["Python", "SQL"],
    "details": {
        "age": 20,
        "city": "Bharuch"
    }
}

print(data["skills"][0])
print(data["details"]["city"])


# ========================================
# 12. COMMON MISTAKES
# ========================================

# 1. Confusing list vs tuple
lst = [1, 2, 3]
tup = (1, 2, 3)

# 2. Using the wrong key
# print(student["Name"]) ❌ KeyError (case-sensitive)

# 3. Forgetting type conversion
num = "10"
# print(num + 5) ❌ ERROR


# ========================================
# 13. BEST PRACTICES
# ========================================

"""
✔ Use a list when data changes
✔ Use a tuple for fixed data
✔ Use a set for unique values
✔ Use dict for structured data
✔ Always check the type when debugging
"""


# ========================================
# 14. MINI PRACTICE
# ========================================

# Create all data types
name = "Aziz"
age = 20
marks = [80, 90, 85]
unique_marks = set(marks)
student = {"name": name, "age": age}

print(name, age, marks, unique_marks, student)
