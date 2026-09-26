"""
============================================================
14 - Boolean Indexing & Filtering
============================================================

Topic:
    Boolean Indexing & Filtering in NumPy

Topics Covered:
    1. Comparison Operators
    2. Boolean Arrays
    3. Conditional Filtering
    4. Multiple Conditions
    5. &  (AND)
    6. |  (OR)
    7. ~  (NOT)

Purpose:
    This file demonstrates how Boolean logic can be used
    to filter and analyze NumPy arrays.

Requirements:
    pip install numpy

Author:
    Aziz

============================================================
"""

import numpy as np


# ============================================================
# 1. Comparison Operators
# ============================================================

print("=" * 60)
print("1. COMPARISON OPERATORS")
print("=" * 60)

numbers = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(numbers)


# Greater than
print("\nGreater than 30:")
print(numbers > 30)


# Less than
print("\nLess than 30:")
print(numbers < 30)


# Greater than or equal to
print("\nGreater than or equal to 30:")
print(numbers >= 30)


# Less than or equal to
print("\nLess than or equal to 30:")
print(numbers <= 30)


# Equal to
print("\nEqual to 30:")
print(numbers == 30)


# Not equal to
print("\nNot equal to 30:")
print(numbers != 30)


# ============================================================
# 2. Boolean Arrays
# ============================================================

print("\n" + "=" * 60)
print("2. BOOLEAN ARRAYS")
print("=" * 60)

numbers = np.array([10, 20, 30, 40, 50])

# Create a Boolean condition
condition = numbers > 30

print("Original Array:")
print(numbers)

print("\nBoolean Condition:")
print(condition)

print("\nBoolean Data Type:")
print(condition.dtype)


# ------------------------------------------------------------
# Using Boolean Array for Indexing
# ------------------------------------------------------------

filtered_values = numbers[condition]

print("\nValues where condition is True:")
print(filtered_values)


# ------------------------------------------------------------
# Another Boolean example
# ------------------------------------------------------------

marks = np.array([35, 78, 45, 91, 62, 28])

passed = marks >= 50

print("\nMarks:")
print(marks)

print("\nPass Condition:")
print(passed)

print("\nPassing Marks:")
print(marks[passed])


# ============================================================
# 3. Conditional Filtering
# ============================================================

print("\n" + "=" * 60)
print("3. CONDITIONAL FILTERING")
print("=" * 60)

sales = np.array([
    1200,
    4500,
    800,
    6700,
    3200,
    1500
])

print("Sales:")
print(sales)


# ------------------------------------------------------------
# Filter values greater than 3000
# ------------------------------------------------------------

high_sales = sales[sales > 3000]

print("\nSales greater than 3000:")
print(high_sales)


# ------------------------------------------------------------
# Filter values less than 2000
# ------------------------------------------------------------

low_sales = sales[sales < 2000]

print("\nSales less than 2000:")
print(low_sales)


# ------------------------------------------------------------
# Filter values equal to 1500
# ------------------------------------------------------------

specific_sales = sales[sales == 1500]

print("\nSales equal to 1500:")
print(specific_sales)


# ------------------------------------------------------------
# Filter values not equal to 1500
# ------------------------------------------------------------

other_sales = sales[sales != 1500]

print("\nSales not equal to 1500:")
print(other_sales)


# ============================================================
# 4. Multiple Conditions
# ============================================================

print("\n" + "=" * 60)
print("4. MULTIPLE CONDITIONS")
print("=" * 60)

numbers = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:")
print(numbers)


# ------------------------------------------------------------
# AND condition
# ------------------------------------------------------------

result = numbers[
    (numbers > 20) &
    (numbers < 60)
]

print("\nValues greater than 20 AND less than 60:")
print(result)


# ------------------------------------------------------------
# OR condition
# ------------------------------------------------------------

result = numbers[
    (numbers < 20) |
    (numbers > 50)
]

print("\nValues less than 20 OR greater than 50:")
print(result)


# ------------------------------------------------------------
# NOT condition
# ------------------------------------------------------------

result = numbers[
    ~(numbers > 30)
]

print("\nValues NOT greater than 30:")
print(result)


# ============================================================
# 5. & Operator — AND
# ============================================================

print("\n" + "=" * 60)
print("5. & OPERATOR — AND")
print("=" * 60)

numbers = np.array([10, 20, 30, 40, 50, 60])

condition_1 = numbers >= 20
condition_2 = numbers <= 50

print("Original Array:")
print(numbers)

print("\nCondition 1 (>= 20):")
print(condition_1)

print("\nCondition 2 (<= 50):")
print(condition_2)

combined_condition = condition_1 & condition_2

print("\nCombined AND Condition:")
print(combined_condition)

