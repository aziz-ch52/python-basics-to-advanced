"""
Core Concept: Dimensional reshaping of tabular data.
You already know how to build a Pivot Table in Excel to summarize data. 
This script executes that exact same logic programmatically. It also covers 'melting' 
(unpivoting), which is mandatory when preparing wide data for ingestion into dashboards like Power BI.
"""

import pandas as pd
import numpy as np

# ==========================================
# SETUP: Creating a standard transactional dataset.
# ==========================================
sales_data = {
    'Date': ['2026-01-01', '2026-01-01', '2026-01-02', '2026-01-02', '2026-01-01', '2026-01-02'],
    'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'Product': ['Laptop', 'Laptop', 'Tablet', 'Tablet', 'Tablet', 'Laptop'],
    'Revenue': [1200, 1200, 450, 450, 600, 1500],
    'Units': [1, 1, 2, 2, 3, 2]
}
df = pd.DataFrame(sales_data)

print("--- Raw Transaction Data (Long Format) ---")
print(df)
print("-" * 60)


# ==========================================
# 1. PIVOT TABLES (.pivot_table)
# Just like Excel: You define your Rows (index), Columns (columns), and Values (values).
# ==========================================

print("\n--- 1. Basic Pivot Table (Total Revenue by Region & Product) ---")

# By default, pivot_table calculates the MEAN. We want the SUM, so we pass aggfunc='sum' (or np.sum).
pivot_revenue = pd.pivot_table(
    df, 
    values='Revenue', 
    index='Region',       # These become your row labels
    columns='Product',    # These become your column headers
    aggfunc='sum',
    fill_value=0          # Replaces NaN with 0 if a Region didn't sell a specific Product
)

print(pivot_revenue)
print("-" * 60)

print("\n--- 2. Advanced Pivot Table (Multiple Metrics) ---")
# You can analyze multiple values and apply different aggregations simultaneously.

advanced_pivot = pd.pivot_table(
    df,
    index=['Region', 'Date'],  # Multi-level rows
    values=['Revenue', 'Units'],
    aggfunc={'Revenue': 'sum', 'Units': 'mean'} # Sum the money, average the units
)

print(advanced_pivot)
print("-" * 60)


# ==========================================
# 3. MELTING DATA (Unpivoting)
# This is the exact opposite of a pivot table. 
# It transforms "Wide" data (many columns) into "Long" data (few columns, many rows).
# BI tools and relational databases require data in a Long format.
# ==========================================

print("\n--- 3. Melting Data (Wide to Long Format) ---")

# Let's create a 'Wide' dataset that looks like a typical financial report
wide_data = pd.DataFrame({
    'Metric': ['Revenue', 'Profit'],
    'Q1_2026': [50000, 12000],
    'Q2_2026': [55000, 14000],
    'Q3_2026': [60000, 15500]
})

print("Wide Format (Hard to query or put in a database):")
print(wide_data)

# We want to 'melt' the quarters into a single column so we can group or filter by Date.
# id_vars: The column(s) to keep as the anchor (identifier).
# var_name: The name for the new column holding the old headers.
# value_name: The name for the new column holding the numbers.

long_data = pd.melt(
    wide_data,
    id_vars=['Metric'],
    var_name='Quarter',
    value_name='Amount'
)

print("\nLong Format (Normalized, ready for SQL or Power BI):")
print(long_data.sort_values(by=['Metric', 'Quarter']))
