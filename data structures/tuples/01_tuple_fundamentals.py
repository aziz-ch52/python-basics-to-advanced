"""
=========================================================
01. TUPLE FUNDAMENTALS (IMMUTABLE DATA)
=========================================================
A tuple is an ordered, IMMUTABLE collection of items. 

Once a tuple is created, you cannot add, remove, or change 
its elements. In data pipelines, tuples are used to represent 
fixed records (like a row from a SQL database) or to return 
multiple calculated metrics from a function safely.
=========================================================
"""

# ---------------------------------------------------------
# 1. CREATION AND IMMUTABILITY
# ---------------------------------------------------------
print("--- 1. CREATION & IMMUTABILITY ---")

# Tuples use parentheses () instead of square brackets []
db_record = (1001, "John Doe", "Active", 450.75)

print(f"User Record: {db_record}")
print(f"Accessing data via index: {db_record[1]}") 

# ❌ THE ERROR THAT MAKES TUPLES VALUABLE:
# If you uncomment the line below, the script will crash.
# db_record[2] = "Inactive"  # TypeError: 'tuple' object does not support item assignment

print("State: Locked and secure. Cannot be mutated.\n")


# ---------------------------------------------------------
# 2. THE SINGLE ITEM TUPLE TRAP (COMMON MISTAKE)
# ---------------------------------------------------------
print("--- 2. THE SINGLE ITEM TRAP ---")

# If you need a tuple with only one item, you MUST include a trailing comma.
# Without the comma, Python just thinks you put a math expression inside parentheses.

fake_tuple = ("admin") 
real_tuple = ("admin",) 

print(f"Type without comma: {type(fake_tuple)}") # Outputs: <class 'str'>
print(f"Type with comma: {type(real_tuple)}\n")  # Outputs: <class 'tuple'>


# ---------------------------------------------------------
# 3. TUPLE UNPACKING (CRITICAL FOR DATA ANALYTICS)
# ---------------------------------------------------------
print("--- 3. TUPLE UNPACKING ---")
# This is how you extract variables quickly. You will use this constantly 
# when iterating over DataFrames (e.g., using iterrows()).

server_config = ("192.168.1.1", 8080, "Production")

# Unpacking assigns each item in the tuple to a distinct variable in one line
ip_address, port, environment = server_config

print(f"Connecting to {environment} at {ip_address}:{port}")

# Using the asterisk (*) to gather remaining items
financial_quarters = ("Q1", 15000, 18000, 22000, 25000)
quarter_name, *revenue_data = financial_quarters

print(f"Revenue array for {quarter_name}: {revenue_data}\n")


# ---------------------------------------------------------
# 4. BUILT-IN METHODS (ONLY TWO EXIST)
# ---------------------------------------------------------
print("--- 4. METHODS ---")
# Because they are immutable, there is no append, remove, pop, or sort.

login_attempts = (200, 403, 404, 200, 500, 200)

# count(x): Returns how many times an item appears
success_count = login_attempts.count(200)
print(f"Successful logins (200 OK): {success_count}")

# index(x): Returns the first zero-based index of the item
first_failure = login_attempts.index(403)
print(f"First forbidden error (403) occurred at index: {first_failure}\n")


# ---------------------------------------------------------
# 5. APPLIED SCENARIO: FUNCTION RETURNS
# ---------------------------------------------------------
print("--- 5. APPLIED SCENARIO: AGGREGATION ---")
# When you write a function to analyze data, you often need to return 
# more than one number. Python implicitly uses tuples to do this.

def analyze_traffic(traffic_list):
    total = sum(traffic_list)
    average = total / len(traffic_list)
    peak = max(traffic_list)
    
    # Returning multiple values creates a tuple automatically
    return total, average, peak

daily_visitors = [120, 150, 200, 110, 300]

# Call the function and unpack the resulting tuple immediately
total_visits, avg_visits, peak_visits = analyze_traffic(daily_visitors)

print(f"Total: {total_visits}, Average: {avg_visits}, Peak: {peak_visits}")