print("\nValues between 20 and 50:")
print(numbers[combined_condition])


# Direct approach

result = numbers[
    (numbers >= 20) &
    (numbers <= 50)
]

print("\nDirect Filtering:")
print(result)


# ============================================================
# 6. | Operator — OR
# ============================================================

print("\n" + "=" * 60)
print("6. | OPERATOR — OR")
print("=" * 60)

numbers = np.array([10, 20, 30, 40, 50, 60])

condition_1 = numbers < 20
condition_2 = numbers > 50

print("Original Array:")
print(numbers)

print("\nCondition 1 (< 20):")
print(condition_1)

print("\nCondition 2 (> 50):")
print(condition_2)

combined_condition = condition_1 | condition_2

print("\nCombined OR Condition:")
print(combined_condition)

print("\nValues less than 20 OR greater than 50:")
print(numbers[combined_condition])


# Direct approach

result = numbers[
    (numbers < 20) |
    (numbers > 50)
]

print("\nDirect Filtering:")
print(result)


# ============================================================
# 7. ~ Operator — NOT
# ============================================================

print("\n" + "=" * 60)
print("7. ~ OPERATOR — NOT")
print("=" * 60)

numbers = np.array([10, 20, 30, 40, 50])

condition = numbers > 30

print("Original Array:")
print(numbers)

print("\nOriginal Condition (numbers > 30):")
print(condition)

not_condition = ~condition

print("\nNOT Condition:")
print(not_condition)

print("\nValues NOT greater than 30:")
print(numbers[not_condition])


# Direct approach

result = numbers[
    ~(numbers > 30)
]

print("\nDirect Filtering:")
print(result)


# ============================================================
# 8. Combining &, | and ~
# ============================================================

print("\n" + "=" * 60)
print("8. COMBINING &, | AND ~")
print("=" * 60)

numbers = np.array([
    10, 15, 20, 25, 30,
    35, 40, 45, 50, 55
])

print("Original Array:")
print(numbers)


# AND
result = numbers[
    (numbers >= 20) &
    (numbers <= 40)
]

print("\nBetween 20 and 40:")
print(result)


# OR
result = numbers[
    (numbers < 20) |
    (numbers > 45)
]

print("\nBelow 20 OR above 45:")
print(result)


# NOT
result = numbers[
    ~(numbers >= 30)
]

print("\nNOT greater than or equal to 30:")
print(result)


# Combined complex condition
result = numbers[
    ((numbers >= 20) & (numbers <= 40)) |
    (numbers == 55)
]

print("\nBetween 20 and 40 OR equal to 55:")
print(result)


# ============================================================
# 9. Filtering a 2D Array
# ============================================================

print("\n" + "=" * 60)
print("9. BOOLEAN FILTERING WITH 2D ARRAYS")
print("=" * 60)

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original 2D Array:")
print(matrix)

# Filter values greater than 50
result = matrix[matrix > 50]

print("\nValues greater than 50:")
print(result)


# Filter values between 30 and 80
result = matrix[
    (matrix >= 30) &
    (matrix <= 80)
]

print("\nValues between 30 and 80:")
print(result)


# ============================================================
# 10. Practical Data Analysis Example
# ============================================================

print("\n" + "=" * 60)
print("10. PRACTICAL DATA ANALYSIS EXAMPLE")
print("=" * 60)


# ------------------------------------------------------------
# Customer transaction data
# ------------------------------------------------------------

transactions = np.array([
    500,
    1200,
    2500,
    800,
    4500,
    3200,
    1500,
    6000,
    900,
    3800
])

print("Customer Transactions:")
print(transactions)


# ------------------------------------------------------------
# High-value transactions
# ------------------------------------------------------------

high_value = transactions[transactions >= 3000]

print("\nHigh-value transactions (>= 3000):")
print(high_value)


# ------------------------------------------------------------
# Low-value transactions
# ------------------------------------------------------------

low_value = transactions[transactions < 1000]

print("\nLow-value transactions (< 1000):")
print(low_value)


# ------------------------------------------------------------
# Medium-value transactions
# ------------------------------------------------------------

medium_value = transactions[
    (transactions >= 1000) &
    (transactions < 3000)
]

print("\nMedium-value transactions:")
print(medium_value)


# ------------------------------------------------------------
# Very low OR very high transactions
# ------------------------------------------------------------

extreme_transactions = transactions[
    (transactions < 1000) |
    (transactions > 5000)
]

print("\nExtreme transactions:")
print(extreme_transactions)


# ------------------------------------------------------------
# Transactions NOT greater than 3000
# ------------------------------------------------------------

not_high_value = transactions[
    ~(transactions > 3000)
]

