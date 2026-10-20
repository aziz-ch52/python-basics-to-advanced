"""
Core Concept: Input/Output (I/O) operations. 
A Data Analyst's first job is getting data out of storage and into a working environment.
"""

import pandas as pd
import os

# ==========================================
# SETUP: Creating dummy data for this script to work.
# In the real world, you are handed these files by a client or database export.
# ==========================================

sample_data = {
    'Transaction_ID': ['T100', 'T101', 'T102', 'T103'],
    'Date': ['2026-01-15', '2026-01-16', '2026-01-16', '2026-01-17'],
    'Revenue': [250.00, 15.50, 899.99, 120.00],
    'Store_Location': ['Vadodara', 'Mumbai', 'Delhi', 'Vadodara']
}
df_mock = pd.DataFrame(sample_data)

# ==========================================
# 1. WRITING DATA (Exporting)
# Saving your DataFrames to disk. 
# ==========================================

print("--- Exporting Data ---")

# Export to CSV (Comma Separated Values)
# index=False is crucial here. If you leave it as True (the default), 
# Pandas will write the row numbers (0, 1, 2...) as a new, unnamed column in your file.
csv_filename = 'raw_transactions.csv'
df_mock.to_csv(csv_filename, index=False)
print(f"Successfully wrote {csv_filename}")

# Export to Excel
# Requires 'openpyxl' engine installed in your environment (pip install openpyxl).
excel_filename = 'financial_report.xlsx'
df_mock.to_excel(excel_filename, sheet_name='Q1_Sales', index=False)
print(f"Successfully wrote {excel_filename}")
print("-" * 30)


# ==========================================
# 2. READING DATA (Ingestion)
# Loading data from disk into a Pandas DataFrame.
# ==========================================

print("\n--- Importing Data ---")

# Reading a CSV file
# This is the most common function you will use. 
df_from_csv = pd.read_csv(csv_filename)
print("Data loaded from CSV:")
print(df_from_csv)

# Reading an Excel file
# You can specify exactly which sheet you want to load.
df_from_excel = pd.read_excel(excel_filename, sheet_name='Q1_Sales')
print("\nData loaded from Excel:")
print(df_from_excel)
print("-" * 30)


# ==========================================
# 3. ADVANCED INGESTION LOGIC
# Real-world data is rarely clean. You often need to control how Pandas reads the file 
# right at the ingestion step to save memory and processing time later.
# ==========================================

print("\n--- Advanced Import Parameters ---")

# Scenario: You only need specific columns, and you want to use 'Transaction_ID' as the index.
# Why? Loading a 10GB CSV with 50 columns when you only need 3 will crash your machine.
# usecols: strict selection of required data.
# index_col: immediately sets the primary key, mapping directly to SQL logic.

df_optimized = pd.read_csv(
    csv_filename, 
    usecols=['Transaction_ID', 'Revenue', 'Store_Location'],
    index_col='Transaction_ID'
)

print("Optimized DataFrame (Filtered columns, explicit index):")
print(df_optimized)

# Notice how Transaction_ID is no longer a standard column, but the row label.
print(f"\nRevenue for T102: {df_optimized.loc['T102', 'Revenue']}")

# ==========================================
# TEARDOWN: Cleaning up the local directory
# ==========================================
if os.path.exists(csv_filename): os.remove(csv_filename)
if os.path.exists(excel_filename): os.remove(excel_filename)
