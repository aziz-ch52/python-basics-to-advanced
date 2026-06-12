"""
=========================================================
02. TUPLE UNPACKING (DATA EXTRACTION)
=========================================================
Unpacking allows you to assign the individual elements of a 
tuple to distinct variables in a single, clean line of code.
=========================================================
"""

# ---------------------------------------------------------
# 1. STANDARD UNPACKING
# ---------------------------------------------------------
print("--- 1. STANDARD UNPACKING ---")

# A simulated database row
db_row = ("alice_smith", "admin", "active")

# Extracting all three values simultaneously
username, role, status = db_row

print(f"User: {username} | Role: {role} | Status: {status}")


# ---------------------------------------------------------
# 2. GATHERING REMAINING ITEMS (THE ASTERISK *)
# ---------------------------------------------------------
print("\n--- 2. GATHERING DATA (*) ---")
# When you only care about the first few items, you can pack 
# the rest into a list using an asterisk.

financial_quarters = ("Q1_2026", 15000, 18000, 22000, 25000)

# Extract the label, and dump the numbers into an array
quarter_label, *revenue_data = financial_quarters

print(f"Quarter: {quarter_label}")
print(f"Revenue Array: {revenue_data}")


# ---------------------------------------------------------
# 3. RETURNING MULTIPLE VALUES FROM FUNCTIONS
# ---------------------------------------------------------
print("\n--- 3. FUNCTION RETURNS ---")
# Python implicitly uses tuples when returning multiple values.

def extract_metrics(data_list):
    """Simulates basic metric extraction."""
    return min(data_list), max(data_list), sum(data_list)

daily_sales = [100, 250, 50, 400, 300]

# Unpacking the returned tuple immediately
lowest, highest, total = extract_metrics(daily_sales)

print(f"Lowest: {lowest}, Highest: {highest}, Total: {total}")
