"""
=========================================================
01. TUPLE BASICS (IMMUTABLE RECORDS)
=========================================================
A tuple is an ordered, IMMUTABLE collection of items. 

In data pipelines, immutability is a feature, not a bug. 
You use tuples to lock down data (like a raw SQL record) 
so it cannot be accidentally altered by downstream code.
=========================================================
"""

# ---------------------------------------------------------
# 1. CREATION & INDEXING
# ---------------------------------------------------------
print("--- 1. CREATION & ACCESS ---")

# Tuples use parentheses (). They are zero-indexed like lists.
raw_transaction = ("TXN-9982", "2026-06-12", 450.75, "SUCCESS")

print(f"Transaction ID: {raw_transaction[0]}")
print(f"Amount: ${raw_transaction[2]}")


# ---------------------------------------------------------
# 2. THE IMMUTABILITY RULE
# ---------------------------------------------------------
print("\n--- 2. THE IMMUTABILITY SHIELD ---")

# ❌ The code below would crash the script with a TypeError.
# raw_transaction[3] = "FAILED" 

print("Data locked. Tuple does not support item assignment.")


# ---------------------------------------------------------
# 3. THE SINGLE-ITEM COMMA TRAP
# ---------------------------------------------------------
print("\n--- 3. THE SINGLE-ITEM TRAP ---")
# To create a tuple with one item, you MUST include a trailing comma.

math_expression = (500)      # Python reads this as an integer
valid_single_tuple = (500,)  # The comma makes it a tuple

print(f"Without comma: {type(math_expression)}")
print(f"With comma: {type(valid_single_tuple)}")


# ---------------------------------------------------------
# 4. BUILT-IN METHODS (ONLY TWO)
# ---------------------------------------------------------
print("\n--- 4. AVAILABLE METHODS ---")

binary_flags = (0, 1, 1, 0, 0, 1, 0)

print(f"Count of 1s (True): {binary_flags.count(1)}")
print(f"First occurrence of 1 is at index: {binary_flags.index(1)}")
