"""
=========================================================
03. LIST COMPREHENSIONS (DATA TRANSFORMATIONS)
=========================================================
List comprehensions provide a concise, optimized way to 
create new lists based on existing ones.

For data processing, this is your primary tool for cleaning 
and transforming 1D arrays of data without writing bloated, 
slow 'for' loops.

SYNTAX:
[expression for item in iterable if condition]
=========================================================
"""

# ---------------------------------------------------------
# 1. BASIC TRANSFORMATION (MATH OPERATIONS)
# ---------------------------------------------------------
print("--- 1. BASIC TRANSFORMATION ---")

# Scenario: You have a list of prices in USD and need them in EUR (1 USD = 0.92 EUR)
usd_prices = [100, 250, 400, 50]

# ❌ The Rookie Way (Slow and bloated):
# eur_prices = []
# for price in usd_prices:
#     eur_prices.append(price * 0.92)

# ✅ The Professional Way (Comprehension):
eur_prices = [price * 0.92 for price in usd_prices]

print(f"USD: {usd_prices}")
print(f"EUR: {eur_prices}\n")


# ---------------------------------------------------------
# 2. FILTERING DATA (THE 'IF' CLAUSE)
# ---------------------------------------------------------
print("--- 2. FILTERING DATA ---")

# Scenario: Extract only valid, positive ages from a messy dataset
raw_ages = [25, -99, 30, 45, -1, 22]

# Keep the age ONLY IF it is greater than 0
valid_ages = [age for age in raw_ages if age > 0]

print(f"Raw data: {raw_ages}")
print(f"Cleaned ages: {valid_ages}\n")


# ---------------------------------------------------------
# 3. CONDITIONAL REPLACEMENT (IF / ELSE)
# ---------------------------------------------------------
print("--- 3. DATA IMPUTATION (IF/ELSE) ---")
# Note: When using if/else, the syntax order changes slightly:
# [value_if_true if condition else value_if_false for item in iterable]

# Scenario: Replace error codes (-999) with 0 (imputation)
sensor_data = [15, 20, -999, 18, 22, -999]

# Read it like English: "Keep the value if it's not -999, else make it 0"
cleaned_sensor = [val if val != -999 else 0 for val in sensor_data]

print(f"Original sensor data: {sensor_data}")
print(f"Imputed sensor data: {cleaned_sensor}\n")


# ---------------------------------------------------------
# 4. STRING CLEANING 
# ---------------------------------------------------------
print("--- 4. STRING CLEANING ---")

# Scenario: You scraped a list of categories, but they have weird whitespace and casing.
raw_categories = ["   electronics ", "APPAREL  ", "  Home & Garden"]

# Strip whitespace and convert to lowercase in one move
standardized_categories = [cat.strip().lower() for cat in raw_categories]

print(f"Standardized Categories: {standardized_categories}\n")
