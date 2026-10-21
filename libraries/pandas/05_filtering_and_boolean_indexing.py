"""
Core Concept: Row filtering based on logic.
This is your SQL WHERE clause applied in Python. 

A hard truth: beginners constantly mess this up by using standard Python 'and' / 'or' operators. 
Pandas doesn't use those. It uses bitwise operators (&, |, ~). If you forget the parentheses 
around your conditions, your code will crash. Pay attention to the syntax here.
"""

import pandas as pd

# ==========================================
# SETUP: Creating a mock dataset of software developers
# ==========================================
dev_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Language': ['Python', 'Java', 'Python', 'C++', 'Python', 'JavaScript'],
    'Bugs_Fixed': [45, 12, 89, 5, 120, 34],
    'Years_Active': [3, 1, 5, 0, 8, 2],
    'Is_Senior': [False, False, True, False, True, False]
}
df = pd.DataFrame(dev_data)

print("--- Base DataFrame ---")
print(df)
print("-" * 50)


# ==========================================
# 1. SINGLE CONDITION FILTERING
# Creating a boolean mask (a Series of True/False values) and passing it to the DataFrame.
# ==========================================

print("\n--- 1. Single Condition ---")
# SQL Equivalent: SELECT * FROM df WHERE Language = 'Python'

# Step 1: Create the mask (You don't usually save this to a variable, but it shows what's happening under the hood)
is_python_dev = df['Language'] == 'Python'
print("Boolean Mask:\n", is_python_dev.head(3)) 

# Step 2: Apply the mask inside the brackets
python_devs = df[df['Language'] == 'Python']
print("\nFiltered DataFrame (Python Devs only):\n", python_devs)
print("-" * 50)


# ==========================================
# 2. MULTIPLE CONDITIONS (AND / OR)
# You MUST wrap each condition in parentheses: (Condition A) & (Condition B).
# & = AND
# | = OR
# ~ = NOT
# ==========================================

print("\n--- 2. Multiple Conditions ---")
# SQL Equivalent: SELECT * FROM df WHERE Language = 'Python' AND Bugs_Fixed > 50

# AND logic (&)
high_performing_python = df[(df['Language'] == 'Python') & (df['Bugs_Fixed'] > 50)]
print("Python devs with > 50 bugs fixed:\n", high_performing_python)

# OR logic (|)
# SQL Equivalent: SELECT * FROM df WHERE Language = 'Java' OR Language = 'C++'
java_or_cpp = df[(df['Language'] == 'Java') | (df['Language'] == 'C++')]
print("\nJava or C++ devs:\n", java_or_cpp)

# NOT logic (~)
# Reversing a condition. Let's find everyone who is NOT a senior.
juniors = df[~df['Is_Senior']]
print("\nNon-senior devs:\n", juniors)
print("-" * 50)


# ==========================================
# 3. THE .isin() METHOD
# When you have a list of targets, writing multiple OR conditions is sloppy. 
# Use .isin() instead. This maps directly to the SQL 'IN' operator.
# ==========================================

print("\n--- 3. Using .isin() ---")
# SQL Equivalent: SELECT * FROM df WHERE Language IN ('Java', 'JavaScript', 'C++')

target_languages = ['Java', 'JavaScript', 'C++']
other_devs = df[df['Language'].isin(target_languages)]
print("Devs using Java, JavaScript, or C++:\n", other_devs)
print("-" * 50)


# ==========================================
# 4. THE .query() METHOD (Advanced/Cleaner Syntax)
# If the bracket notation with all the ampersands and parentheses looks ugly to you, 
# you can pass a string expression directly to .query(). It's highly readable.
# ==========================================

print("\n--- 4. Using .query() ---")

# Variables from your Python environment can be referenced using the @ symbol.
min_bugs = 40

# Look at how clean this is compared to the bracket notation.
query_result = df.query("Language == 'Python' and Bugs_Fixed > @min_bugs")

print(f"Python devs with > {min_bugs} bugs fixed (using .query):\n", query_result)
