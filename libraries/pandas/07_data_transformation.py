"""
Core Concept: Mutating and restructuring your dataset.
Raw data is rarely in the exact format you need for analysis or machine learning. 
This script covers the mechanics of creating calculated fields, cleaning up headers, 
and applying custom functions to your data.
"""

import pandas as pd

# ==========================================
# SETUP: A dataset with poor naming conventions and raw metrics.
# ==========================================
sales_data = {
    'product ID': ['P1', 'P2', 'P3', 'P4'],
    'base_price': [100.0, 250.0, 50.0, 800.0],
    'tax_rate': [0.05, 0.08, 0.05, 0.10],
    'Category': ['Office', 'Electronics', 'Office', 'Electronics']
}
df = pd.DataFrame(sales_data)

print("--- Original DataFrame ---")
print(df)
print("-" * 50)


# ==========================================
# 1. RENAMING COLUMNS
# Standardizing column headers is mandatory before loading data into a SQL database.
# Notice the space in 'product ID' - that will cause syntax errors in many downstream tools.
# ==========================================

print("\n--- 1. Renaming Columns ---")
# Use a dictionary to map { 'Old_Name' : 'New_Name' }
df_renamed = df.rename(columns={'product ID': 'Product_ID', 'base_price': 'Base_Price'})

print("Cleaned Headers:")
print(df_renamed)
print("-" * 50)


# ==========================================
# 2. CREATING NEW COLUMNS (Calculated Fields)
# This is basic vectorization. You perform math on entire columns at once, 
# exactly like dragging a formula down in an Excel column.
# ==========================================

print("\n--- 2. Creating Calculated Fields ---")

# Let's calculate the final price including tax.
# We create a new column on the fly by simply declaring it.
df_renamed['Tax_Amount'] = df_renamed['Base_Price'] * df_renamed['tax_rate']
df_renamed['Final_Price'] = df_renamed['Base_Price'] + df_renamed['Tax_Amount']

print("Added Tax_Amount and Final_Price columns:")
print(df_renamed)
print("-" * 50)


# ==========================================
# 3. DROPPING COLUMNS
# Get rid of data you don't need. It saves memory and removes clutter.
# ==========================================

print("\n--- 3. Dropping Columns ---")

# Use axis=1 to specify you are dropping a column (axis=0 is for rows).
# Let's drop the original tax_rate since we already calculated the final price.
df_lean = df_renamed.drop('tax_rate', axis=1)

print("Dropped 'tax_rate' column:")
print(df_lean)
print("-" * 50)


# ==========================================
# 4. APPLYING CUSTOM FUNCTIONS (.apply)
# When simple math isn't enough, you need custom logic.
# .apply() lets you run a custom Python function (or lambda) against every row or column.
# ==========================================

print("\n--- 4. Using .apply() for Custom Logic ---")

# Let's create a custom function that determines if a product is "Premium" or "Standard".
def categorize_price(price):
    if price > 300:
        return 'Premium'
    else:
        return 'Standard'

# We apply this function to the 'Final_Price' column to generate a new classification column.
df_lean['Price_Tier'] = df_lean['Final_Price'].apply(categorize_price)

print("Applied custom logic to create 'Price_Tier':")
print(df_lean[['Product_ID', 'Final_Price', 'Price_Tier']])

# Note on Performance: .apply() is essentially a Python for-loop under the hood. 
# It is slower than pure vectorized operations (like Step 2). 
# Always try to use built-in Pandas/NumPy math before resorting to .apply() on millions of rows.
