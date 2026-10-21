"""
Core Concept: Precision data extraction.
Extracting specific columns and rows using dictionary-style bracket notation, .iloc[] (position), and .loc[] (label).
If you don't master .loc and .iloc, you will constantly overwrite the wrong data and trigger the SettingWithCopyWarning.
"""

import pandas as pd

# ==========================================
# SETUP: Creating a DataFrame with a custom text index.
# Using a custom index makes the difference between .iloc (number) and .loc (name) obvious.
# ==========================================
employee_data = {
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
    'Salary': [85000, 62000, 95000, 78000, 68000],
    'Years_Experience': [5, 2, 8, 3, 4]
}
# Setting Employee IDs as the explicit row labels (index)
df = pd.DataFrame(employee_data, index=['EMP01', 'EMP02', 'EMP03', 'EMP04', 'EMP05'])

print("--- Base DataFrame ---")
print(df)
print("-" * 40)


# ==========================================
# 1. SELECTING COLUMNS (Dictionary-style)
# This is how you extract entire vertical columns from the dataset.
# ==========================================

print("\n--- 1. Selecting Columns ---")
# Extracting a single column returns a Pandas Series.
# Syntax: df['ColumnName']
salaries = df['Salary']
print("Single Column (Series):\n", salaries.head(2))

# Extracting multiple columns returns a new DataFrame.
# Syntax: df[['Col1', 'Col2']] -> Notice the double brackets! You are passing a list of column names.
subset_df = df[['Department', 'Years_Experience']]
print("\nMultiple Columns (DataFrame):\n", subset_df.head(2))
print("-" * 40)


# ==========================================
# 2. SELECTION BY POSITION: .iloc[]
# "iloc" stands for Integer Location. 
# It operates strictly on the 0-indexed position of rows and columns, just like standard Python lists or NumPy arrays.
# Syntax: df.iloc[row_position, column_position]
# ==========================================

print("\n--- 2. Position-Based Selection (.iloc) ---")

# Extract the very first row (index 0)
print("First row:\n", df.iloc[0])

# Extract the first three rows (0, 1, 2) and the first two columns (0, 1)
# Remember standard Python slicing: the end bound is EXCLUSIVE.
print("\nFirst 3 rows, first 2 columns:\n", df.iloc[0:3, 0:2])

# Extract specific disconnected rows (1st and 4th) and a specific column (2nd)
print("\nSpecific rows and column:\n", df.iloc[[0, 3], 1])
print("-" * 40)


# ==========================================
# 3. SELECTION BY LABEL: .loc[]
# "loc" stands for Location. 
# It operates on the explicit labels of the index and columns.
# Syntax: df.loc[row_label, column_label]
# ==========================================

print("\n--- 3. Label-Based Selection (.loc) ---")

# Extract a single row by its explicit index label
print("Data for EMP03:\n", df.loc['EMP03'])

# Extract a range of rows by label.
# CRITICAL DIFFERENCE FROM .iloc: When slicing with .loc, the end bound is INCLUSIVE.
print("\nData from EMP02 to EMP04:\n", df.loc['EMP02':'EMP04'])

# Extract specific rows and specific columns by name.
# This is the safest, most readable way to extract precise data points.
print("\nDepartment and Salary for EMP01 and EMP05:\n", df.loc[['EMP01', 'EMP05'], ['Department', 'Salary']])
