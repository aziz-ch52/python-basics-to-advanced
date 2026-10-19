"""
Core Concept: Understanding the two primary data structures in Pandas.
"""

import pandas as pd
import numpy as np

# ==========================================
# 1. PANDAS SERIES: The 1D Building Block
# Think of a Series as a single column in an Excel spreadsheet or an SQL table.
# It contains data arrays (built on NumPy) and an explicit index (row labels).
# ==========================================

# Creating a Series from a standard Python list
# If you don't specify an index, Pandas automatically assigns integers starting from 0.
sales_figures = [150, 200, 350, 90]
sales_series = pd.Series(sales_figures)

print("--- Default Series (Integer Index) ---")
print(sales_series)
print("-" * 30)

# Creating a Series with a custom index
# This applies first-principles logic: mapping specific identifiers directly to values, similar to a dictionary.
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
daily_sales = pd.Series(data=sales_figures, index=days)

print("\n--- Series with Custom Index ---")
print(daily_sales)
# You can now retrieve data using the exact label rather than just a numeric position
print(f"Sales on Wednesday: {daily_sales['Wednesday']}")
print("-" * 30)


# ==========================================
# 2. PANDAS DATAFRAME: The 2D Tabular Structure
# Think of a DataFrame as a complete relational database table.
# Under the hood, it is essentially a dictionary of Series objects sharing the same index.
# ==========================================

# Creating a DataFrame from a dictionary of lists.
# The keys become the column headers, and the lists populate the rows.
# Ensure all lists are exactly the same length, or Pandas will throw an error.
inventory_data = {
    'Product_ID': [101, 102, 103, 104],
    'Product_Name': ['Laptop', 'Smartphone', 'Earbuds', 'Tablet'],
    'Category': ['Hardware', 'Hardware', 'Accessories', 'Hardware'],
    'Price_USD': [999.00, 450.50, 120.00, 850.00],
    'Stock_Quantity': [15, 42, 0, 8]
}

df_inventory = pd.DataFrame(inventory_data)

print("\n--- Core DataFrame ---")
print(df_inventory)
print("-" * 30)

# Creating a DataFrame from a list of dictionaries (Row-by-Row construction)
# This is highly relevant when parsing JSON data from APIs.
api_response_data = [
    {'User_ID': 1, 'Action': 'Login', 'Timestamp': '08:00'},
    {'User_ID': 2, 'Action': 'Click', 'Timestamp': '08:05'},
    {'User_ID': 1, 'Action': 'Logout', 'Timestamp': '08:45'}
]

df_logs = pd.DataFrame(api_response_data)

print("\n--- DataFrame from Row Data (JSON-style) ---")
print(df_logs)
print("-" * 30)


# ==========================================
# 3. ANATOMY OF A DATAFRAME
# Before applying any logic or transformations, inspect the structure.
# ==========================================

print("\n--- Inspecting DataFrame Anatomy ---")
# .shape returns a tuple (rows, columns) - identical to NumPy matrices
print(f"Shape (Rows, Columns): {df_inventory.shape}") 

# .columns returns the list of column headers
print(f"Columns: {list(df_inventory.columns)}")

# .dtypes returns the data type of each column (int64, float64, object/string)
print(f"\nData Types:\n{df_inventory.dtypes}")
