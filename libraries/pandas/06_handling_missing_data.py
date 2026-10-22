"""
Core Concept: Dealing with dirty data.
Real-world data is never perfect. You will encounter blanks, nulls, and NaNs constantly. 
How you handle missing data separates good analysts from amateurs. If you just blindly 
drop every row with a missing value, you might destroy half your dataset and ruin your analysis.
"""

import pandas as pd
import numpy as np

# ==========================================
# SETUP: Creating a notoriously dirty dataset.
# np.nan is the standard representation of missing numeric data in Pandas.
# ==========================================
messy_data = {
    'Invoice_ID': ['INV-01', 'INV-02', 'INV-03', 'INV-04', 'INV-05', 'INV-06'],
    'Client': ['Alpha Co', 'Beta LLC', np.nan, 'Delta Inc', 'Echo Corp', 'Foxtrot'],
    'Amount': [1500.0, np.nan, 3200.5, 450.0, np.nan, 890.0],
    'Status': ['Paid', 'Pending', 'Paid', np.nan, 'Pending', 'Paid']
}
df = pd.DataFrame(messy_data)

print("--- The Dirty DataFrame ---")
print(df)
print("-" * 50)


# ==========================================
# 1. IDENTIFYING MISSING DATA
# You cannot fix what you haven't found. 
# ==========================================

print("\n--- 1. Locating the Gaps ---")
# .isna() (or .isnull()) returns a DataFrame of booleans. True means the data is missing.
print("Boolean map of missing values:\n", df.isna())

# Summing the missing values per column is the fastest way to profile the damage.
# True evaluates to 1, False to 0. So .sum() counts the blanks.
print("\nTotal missing values per column:")
print(df.isna().sum())
print("-" * 50)


# ==========================================
# 2. DROPPING MISSING DATA (The Nuclear Option)
# Use .dropna() carefully. 
# ==========================================

print("\n--- 2. Dropping Rows (.dropna) ---")

# Default behavior: Drops ANY row that contains AT LEAST ONE missing value.
# Look at the output: we lose 4 out of 6 rows. This is usually a terrible idea.
df_dropped_any = df.dropna()
print("Dropped rows with ANY missing data:\n", df_dropped_any)

# A smarter approach: Only drop a row if a CRITICAL column is missing.
# Example: If we don't know the Client, the invoice is useless to us.
df_dropped_subset = df.dropna(subset=['Client'])
print("\nDropped only if 'Client' is missing:\n", df_dropped_subset)
print("-" * 50)


# ==========================================
# 3. FILLING MISSING DATA (Imputation)
# This is usually the better route. You replace NaNs with logical defaults.
# ==========================================

print("\n--- 3. Filling Gaps (.fillna) ---")

# Strategy A: Hardcoded Default Values
# Let's assume missing statuses are just 'Pending'.
df_filled_status = df.copy()
df_filled_status['Status'] = df_filled_status['Status'].fillna('Pending')
print("Filled missing Status with 'Pending':\n", df_filled_status[['Invoice_ID', 'Status']])

# Strategy B: Mathematical Imputation (Mean/Median)
# For numerical data like 'Amount', filling with the average of the valid data is common.
average_amount = df['Amount'].mean()
df_filled_amount = df.copy()
df_filled_amount['Amount'] = df_filled_amount['Amount'].fillna(average_amount)

print(f"\nFilled missing Amount with mean ({average_amount:.2f}):")
print(df_filled_amount[['Invoice_ID', 'Amount']])
print("-" * 50)

# ==========================================
# 4. FORWARD FILL AND BACKWARD FILL
# Critical for Time Series Data (e.g., Stock prices, daily temperature).
# If Tuesday's data is missing, just carry over Monday's data.
# ==========================================

print("\n--- 4. Forward Fill (ffill) ---")
# ffill() propagates the last valid observation forward.
# Notice how INV-02's missing amount is filled by INV-01's amount (1500.0).
df_ffill = df.ffill()
print(df_ffill)
