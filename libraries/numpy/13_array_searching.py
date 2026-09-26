"""
============================================================
13 - NumPy Array Searching
============================================================

Topic:
    Array Searching in NumPy

Functions Covered:
    1. np.where()
    2. np.argwhere()
    3. np.searchsorted()
    4. np.argmax()
    5. np.argmin()

Purpose:
    This file demonstrates how to search, locate, and analyze
    values inside NumPy arrays.

Requirements:
    pip install numpy

Author:
    Aziz

============================================================
"""

import numpy as np


# ============================================================
# 1. np.where()
# ============================================================

print("=" * 60)
print("1. np.where()")
print("=" * 60)

numbers = np.array([10, 20, 30, 40, 50])

print("Original array:")
print(numbers)

# Find the indices where values are greater than 30
indices = np.where(numbers > 30)

print("\nIndices where values are greater than 30:")
print(indices)

# Extract the actual values
matching_values = numbers[numbers > 30]

print("\nValues greater than 30:")
print(matching_values)


# ------------------------------------------------------------
# np.where() with multiple conditions
# ------------------------------------------------------------

numbers = np.array([10, 20, 30, 40, 50, 60])

indices = np.where((numbers >= 20) & (numbers <= 50))

print("\nIndices of values between 20 and 50:")
print(indices)

print("\nValues between 20 and 50:")
print(numbers[indices])


# ------------------------------------------------------------
# np.where() for conditional replacement
# ------------------------------------------------------------

marks = np.array([35, 72, 48, 91, 64, 28])

result = np.where(marks >= 50, "Pass", "Fail")

print("\nMarks:")
print(marks)

print("\nPass/Fail classification:")
print(result)


# ------------------------------------------------------------
# Real-world example: Sales classification
# ------------------------------------------------------------

sales = np.array([1200, 4500, 800, 6700, 3200, 1500])

sales_category = np.where(
    sales >= 3000,
    "High Sales",
    "Low Sales"
)

print("\nSales:")
print(sales)

print("\nSales classification:")
print(sales_category)


# ============================================================
# 2. np.argwhere()
# ============================================================

print("\n" + "=" * 60)
print("2. np.argwhere()")
print("=" * 60)

numbers = np.array([10, 20, 30, 40, 50])

print("Original array:")
print(numbers)

# Find positions where values are greater than 30
positions = np.argwhere(numbers > 30)

print("\nPositions where values are greater than 30:")
print(positions)


# ------------------------------------------------------------
# argwhere() with a 2D array
# ------------------------------------------------------------

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2D array:")
print(matrix)

positions = np.argwhere(matrix > 50)

print("\nPositions where values are greater than 50:")
print(positions)


# Display each coordinate and corresponding value
print("\nMatching coordinates and values:")

for row, column in positions:
    print(
        f"Position: ({row}, {column}) "
        f"Value: {matrix[row, column]}"
    )


# ============================================================
# 3. np.searchsorted()
# ============================================================

print("\n" + "=" * 60)
print("3. np.searchsorted()")
print("=" * 60)

# searchsorted() works with a sorted array
numbers = np.array([10, 20, 30, 40, 50])

print("Sorted array:")
print(numbers)

# Find where 35 should be inserted
position = np.searchsorted(numbers, 35)

print("\nPosition where 35 should be inserted:")
print(position)

# Demonstrate insertion concept
new_array = np.insert(numbers, position, 35)

print("\nArray after inserting 35:")
print(new_array)


# ------------------------------------------------------------
# Search for multiple values
# ------------------------------------------------------------

values = np.array([15, 25, 45])

positions = np.searchsorted(numbers, values)

print("\nValues to search:")
print(values)

print("\nInsertion positions:")
print(positions)


# ------------------------------------------------------------
# searchsorted() with side parameter
# ------------------------------------------------------------

numbers = np.array([10, 20, 20, 20, 30, 40])

print("\nArray with duplicate values:")
print(numbers)

left_position = np.searchsorted(
    numbers,
    20,
    side="left"
)

right_position = np.searchsorted(
    numbers,
    20,
    side="right"
)

print("\nLeft insertion position for 20:")
print(left_position)

print("\nRight insertion position for 20:")
print(right_position)


# ============================================================
# 4. np.argmax()
# ============================================================

print("\n" + "=" * 60)
print("4. np.argmax()")
print("=" * 60)

numbers = np.array([10, 50, 30, 90, 20])

print("Array:")
print(numbers)

# Find index of maximum value
max_index = np.argmax(numbers)

print("\nIndex of maximum value:")
print(max_index)

# Get maximum value using the index
max_value = numbers[max_index]

print("\nMaximum value:")
print(max_value)


# ------------------------------------------------------------
# Real-world example: Find highest sales
# ------------------------------------------------------------

sales = np.array([
    12000,
    18000,
    15000,
    25000,
    21000
])

max_sales_index = np.argmax(sales)

print("\nSales:")
print(sales)

print("\nHighest sales:")
print(sales[max_sales_index])

print("\nIndex of highest sales:")
print(max_sales_index)


