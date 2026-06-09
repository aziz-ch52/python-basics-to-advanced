"""
=========================================================
04. APPLIED LISTS (DATA CLEANING PIPELINE)
=========================================================
Syntax is useless if you can't apply it. 

This script simulates a real-world scenario where you extract
a messy column of transaction amounts from a database, clean 
out the garbage, and calculate a baseline metric.

This is the exact logical flow you will use later with heavy
analytics libraries, just done with foundational Python.
=========================================================
"""

# ---------------------------------------------------------
# 1. THE RAW DATA
# ---------------------------------------------------------
# Imagine this was scraped from a broken payment gateway.
# It contains duplicates, system errors, missing data (None), and invalid negative charges.
raw_transactions = [150.50, "ERROR", 200.00, -99.00, None, 450.75, 150.50, "TIMEOUT", 300.00, -50.00, 200.00]

print("--- RAW DATA ---")
print(f"Initial record count: {len(raw_transactions)}\n")


# ---------------------------------------------------------
# 2. REMOVING KNOWN FATAL ERRORS (List Methods)
# ---------------------------------------------------------
# If we know specific string flags are in there, we can pull them out.
if "ERROR" in raw_transactions:
    raw_transactions.remove("ERROR")
if "TIMEOUT" in raw_transactions:
    raw_transactions.remove("TIMEOUT")


# ---------------------------------------------------------
# 3. FILTERING AND TYPE VALIDATION (List Comprehension)
# ---------------------------------------------------------
# Drop the 'None' values and ensure everything left is a valid number greater than 0.
# This single line of code replaces about 6 lines of standard 'for' loop bloat.
valid_transactions = [
    float(amount) for amount in raw_transactions 
    if amount is not None and isinstance(amount, (int, float)) and amount > 0
]


# ---------------------------------------------------------
# 4. DEDUPLICATION 
# ---------------------------------------------------------
# Lists don't handle deduplication well natively. The standard professional 
# workaround is converting the list to a Set (which destroys duplicates), 
# and then casting it back to a List.
unique_transactions = list(set(valid_transactions))


# ---------------------------------------------------------
# 5. SORTING FOR ANALYSIS (List Methods)
# ---------------------------------------------------------
# Sort ascending to easily identify our lowest and highest valid transactions.
unique_transactions.sort()


# ---------------------------------------------------------
# 6. SLICING OUTLIERS 
# ---------------------------------------------------------
# Business logic dictates we drop the absolute highest and lowest transactions 
# to avoid skewing our average. We slice from index 1 to -1 (excluding the ends).
trimmed_transactions = unique_transactions[1:-1]


# ---------------------------------------------------------
# 7. FINAL METRIC CALCULATION
# ---------------------------------------------------------
total_revenue = sum(trimmed_transactions)
average_transaction = total_revenue / len(trimmed_transactions)

print("--- PIPELINE RESULTS ---")
print(f"Cleaned & Trimmed Data: {trimmed_transactions}")
print(f"Final Valid Record Count: {len(trimmed_transactions)}")
print(f"Average Transaction Value: ${average_transaction:.2f}")
