"""
============================================================
14 - NumPy Fancy Indexing
============================================================

Topic:
    Fancy Indexing in NumPy

Topics Covered:
    1. Integer Array Indexing
    2. Selecting Multiple Rows
    3. Selecting Multiple Columns
    4. Combining Indexing Techniques

Purpose:
    Fancy indexing allows us to select multiple elements,
    rows, or columns from a NumPy array using arrays/lists
    of integer indices.

Requirements:
    pip install numpy

Author:
    Aziz

============================================================
"""

import numpy as np


# ============================================================
# 1. Integer Array Indexing
# ============================================================

print("=" * 60)
print("1. INTEGER ARRAY INDEXING")
print("=" * 60)

numbers = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:")
print(numbers)

# Select one element
print("\nElement at index 2:")
print(numbers[2])

# Select multiple elements using integer indices
indices = [0, 2, 4]

result = numbers[indices]

print("\nIndices:")
print(indices)

print("\nSelected elements:")
print(result)


# ------------------------------------------------------------
# Using a NumPy array as indices
# ------------------------------------------------------------

indices = np.array([1, 3, 5])

result = numbers[indices]

print("\nNumPy index array:")
print(indices)

print("\nSelected elements:")
print(result)


# ------------------------------------------------------------
# Selecting elements in any order
# ------------------------------------------------------------

indices = np.array([5, 1, 4, 0])

result = numbers[indices]

print("\nIndices in custom order:")
print(indices)

print("\nSelected elements:")
print(result)


# ------------------------------------------------------------
# Selecting the same element multiple times
# ------------------------------------------------------------

indices = np.array([2, 2, 4, 2])

result = numbers[indices]

print("\nRepeated indices:")
print(indices)

print("\nSelected elements:")
print(result)


# ============================================================
# 2. Selecting Multiple Rows
# ============================================================

print("\n" + "=" * 60)
print("2. SELECTING MULTIPLE ROWS")
print("=" * 60)

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120],
    [130, 140, 150]
])

print("Original Matrix:")
print(matrix)


# ------------------------------------------------------------
# Select one row
# ------------------------------------------------------------

print("\nRow at index 2:")
print(matrix[2])


# ------------------------------------------------------------
# Select multiple rows
# ------------------------------------------------------------

row_indices = [0, 2, 4]

selected_rows = matrix[row_indices]

print("\nSelected row indices:")
print(row_indices)

print("\nSelected rows:")
print(selected_rows)


# ------------------------------------------------------------
# Select rows in a custom order
# ------------------------------------------------------------

row_indices = [4, 1, 3]

selected_rows = matrix[row_indices]

print("\nCustom row indices:")
print(row_indices)

print("\nSelected rows:")
print(selected_rows)


# ------------------------------------------------------------
# Select the same row multiple times
# ------------------------------------------------------------

row_indices = [1, 1, 3]

selected_rows = matrix[row_indices]

print("\nRepeated row indices:")
print(row_indices)

print("\nSelected rows:")
print(selected_rows)


# ============================================================
# 3. Selecting Multiple Columns
# ============================================================

print("\n" + "=" * 60)
print("3. SELECTING MULTIPLE COLUMNS")
print("=" * 60)

matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print("Original Matrix:")
print(matrix)


# ------------------------------------------------------------
# Select one column
# ------------------------------------------------------------

print("\nColumn at index 1:")
print(matrix[:, 1])


# ------------------------------------------------------------
# Select multiple columns
# ------------------------------------------------------------

column_indices = [0, 2]

selected_columns = matrix[:, column_indices]

print("\nSelected column indices:")
print(column_indices)

print("\nSelected columns:")
print(selected_columns)


# ------------------------------------------------------------
# Select columns in custom order
# ------------------------------------------------------------

column_indices = [3, 1, 0]

selected_columns = matrix[:, column_indices]

print("\nCustom column indices:")
print(column_indices)

print("\nSelected columns:")
print(selected_columns)


# ------------------------------------------------------------
# Select the same column multiple times
# ------------------------------------------------------------

column_indices = [1, 1, 3]

selected_columns = matrix[:, column_indices]

print("\nRepeated column indices:")
print(column_indices)

print("\nSelected columns:")
print(selected_columns)


