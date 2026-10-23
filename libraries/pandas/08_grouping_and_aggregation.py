"""
Core Concept: Summarizing data by categories.
This is the exact Pandas equivalent of the SQL GROUP BY statement. 
It follows the "Split-Apply-Combine" strategy: split the data into groups based on a key, 
apply a mathematical function (sum, mean, count), and combine the results into a new summary table.
"""

import pandas as pd

# ==========================================
# SETUP: A transactional dataset with categories.
# We have multiple sales records for different regions and departments.
# ==========================================
sales_data = {
    'Region': ['North', 'South', 'North', 'East', 'South', 'East', 'North'],
    'Department': ['Electronics', 'Clothing', 'Clothing', 'Electronics', 'Electronics', 'Clothing', 'Electronics'],
    'Sales_Rep': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Revenue': [1500, 800, 1200, 2000, 1750, 900, 2200],
    'Units_Sold': [15, 40, 60, 20, 18, 45, 22]
}
df = pd.DataFrame(sales_data)

print("--- Raw Transaction Data ---")
print(df)
print("-" * 50)


# ==========================================
# 1. BASIC GROUPING & AGGREGATION
# SQL Equivalent: SELECT Region, SUM(Revenue) FROM df GROUP BY Region
# ==========================================

print("\n--- 1. Simple Aggregation (Sum by Region) ---")

# Step 1: Specify the column to group by.
# Step 2: Specify the column you want to do math on.
# Step 3: Specify the mathematical operation (.sum(), .mean(), .max(), .count())
region_sales = df.groupby('Region')['Revenue'].sum()

print(region_sales)
# Notice that the output is a Series where the 'Region' has become the index.
print("-" * 50)


# ==========================================
# 2. AGGREGATING MULTIPLE COLUMNS AT ONCE
# ==========================================

print("\n--- 2. Multi-Column Aggregation (Mean by Department) ---")

# If you don't isolate a specific numeric column, Pandas will try to calculate the mean 
# for ALL numeric columns in the DataFrame.
dept_averages = df.groupby('Department')[['Revenue', 'Units_Sold']].mean()

print(dept_averages)
print("-" * 50)


# ==========================================
# 3. GROUPING BY MULTIPLE CATEGORIES
# SQL Equivalent: SELECT Region, Department, SUM(Revenue) FROM df GROUP BY Region, Department
# ==========================================

print("\n--- 3. Multi-Level Grouping ---")

# Pass a list of columns to groupby() to create a hierarchical index (MultiIndex).
region_dept_summary = df.groupby(['Region', 'Department'])['Revenue'].sum()

print("Revenue grouped by Region, then Department:")
print(region_dept_summary)

# To flatten this back into a standard DataFrame (which is often easier for exporting), 
# use .reset_index()
print("\nFlattened back to standard DataFrame:")
print(region_dept_summary.reset_index())
print("-" * 50)


# ==========================================
# 4. ADVANCED AGGREGATION (.agg)
# What if you want the SUM of Revenue, but the AVERAGE of Units_Sold?
# The .agg() method lets you apply different math functions to different columns simultaneously.
# ==========================================

print("\n--- 4. Custom Aggregation with .agg() ---")

custom_summary = df.groupby('Region').agg({
    'Revenue': ['sum', 'max'],          # Calculate both Total and Highest single sale
    'Units_Sold': 'mean',               # Calculate Average units
    'Sales_Rep': 'count'                # Count the number of sales reps in the region
})

print("Complex Summary Data:")
print(custom_summary)