# ------------------------------------------------------------
# argmax() with a 2D array
# ------------------------------------------------------------

matrix = np.array([
    [10, 50, 30],
    [90, 20, 60],
    [40, 80, 70]
])

print("\n2D array:")
print(matrix)

# Flattened index of maximum value
max_index = np.argmax(matrix)

print("\nFlattened index of maximum value:")
print(max_index)

print("\nMaximum value:")
print(matrix.flatten()[max_index])


# ============================================================
# 5. np.argmin()
# ============================================================

print("\n" + "=" * 60)
print("5. np.argmin()")
print("=" * 60)

numbers = np.array([10, 50, 30, 90, 20])

print("Array:")
print(numbers)

# Find index of minimum value
min_index = np.argmin(numbers)

print("\nIndex of minimum value:")
print(min_index)

# Get minimum value
min_value = numbers[min_index]

print("\nMinimum value:")
print(min_value)


# ------------------------------------------------------------
# Real-world example: Find lowest sales
# ------------------------------------------------------------

sales = np.array([
    12000,
    18000,
    15000,
    25000,
    21000
])

min_sales_index = np.argmin(sales)

print("\nSales:")
print(sales)

print("\nLowest sales:")
print(sales[min_sales_index])

print("\nIndex of lowest sales:")
print(min_sales_index)


# ============================================================
# 6. Comparing Array Searching Functions
# ============================================================

print("\n" + "=" * 60)
print("6. Comparing Array Searching Functions")
print("=" * 60)

numbers = np.array([10, 20, 30, 40, 50])

print("Array:")
print(numbers)

# where()
print("\nnp.where(numbers > 25):")
print(np.where(numbers > 25))

# argwhere()
print("\nnp.argwhere(numbers > 25):")
print(np.argwhere(numbers > 25))

# searchsorted()
print("\nnp.searchsorted(numbers, 35):")
print(np.searchsorted(numbers, 35))

# argmax()
print("\nnp.argmax(numbers):")
print(np.argmax(numbers))

# argmin()
print("\nnp.argmin(numbers):")
print(np.argmin(numbers))


# ============================================================
# 7. Practical Data Analysis Example
# ============================================================

print("\n" + "=" * 60)
print("7. Practical Data Analysis Example")
print("=" * 60)

# Monthly sales data
monthly_sales = np.array([
    15000,
    22000,
    18000,
    31000,
    27000,
    12000,
    35000,
    29000,
    19000,
    40000,
    33000,
    25000
])

months = np.array([
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
])

print("Monthly Sales:")
for month, sale in zip(months, monthly_sales):
    print(f"{month:10} : ₹{sale:,}")


# ------------------------------------------------------------
# Highest sales
# ------------------------------------------------------------

highest_index = np.argmax(monthly_sales)
highest_sales = monthly_sales[highest_index]
highest_month = months[highest_index]

print("\nHighest Sales:")
print(f"Month  : {highest_month}")
print(f"Sales  : ₹{highest_sales:,}")


# ------------------------------------------------------------
# Lowest sales
# ------------------------------------------------------------

lowest_index = np.argmin(monthly_sales)
lowest_sales = monthly_sales[lowest_index]
lowest_month = months[lowest_index]

print("\nLowest Sales:")
print(f"Month  : {lowest_month}")
print(f"Sales  : ₹{lowest_sales:,}")


# ------------------------------------------------------------
# Find months with sales above ₹30,000
# ------------------------------------------------------------

high_sales_indices = np.where(monthly_sales > 30000)[0]

print("\nMonths with sales above ₹30,000:")

for index in high_sales_indices:
    print(
        f"{months[index]} : "
        f"₹{monthly_sales[index]:,}"
    )


# ------------------------------------------------------------
# Find positions using argwhere()
# ------------------------------------------------------------

high_sales_positions = np.argwhere(
    monthly_sales > 30000
)

print("\nPositions of sales above ₹30,000:")
print(high_sales_positions)


# ------------------------------------------------------------
# Classify each month
# ------------------------------------------------------------

sales_category = np.where(
    monthly_sales >= 30000,
    "High",
    "Normal"
)

print("\nSales Category:")

for month, category in zip(months, sales_category):
    print(f"{month:10} : {category}")


# ============================================================
# 8. Summary
# ============================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("""
np.where()
    - Finds indices matching a condition
    - Can also perform conditional selection/replacement

np.argwhere()
    - Returns coordinates/indices where a condition is True
    - Particularly useful for multidimensional arrays

np.searchsorted()
    - Finds the position where a value should be inserted
    - Works with sorted arrays

np.argmax()
    - Returns the index of the maximum value

np.argmin()
    - Returns the index of the minimum value

Key Data Analysis Pattern:
    array[condition]

Example:
    sales[sales > 3000]

Multiple Conditions:
    (condition1) & (condition2)   -> AND
    (condition1) | (condition2)   -> OR
    ~(condition)                   -> NOT
""")

print("=" * 60)
print("End of Array Searching")
print("=" * 60)
