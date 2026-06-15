"""
=========================================================
04. DICTIONARY COMPREHENSIONS (DATA CLEANING)
=========================================================
Just like list comprehensions, this is a highly optimized A 
way to transform or filter key-value pairs in a single line.

Syntax: {key: value for key, value in iterable if condition}
=========================================================
"""

# ---------------------------------------------------------
# 1. FILTERING OUT MISSING DATA
# ---------------------------------------------------------
print("--- 1. FILTERING NULLS ---")

# Raw row extracted from a database with missing values (None)
raw_row = {"user_id": 101, "age": 28, "email": "test@test.com", "phone": None, "address": None}

# Clean it: Keep the key-value pair ONLY IF the value is not None
cleaned_row = {k: v for k, v in raw_row.items() if v is not None}

print(f"Cleaned Record: {cleaned_row}")


# ---------------------------------------------------------
# 2. DATA TRANSFORMATION
# ---------------------------------------------------------
print("\n--- 2. VALUE TRANSFORMATION ---")

# Convert a dictionary of daily revenues from USD to EUR (Rate: 0.92)
usd_revenue = {"Monday": 1000, "Tuesday": 1500, "Wednesday": 1200}

eur_revenue = {day: (amount * 0.92) for day, amount in usd_revenue.items()}

print(f"Revenue in EUR: {eur_revenue}")


# ---------------------------------------------------------
# 3. SWAPPING KEYS AND VALUES
# ---------------------------------------------------------
print("\n--- 3. KEY-VALUE SWAP ---")

# Sometimes a dataset gives you IDs mapped to Names, but you need to look up Names to find IDs.
id_to_name = {101: "Alice", 102: "Bob", 103: "Charlie"}

# Invert the dictionary instantly
name_to_id = {name: uid for uid, name in id_to_name.items()}

print(f"Inverted Lookup Table: {name_to_id}")
