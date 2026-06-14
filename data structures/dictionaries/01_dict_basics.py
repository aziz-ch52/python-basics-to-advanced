"""
=========================================================
01. DICTIONARY BASICS (KEY-VALUE PAIRS)
=========================================================
A dictionary is an UNORDERED, MUTABLE collection of key-value pairs.

You do not look up data by its index position (0, 1, 2). 
You look up data by its exact Key. This is the exact structure 
of JSON data, making it the most important structure for 
ingesting data from the web or APIs.
=========================================================
"""

# ---------------------------------------------------------
# 1. CREATION & ACCESS
# ---------------------------------------------------------
print("--- 1. CREATION & LOOKUPS ---")

# Keys must be immutable (strings, numbers, or tuples).
# Values can be absolutely anything (lists, other dicts, etc.).
user_profile = {
    "user_id": 1055,
    "username": "data_ninja",
    "is_active": True,
    "total_queries": 450
}

# Fast O(1) lookup using the exact key name
print(f"User ID: {user_profile['user_id']}")
print(f"Queries run: {user_profile['total_queries']}")


# ---------------------------------------------------------
# 2. MUTATION (ADDING & UPDATING)
# ---------------------------------------------------------
print("\n--- 2. UPDATING RECORDS ---")

# If the key exists, it UPDATES the value.
user_profile["total_queries"] = 451

# If the key does NOT exist, it ADDS a new key-value pair.
user_profile["subscription_tier"] = "Pro"

print(f"Updated Profile: {user_profile}")


# ---------------------------------------------------------
# 3. THE FATAL FLAW: KEYERRORS
# ---------------------------------------------------------
print("\n--- 3. THE KEYERROR CRASH ---")

# ❌ If you ask for a key that doesn't exist using standard bracket notation, 
# your entire pipeline will crash immediately.
# print(user_profile["last_login"]) # KeyError: 'last_login'

print("Never use bracket notation if you aren't 100% sure the key exists. Use .get() instead (covered in methods).")

