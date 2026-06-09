"""
=========================================================
01. LIST BASICS (DATA ANALYTICS FOCUS)
=========================================================
A list is Python's fundamental ordered, mutable data structure.

While you will eventually use Pandas DataFrames for real-world 
analytics, understanding list indexing and slicing is mandatory 
because those exact mechanics carry over to advanced libraries.
=========================================================
"""

# ---------------------------------------------------------
# 1. LIST CREATION
# ---------------------------------------------------------
# In analytics, a list often represents a single column or row of data.

customer_ages = [24, 35, 28, 42, 19, 55, 31]
data_columns = ["user_id", "transaction_amount", "date", "status"]

# Mixed data types are allowed, but it is bad practice for large datasets 
# as it breaks mathematical operations later.
mixed_record = [1001, 250.75, "2026-06-09", True] 

print("--- 1. CREATION ---")
print(f"Total ages recorded: {len(customer_ages)}")
print(f"Schema columns: {data_columns}\n")


# ---------------------------------------------------------
# 2. INDEXING (ACCESSING SINGLE ELEMENTS)
# ---------------------------------------------------------
# Python is ZERO-INDEXED. The first element is always [0].

print("--- 2. INDEXING ---")
first_age = customer_ages[0]
third_age = customer_ages[2]

# Negative indexing pulls from the end of the dataset.
# -1 is the last item, -2 is the second to last, etc.
last_age = customer_ages[-1]

print(f"First Age: {first_age}")
print(f"Third Age: {third_age}")
print(f"Last Age: {last_age}\n")


# ---------------------------------------------------------
# 3. SLICING (EXTRACTING SUBSETS OF DATA)
# ---------------------------------------------------------
# Syntax: dataset[start:stop:step]
# The 'stop' index is EXCLUSIVE (it grabs up to, but not including, that index).

daily_revenue = [500, 650, 400, 800, 1200, 950, 1100]

print("--- 3. SLICING ---")

# Grab the first 3 days (indices 0, 1, 2)
# Notice we use 3 for the stop index. It excludes index 3.
first_three_days = daily_revenue[0:3] 
# Alternatively: daily_revenue[:3] (Python assumes 0 for start)
print(f"First 3 days of revenue: {first_three_days}")

# Grab everything from the 4th day onward (index 3 to end)
mid_week_onward = daily_revenue[3:]
print(f"Day 4 to end: {mid_week_onward}")

# Grab every second day (Step = 2)
every_other_day = daily_revenue[0:7:2]
# Alternatively: daily_revenue[::2]
print(f"Every other day: {every_other_day}")

# Trick to reverse a dataset sequence using slicing
reversed_revenue = daily_revenue[::-1]
print(f"Reversed data sequence: {reversed_revenue}\n")
