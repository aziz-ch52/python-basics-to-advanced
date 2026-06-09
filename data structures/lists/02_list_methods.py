"""
=========================================================
02. LIST METHODS (DATA MANIPULATION)
=========================================================
A definitive guide to the 11 built-in list methods.

In data pipelines, you will constantly need to append new 
records, drop bad rows, or sort values. Master these operations 
now so they are second nature when you move to Pandas.

CATEGORIES:
1. Adding Data (append, extend, insert)
2. Removing Data (remove, pop, clear)
3. Searching & Analyzing (index, count)
4. Reorganizing (sort, reverse)
5. Memory Management (copy)
=========================================================
"""

# ---------------------------------------------------------
# 1. ADDING DATA
# ---------------------------------------------------------
print("--- 1. ADDING DATA ---")

data_pipeline = ["extract", "clean"]

# append(x): Adds a SINGLE element to the end of the list.
data_pipeline.append("transform")
print(f"After append: {data_pipeline}") 

# extend(iterable): Flattens another sequence into the current list.
# CRITICAL: append() would add the list as a single nested element.
loading_steps = ["load_to_sql", "verify_tables"]
data_pipeline.extend(loading_steps)
print(f"After extend: {data_pipeline}") 

# insert(i, x): Inserts an element at a given index.
# WARNING: Inserting at index 0 on large datasets is computationally expensive.
data_pipeline.insert(0, "initialize_connection")
print(f"After insert: {data_pipeline}\n") 


# ---------------------------------------------------------
# 2. REMOVING DATA
# ---------------------------------------------------------
print("--- 2. REMOVING DATA ---")

http_status_codes = [200, 404, 500, 404, 403]

# remove(x): Removes the FIRST occurrence of a specific value. 
# Throws ValueError if the item does not exist.
http_status_codes.remove(404)
print(f"After remove(404): {http_status_codes}") 

# pop([i]): Removes and RETURNS the element at the given position. 
# Default is the last element (highly efficient).
last_code = http_status_codes.pop()
print(f"Popped value: {last_code} | Remaining: {http_status_codes}") 

# clear(): Wipes ALL items, leaving an empty list.
http_status_codes.clear()
print(f"After clear: {http_status_codes}\n") 


# ---------------------------------------------------------
# 3. SEARCHING & ANALYZING
# ---------------------------------------------------------
print("--- 3. SEARCHING & ANALYZING ---")

daily_active_users = [1200, 1500, 1200, 1800, 2000, 1200]

# count(x): Returns the number of times 'x' appears.
baseline_days = daily_active_users.count(1200)
print(f"Count of 1200 DAU: {baseline_days}") 

# index(x, [start], [end]): Returns zero-based index of the FIRST occurrence.
first_spike_index = daily_active_users.index(1800)
print(f"Index of 1800 DAU: {first_spike_index}\n") 


# ---------------------------------------------------------
# 4. REORGANIZING
# ---------------------------------------------------------
print("--- 4. REORGANIZING ---")

q1_revenue = [50000, 20000, 85000, 10000]

# sort(): Sorts the items IN-PLACE (modifies original list memory).
q1_revenue.sort()
print(f"Sorted (Ascending): {q1_revenue}") 

q1_revenue.sort(reverse=True)
print(f"Sorted (Descending): {q1_revenue}") 

# reverse(): Reverses the current order IN-PLACE. Does NOT sort.
months = ["Jan", "Feb", "Mar"]
months.reverse()
print(f"Reversed sequence: {months}\n") 


# ---------------------------------------------------------
# 5. MEMORY MANAGEMENT (CRITICAL)
# ---------------------------------------------------------
print("--- 5. MEMORY MANAGEMENT ---")

raw_dataset = [10.5, 11.2, 10.8]

# copy(): Returns a shallow copy.
# If you just do `backup = raw_dataset`, both variables point to the same memory.
# Modifying one will silently corrupt the other. Always use .copy().
clean_dataset = raw_dataset.copy()

# Proving they are independent:
clean_dataset.clear()
print(f"Raw dataset intact: {raw_dataset}") 
print(f"Clean dataset wiped: {clean_dataset}")
