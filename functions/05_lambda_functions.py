"""
=========================================================
05. LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
=========================================================
Lambdas are small, anonymous, single-line functions. 

You will use these constantly in data engineering when you 
need to quickly clean or transform a column of data without 
writing a full, multi-line 'def' block.

Syntax: lambda arguments : expression
=========================================================
"""

# ---------------------------------------------------------
# 1. BASIC LAMBDA SYNTAX
# ---------------------------------------------------------
print("--- 1. BASIC LAMBDA ---")

# Standard def function
def add_ten(x):
    return x + 10

# Equivalent Lambda function
lambda_add_ten = lambda x: x + 10

print(f"Standard function output: {add_ten(5)}")
print(f"Lambda function output: {lambda_add_ten(5)}")


# ---------------------------------------------------------
# 2. DATA TRANSFORMATION (WITH MAP)
# ---------------------------------------------------------
print("\n--- 2. BATCH TRANSFORMATIONS (map) ---")
# 'map' applies a function to every item in an iterable.

raw_prices = [10, 25, 50, 100]

# Add a 5% tax to every item in the list instantly
taxed_prices = list(map(lambda price: price * 1.05, raw_prices))

print(f"Raw prices: {raw_prices}")
print(f"Taxed prices: {taxed_prices}")


# ---------------------------------------------------------
# 3. DATA FILTERING (WITH FILTER)
# ---------------------------------------------------------
print("\n--- 3. DATA CLEANING (filter) ---")
# 'filter' extracts elements from an iterable where the lambda evaluates to True.

# A dataset mixed with valid numbers and missing data (-1)
sensor_readings = [85, -1, 90, 78, -1, 92]

# Keep only the valid readings
clean_readings = list(filter(lambda x: x != -1, sensor_readings))

print(f"Raw readings: {sensor_readings}")
print(f"Cleaned readings: {clean_readings}")
