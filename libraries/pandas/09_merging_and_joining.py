"""
Core Concept: Combining relational datasets.
This is where your SQL background pays off. If you understand INNER JOIN, LEFT JOIN, 
and UNION, you already know how to merge in Pandas. 
Real data never lives in a single flat file; it is distributed across multiple tables.
"""

import pandas as pd

# ==========================================
# SETUP: Creating two relational tables.
# Notice that EMP04 has a Dept_ID (D99) that doesn't exist in the departments table.
# Notice that D04 (Marketing) has no employees assigned to it.
# ==========================================

employees = pd.DataFrame({
    'Emp_ID': ['EMP01', 'EMP02', 'EMP03', 'EMP04'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Dept_ID': ['D01', 'D02', 'D01', 'D99'] 
})

departments = pd.DataFrame({
    'Dept_ID': ['D01', 'D02', 'D03', 'D04'],
    'Dept_Name': ['Engineering', 'Sales', 'HR', 'Marketing']
})

print("--- Table 1: Employees ---")
print(employees)
print("\n--- Table 2: Departments ---")
print(departments)
print("-" * 50)


# ==========================================
# 1. INNER JOIN (The Default Merge)
# pd.merge() defaults to an inner join. 
# It only keeps rows where the matching key ('Dept_ID') exists in BOTH tables.
# ==========================================

print("\n--- 1. Inner Merge (Intersection) ---")
# SQL Equivalent: 
# SELECT * FROM employees INNER JOIN departments ON employees.Dept_ID = departments.Dept_ID

inner_merge = pd.merge(employees, departments, on='Dept_ID', how='inner')

# David (EMP04) is gone because D99 doesn't exist in departments.
# Marketing (D04) is gone because no employee has that ID.
print(inner_merge)
print("-" * 50)


# ==========================================
# 2. LEFT JOIN 
# Keeps ALL rows from the left table (employees), regardless of whether there is a match.
# If there is no match in the right table, Pandas fills the missing data with NaN.
# ==========================================

print("\n--- 2. Left Merge ---")
# SQL Equivalent: 
# SELECT * FROM employees LEFT JOIN departments ON employees.Dept_ID = departments.Dept_ID

left_merge = pd.merge(employees, departments, on='Dept_ID', how='left')

# David is back. But since D99 doesn't map to a department name, Dept_Name is NaN.
# This is how you identify broken relational links in dirty data.
print(left_merge)
print("-" * 50)


# ==========================================
# 3. RIGHT AND OUTER JOINS
# ==========================================

print("\n--- 3. Outer Merge (Full Union) ---")
# how='outer' keeps everything from both tables. 
# It is the equivalent of a FULL OUTER JOIN in SQL.

outer_merge = pd.merge(employees, departments, on='Dept_ID', how='outer')
print(outer_merge)
print("-" * 50)


# ==========================================
# 4. CONCATENATION (Stacking Data)
# pd.concat() is used when you have two tables with the exact same columns and you 
# just want to stack them vertically.
# SQL Equivalent: UNION ALL
# ==========================================

print("\n--- 4. Concatenation (Vertical Stacking) ---")

new_hires = pd.DataFrame({
    'Emp_ID': ['EMP05', 'EMP06'],
    'Name': ['Eve', 'Frank'],
    'Dept_ID': ['D03', 'D01']
})

# Pass the DataFrames as a list.
# ignore_index=True forces Pandas to create a clean, new 0-indexed row structure.
all_employees = pd.concat([employees, new_hires], ignore_index=True)

print(all_employees)
