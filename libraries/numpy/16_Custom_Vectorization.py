"""
Core Concept: Applying complex, custom logic across massive datasets.
Standard Python `if/else` statements completely break when you pass them a NumPy array. 
You must use NumPy's specialized functions to apply conditional logic without writing slow loops.
"""

import numpy as np
import math

# ==========================================
# 1. THE PROBLEM: Python `if` statements fail
# ==========================================
print("--- 1. Why standard if/else fails ---")
arr = np.array([1, 5, 10, 15])

try:
    if arr > 5:
        print("This will never print.")
except ValueError as e:
    print(f"ERROR CAUGHT: {e}")
    print("Explanation: Python doesn't know if you mean 'if ANY number is > 5' or 'if ALL are > 5'.")
print("-" * 40)


# ==========================================
# 2. np.select: The "if-elif-else" of NumPy
# When you have multiple conditions (not just a simple True/False like np.where), 
# np.select is your best friend. It evaluates a list of conditions in order.
# ==========================================
print("\n--- 2. Multiple Conditions (np.select) ---")
ages = np.array([12, 18, 25, 65, 8, 45])
print(f"Ages: {ages}")

# Step 1: Define your conditions (The 'if' and 'elif' parts)
conditions = [
    (ages < 13),               # Child
    (ages >= 13) & (ages < 20), # Teen
    (ages >= 20) & (ages < 65)  # Adult
]

# Step 2: Define the results for those conditions
choices = [
    "Child", 
    "Teen", 
    "Adult"
]

# Step 3: Apply np.select (with a 'default' acting as the 'else')
# If an age is 65 or older, it falls to the default.
categories = np.select(conditions, choices, default="Senior")

print(f"Categorized: {categories}")
print("-" * 40)


# ==========================================
# 3. np.vectorize: Using Custom Python Functions
# Sometimes your logic is too complex for basic math operators.
# You can write a standard Python function and 'vectorize' it so it accepts arrays.
# WARNING: This does NOT make it run at C-speed. It just makes the syntax cleaner.
# ==========================================
print("\n--- 3. Custom Functions (np.vectorize) ---")

# A custom Python function that requires standard math module (which breaks on arrays)
def complex_business_logic(x):
    if x < 0:
        return 0
    elif x < 10:
        return math.factorial(x) # math.factorial crashes if given a NumPy array
    else:
        return x ** 2

# Wrap it in np.vectorize
vectorized_logic = np.vectorize(complex_business_logic)

data = np.array([-5, 3, 5, 12])
print(f"Raw Data: {data}")

# Now we can pass the whole array directly into our function
processed_data = vectorized_logic(data)
print(f"Processed Data: {processed_data}")
print("-" * 40)


# ==========================================
# 4. np.piecewise: Mathematical Piece-wise Functions
# A highly optimized alternative to np.vectorize when you are purely doing math.
# It evaluates conditions and applies specific functions to those matching elements.
# ==========================================
print("\n--- 4. Piece-wise Math (np.piecewise) ---")
x = np.array([-5, -2, 0, 2, 5])
print(f"Input X: {x}")

# Mathematical definition:
# If x < 0, multiply by -1
# If x >= 0, square it
result = np.piecewise(
    x, 
    [x < 0, x >= 0], 
    [lambda v: v * -1, lambda v: v ** 2]
)

print(f"Piecewise Result: {result}")
