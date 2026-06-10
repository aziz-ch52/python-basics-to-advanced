"""
=========================================================
01. SET FUNDAMENTALS (DEDUPLICATION & MATH)
=========================================================
A Set is an UNORDERED collection of UNIQUE items.

Because they are unordered, you cannot use indexing (e.g., my_set[0] will crash).
Because they require unique items, they are the absolute best tool 
for dropping duplicate records and comparing two different datasets.
=========================================================
"""

# ---------------------------------------------------------
# 1. CREATION & AUTOMATIC DEDUPLICATION
# ---------------------------------------------------------
print("--- 1. CREATION & DEDUPLICATION ---")

# Sets use curly braces {}, just like dictionaries, but without key-value pairs.
# Notice we put duplicates in this definition.
active_user_ids = {1001, 1002, 1002, 1003, 1001}

# Python instantly destroys the duplicates in memory.
print(f"Set automatically deduplicated: {active_user_ids}")


# ---------------------------------------------------------
# 2. THE LIST-TO-SET TRICK (DATA CLEANING)
# ---------------------------------------------------------
print("\n--- 2. THE DEDUPLICATION TRICK ---")
# As shown in the applied lists script, casting a messy list into a set 
# is the fastest way to extract only the unique values.

messy_column = ["TX", "NY", "TX", "CA", "NY", "NY", "FL"]
unique_states = list(set(messy_column))

print(f"Unique states extracted: {unique_states}")


# ---------------------------------------------------------
# 3. SET OPERATIONS (CROSS-REFERENCING DATASETS)
# ---------------------------------------------------------
print("\n--- 3. SET MATH (COMPARING TABLES) ---")
# This is where Sets become incredibly powerful for analytics.
# Imagine you have two separate tables of data and need to compare them.

q1_customers = {"Alice", "Bob", "Charlie", "David"}
q2_customers = {"Charlie", "David", "Eve", "Frank"}

# INTERSECTION (&): Who bought in BOTH Q1 and Q2? (Inner Join logic)
repeat_customers = q1_customers & q2_customers
print(f"Repeat Customers (Intersection): {repeat_customers}")

# DIFFERENCE (-): Who bought in Q1 but NOT in Q2? (Left Anti Join logic)
churned_customers = q1_customers - q2_customers
print(f"Churned Customers (Difference): {churned_customers}")

# UNION (|): Give me a master list of EVERY unique customer across both quarters.
all_customers = q1_customers | q2_customers
print(f"All Unique Customers (Union): {all_customers}")


# ---------------------------------------------------------
# 4. FAST LOOKUPS (MEMBERSHIP TESTING)
# ---------------------------------------------------------
print("\n--- 4. HIGH-PERFORMANCE LOOKUPS ---")

banned_ips = {"192.168.1.100", "10.0.0.5", "172.16.0.2"}
incoming_ip = "10.0.0.5"

# The 'in' keyword is O(1) time complexity for sets. It is practically instant.
# Doing this on a massive List would cause performance bottlenecks.
if incoming_ip in banned_ips:
    print(f"ALERT: Blocked connection from {incoming_ip}")
