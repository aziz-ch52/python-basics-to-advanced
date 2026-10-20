"""
Core Concept: Profiling a new dataset.
Before you write complex logic, you must understand the shape, structure, and quality of your data. 
Running these commands is the mandatory first step every time you ingest a new file.
"""

import pandas as pd
import numpy as np

# ==========================================
# SETUP: Creating a mock e-commerce dataset.
# Notice the intentional inclusion of a NaN (missing) value and diverse data types.
# ==========================================

ecommerce_data = {
    'Order_ID': [1001, 1002, 1003, 1004, 1005, 1006],
    'Customer_Segment': ['Corporate', 'Consumer', 'Consumer', 'Corporate', 'Home Office', 'Consumer'],
    'Sales': [450.00, 120.50, np.nan, 890.00, 45.99, 120.50],
    'Quantity': [4, 1, 2, 8, 1, 1],
    'Is_Returned': [False, False, True, False, False, False]
}

df = pd.DataFrame(ecommerce_data)

# ==========================================
# 1. QUICK GLANCES
# Never print an entire DataFrame to the console if it has 50,000 rows.
# ==========================================

print("--- 1. Data Sampling ---")
# .head(n) returns the first n rows (default is 5). 
# Used to verify the file loaded correctly and headers are aligned.
print("First 3 rows:\n", df.head(3))

# .tail(n) returns the last n rows.
# Useful for checking if the end of a CSV file has junk data or aggregate totals.
print("\nLast 2 rows:\n", df.tail(2))

# .sample(n) returns n random rows.
# Critical for avoiding bias when inspecting sorted data.
print("\nRandom 2 rows:\n", df.sample(2))
print("-" * 40)


# ==========================================
# 2. STRUCTURAL INFORMATION
# This is the most important method in this file. 
# It tells you how dirty your data is before you start working.
# ==========================================

print("\n--- 2. DataFrame Info ---")
# .info() prints a concise summary: row counts, column names, non-null counts, and data types.
# Look at the 'Sales' column output: it will show 5 non-null values out of 6 rows. 
# That immediately tells you there is missing data you need to handle later.
df.info()
print("-" * 40)


# ==========================================
# 3. STATISTICAL SUMMARY
# Rapidly identifying outliers, impossible values, or general distribution.
# ==========================================

print("\n--- 3. Descriptive Statistics ---")
# .describe() automatically calculates count, mean, standard deviation, min, max, and quartiles 
# ONLY for numeric columns (int, float).
# If your 'Sales' max is $1,000,000 but the mean is $50, you instantly know you have an outlier.
print(df.describe())

# You can force it to describe categorical (object/string) data as well.
print("\nDescribing Categorical Data:")
print(df.describe(include=['object', 'bool']))
print("-" * 40)


# ==========================================
# 4. CATEGORICAL DISTRIBUTION
# This maps directly to the SQL query: 
# SELECT Customer_Segment, COUNT(*) FROM df GROUP BY Customer_Segment
# ==========================================

print("\n--- 4. Value Counts ---")
# .value_counts() counts the frequency of unique values in a specific column (Series).
# It returns the counts sorted in descending order by default.
segment_counts = df['Customer_Segment'].value_counts()

print("Count of orders by Customer Segment:")
print(segment_counts)

# You can also return this as a percentage (relative frequency) by passing normalize=True.
print("\nPercentage breakdown of Customer Segments:")
print(df['Customer_Segment'].value_counts(normalize=True) * 100)