# ============================================================
# 4. Selecting Specific Rows and Columns
# ============================================================

print("\n" + "=" * 60)
print("4. SELECTING SPECIFIC ROWS AND COLUMNS")
print("=" * 60)

matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print("Original Matrix:")
print(matrix)


# ------------------------------------------------------------
# Select specific rows first
# ------------------------------------------------------------

row_indices = [0, 2]

selected_rows = matrix[row_indices, :]

print("\nSelected rows:")
print(selected_rows)


# ------------------------------------------------------------
# Select specific columns
# ------------------------------------------------------------

column_indices = [1, 3]

selected_columns = matrix[:, column_indices]

print("\nSelected columns:")
print(selected_columns)


# ------------------------------------------------------------
# Select rows and columns using np.ix_
# ------------------------------------------------------------

row_indices = [0, 2]
column_indices = [1, 3]

result = matrix[
    np.ix_(row_indices, column_indices)
]

print("\nSelected rows:")
print(row_indices)

print("\nSelected columns:")
print(column_indices)

print("\nSelected rows AND columns:")
print(result)


# ============================================================
# 5. Combining Fancy Indexing with Slicing
# ============================================================

print("\n" + "=" * 60)
print("5. COMBINING FANCY INDEXING WITH SLICING")
print("=" * 60)

matrix = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]
])

print("Original Matrix:")
print(matrix)


# ------------------------------------------------------------
# Fancy indexing rows + slicing columns
# ------------------------------------------------------------

row_indices = [0, 2]

result = matrix[row_indices, 1:4]

print("\nSelected rows:")
print(row_indices)

print("\nSelected columns using slicing (1:4):")
print(result)


# ------------------------------------------------------------
# Slicing rows + fancy indexing columns
# ------------------------------------------------------------

column_indices = [0, 2, 4]

result = matrix[1:4, column_indices]

print("\nRows using slicing (1:4):")
print("Columns using fancy indexing:", column_indices)

print("\nResult:")
print(result)


# ============================================================
# 6. Combining Fancy Indexing with Boolean Indexing
# ============================================================

print("\n" + "=" * 60)
print("6. FANCY INDEXING + BOOLEAN INDEXING")
print("=" * 60)

numbers = np.array([
    10, 20, 30, 40, 50, 60, 70, 80
])

print("Original Array:")
print(numbers)


# ------------------------------------------------------------
# Step 1: Select specific indices
# ------------------------------------------------------------

indices = np.array([1, 3, 5, 7])

selected = numbers[indices]

print("\nSelected using fancy indexing:")
print(selected)


# ------------------------------------------------------------
# Step 2: Apply Boolean filtering
# ------------------------------------------------------------

filtered = selected[selected > 30]

print("\nAfter Boolean filtering (> 30):")
print(filtered)


# ------------------------------------------------------------
# Direct approach
# ------------------------------------------------------------

result = numbers[indices][numbers[indices] > 30]

print("\nDirect combined approach:")
print(result)


# ============================================================
# 7. Practical Student Data Example
# ============================================================

print("\n" + "=" * 60)
print("7. PRACTICAL STUDENT DATA EXAMPLE")
print("=" * 60)

students = np.array([
    [101, 85, 90, 88],
    [102, 72, 75, 80],
    [103, 95, 92, 96],
    [104, 60, 65, 70],
    [105, 88, 84, 91]
])

print("Student Data:")
print(students)

print("""
Columns:
    Column 0 -> Student ID
    Column 1 -> Subject 1
    Column 2 -> Subject 2
    Column 3 -> Subject 3
""")


# ------------------------------------------------------------
# Select students 1, 3 and 5
# ------------------------------------------------------------

student_indices = [0, 2, 4]

selected_students = students[student_indices]

print("\nSelected students:")
print(selected_students)


# ------------------------------------------------------------
# Select only subject marks
# ------------------------------------------------------------

marks = students[:, [1, 2, 3]]

print("\nAll subject marks:")
print(marks)


# ------------------------------------------------------------
# Select Subject 1 and Subject 3
# ------------------------------------------------------------

selected_subjects = students[:, [1, 3]]

print("\nSubject 1 and Subject 3:")
print(selected_subjects)


# ------------------------------------------------------------
# Select students 1, 3, 5 and only Subject 1 & 3
# ------------------------------------------------------------