print("\nTransactions NOT greater than 3000:")
print(not_high_value)


# ============================================================
# 11. Practical Customer Age Example
# ============================================================

print("\n" + "=" * 60)
print("11. PRACTICAL CUSTOMER AGE FILTERING")
print("=" * 60)

ages = np.array([
    16, 18, 21, 25, 32,
    45, 52, 67, 72, 29
])

print("Customer Ages:")
print(ages)


# Adults
adults = ages[ages >= 18]

print("\nAdults:")
print(adults)


# Young adults between 18 and 30
young_adults = ages[
    (ages >= 18) &
    (ages <= 30)
]

print("\nCustomers aged 18-30:")
print(young_adults)


# Senior customers
senior_customers = ages[ages >= 60]

print("\nSenior customers (60+):")
print(senior_customers)


# ============================================================
# 12. Practical Employee Salary Example
# ============================================================

print("\n" + "=" * 60)
print("12. PRACTICAL EMPLOYEE SALARY FILTERING")
print("=" * 60)

salaries = np.array([
    25000,
    35000,
    42000,
    28000,
    55000,
    70000,
    32000,
    48000
])

print("Employee Salaries:")
print(salaries)


# Salaries above 40000
high_salary = salaries[salaries > 40000]

print("\nSalaries above 40,000:")
print(high_salary)


# Salaries between 30000 and 50000
mid_salary = salaries[
    (salaries >= 30000) &
    (salaries <= 50000)
]

print("\nSalaries between 30,000 and 50,000:")
print(mid_salary)


# Salaries below 30000 OR above 60000
extreme_salary = salaries[
    (salaries < 30000) |
    (salaries > 60000)
]

print("\nSalaries below 30,000 OR above 60,000:")
print(extreme_salary)


# ============================================================
# 13. Boolean Filtering + np.where()
# ============================================================

print("\n" + "=" * 60)
print("13. BOOLEAN FILTERING + np.where()")
print("=" * 60)

marks = np.array([
    35, 48, 55, 72, 89, 41, 95, 63
])

print("Student Marks:")
print(marks)


# Create Pass/Fail classification
result = np.where(
    marks >= 50,
    "Pass",
    "Fail"
)

print("\nPass/Fail Classification:")
print(result)


# Create performance classification
performance = np.where(
    marks >= 80,
    "Excellent",
    np.where(
        marks >= 60,
        "Good",
        np.where(
            marks >= 50,
            "Average",
            "Fail"
        )
    )
)

print("\nPerformance Classification:")
print(performance)


# ============================================================
# 14. Important NumPy Boolean Rules
# ============================================================

print("\n" + "=" * 60)
print("14. IMPORTANT NUMPY BOOLEAN RULES")
print("=" * 60)

print("""
1. Use & for AND
       (condition1) & (condition2)

2. Use | for OR
       (condition1) | (condition2)

3. Use ~ for NOT
       ~(condition)

4. Always use parentheses around conditions.

5. Do NOT use Python's:
       and
       or
       not

   with NumPy arrays.

6. Boolean indexing follows:
       array[condition]

Example:
       sales[sales > 3000]

7. Boolean arrays contain:
       True
       False

8. Boolean indexing returns only the
   elements where the condition is True.
""")


# ============================================================
# 15. Common Mistakes
# ============================================================

print("\n" + "=" * 60)
print("15. COMMON MISTAKES")
print("=" * 60)

print("""
WRONG:
    array > 10 and array < 50

CORRECT:
    (array > 10) & (array < 50)


WRONG:
    array < 10 or array > 50

CORRECT:
    (array < 10) | (array > 50)


WRONG:
    not (array > 30)

CORRECT:
    ~(array > 30)


WRONG:
    array[array > 10 & array < 50]

CORRECT:
    array[(array > 10) & (array < 50)]
""")


# ============================================================
# 16. Final Summary
# ============================================================

print("\n" + "=" * 60)
print("FINAL SUMMARY")
print("=" * 60)

print("""
Comparison Operators:
    >      Greater than
    <      Less than
    >=     Greater than or equal
    <=     Less than or equal
    ==     Equal
    !=     Not equal

Boolean Array:
    An array containing True and False values.

Conditional Filtering:
    array[condition]

AND:
    (condition1) & (condition2)

OR:
    (condition1) | (condition2)

NOT:
    ~(condition)

Example:
    sales[(sales >= 1000) & (sales <= 5000)]

This technique is fundamental to:
    - NumPy
    - Pandas
    - Data Analysis
    - Data Cleaning
    - Feature Selection
    - Exploratory Data Analysis (EDA)
    - Data Filtering
""")

print("=" * 60)
print("End of Boolean Indexing & Filtering")
print("=" * 60)