result = students[
    np.ix_(
        [0, 2, 4],
        [1, 3]
    )
]

print("\nSelected students and selected subjects:")
print(result)


# ============================================================
# 8. Practical Sales Data Example
# ============================================================

print("\n" + "=" * 60)
print("8. PRACTICAL SALES DATA EXAMPLE")
print("=" * 60)

sales_data = np.array([
    [101, 12000, 150, 5],
    [102, 18000, 220, 7],
    [103, 25000, 310, 9],
    [104, 9000, 100, 3],
    [105, 32000, 400, 12],
    [106, 21000, 280, 8]
])

print("Sales Data:")
print(sales_data)

print("""
Columns:
    Column 0 -> Product ID
    Column 1 -> Revenue
    Column 2 -> Units Sold
    Column 3 -> Number of Transactions
""")


# ------------------------------------------------------------
# Select specific products
# ------------------------------------------------------------

product_indices = [0, 2, 4]

selected_products = sales_data[product_indices]

print("\nSelected Products:")
print(selected_products)


# ------------------------------------------------------------
# Select Revenue and Units Sold columns
# ------------------------------------------------------------

selected_columns = sales_data[:, [1, 2]]

print("\nRevenue and Units Sold:")
print(selected_columns)


# ------------------------------------------------------------
# Select products and specific metrics
# ------------------------------------------------------------

result = sales_data[
    np.ix_(
        [1, 2, 4],
        [0, 1, 2]
    )
]

print("\nSelected Products and Metrics:")
print(result)


# ============================================================
# 9. Fancy Indexing vs Basic Slicing
# ============================================================

print("\n" + "=" * 60)
print("9. FANCY INDEXING VS BASIC SLICING")
print("=" * 60)

numbers = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(numbers)


# Basic slicing
slice_result = numbers[1:4]

print("\nBasic slicing [1:4]:")
print(slice_result)


# Fancy indexing
fancy_result = numbers[[1, 2, 3]]

print("\nFancy indexing [[1, 2, 3]]:")
print(fancy_result)


print("""
Basic Slicing:
    array[start:stop]

Fancy Indexing:
    array[[index1, index2, index3]]

Basic slicing selects a continuous range.

Fancy indexing allows specific positions,
custom order, and repeated positions.
""")


# ============================================================
# 10. Important Fancy Indexing Rules
# ============================================================

print("\n" + "=" * 60)
print("10. IMPORTANT FANCY INDEXING RULES")
print("=" * 60)

print("""
1. Fancy indexing uses integer arrays/lists.

       array[[0, 2, 4]]

2. You can select elements in any order.

       array[[4, 1, 3]]

3. You can repeat indices.

       array[[1, 1, 3]]

4. For 2D arrays, use:

       array[[row_indices]]

   to select rows.

5. To select columns:

       array[:, [column_indices]]

6. To select specific rows AND columns together,
   np.ix_() is useful:

       array[np.ix_(rows, columns)]

7. Fancy indexing can be combined with:

       - Slicing
       - Boolean indexing
       - Regular indexing

8. Fancy indexing returns a copy rather than a view
   of the original array.
""")


# ============================================================
# 11. Final Summary
# ============================================================

print("\n" + "=" * 60)
print("FINAL SUMMARY")
print("=" * 60)

print("""
Fancy Indexing:
    Selecting multiple array elements using
    integer index arrays.

Integer Array Indexing:
    array[[0, 2, 4]]

Multiple Rows:
    matrix[[0, 2, 4]]

Multiple Columns:
    matrix[:, [0, 2]]

Specific Rows + Columns:
    matrix[np.ix_(rows, columns)]

Fancy Indexing + Slicing:
    matrix[[0, 2], 1:4]

Fancy Indexing + Boolean Filtering:
    array[[1, 3, 5]][array[[1, 3, 5]] > 30]

Key Advantage:
    Fancy indexing allows precise, flexible,
    and non-contiguous data selection.

Important for:
    - Data Analysis
    - Data Cleaning
    - Feature Selection
    - Machine Learning
    - NumPy
    - Pandas
    - Exploratory Data Analysis (EDA)
""")

print("=" * 60)
print("End of Fancy Indexing")
print("=" * 60)
