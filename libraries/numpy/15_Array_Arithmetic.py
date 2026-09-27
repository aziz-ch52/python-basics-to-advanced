"""
============================================================
15 - NumPy Array Arithmetic
============================================================

Topic:
    Array Arithmetic in NumPy

Operations Covered:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Power
    6. Modulo

Additional Concepts:
    - Element-wise arithmetic
    - Scalar arithmetic
    - Arithmetic with 2D arrays
    - Practical data-analysis examples
    - Broadcasting basics

Purpose:
    NumPy allows arithmetic operations to be performed
    efficiently on entire arrays without using explicit
    Python loops.

Requirements:
    pip install numpy

Author:
    Aziz

============================================================
"""

import numpy as np


# ============================================================
# 1. Creating Arrays
# ============================================================

print("=" * 60)
print("1. CREATING ARRAYS")
print("=" * 60)

array_a = np.array([10, 20, 30, 40, 50])
array_b = np.array([2, 4, 5, 8, 10])

print("Array A:")
print(array_a)

print("\nArray B:")
print(array_b)


# ============================================================
# 2. Addition
# ============================================================

print("\n" + "=" * 60)
print("2. ADDITION")
print("=" * 60)

result = array_a + array_b

print("Array A:")
print(array_a)

print("\nArray B:")
print(array_b)

print("\nA + B:")
print(result)


# ------------------------------------------------------------
# Addition with a scalar
# ------------------------------------------------------------

result = array_a + 10

print("\nA + 10:")
print(result)


# ------------------------------------------------------------
# np.add()
# ------------------------------------------------------------

result = np.add(array_a, array_b)

print("\nUsing np.add():")
print(result)


# ============================================================
# 3. Subtraction
# ============================================================

print("\n" + "=" * 60)
print("3. SUBTRACTION")
print("=" * 60)

result = array_a - array_b

print("A - B:")
print(result)


# ------------------------------------------------------------
# Subtraction with a scalar
# ------------------------------------------------------------

result = array_a - 5

print("\nA - 5:")
print(result)


# ------------------------------------------------------------
# np.subtract()
# ------------------------------------------------------------

result = np.subtract(array_a, array_b)

print("\nUsing np.subtract():")
print(result)


# ============================================================
# 4. Multiplication
# ============================================================

print("\n" + "=" * 60)
print("4. MULTIPLICATION")
print("=" * 60)

result = array_a * array_b

print("A * B:")
print(result)


# ------------------------------------------------------------
# Multiplication with a scalar
# ------------------------------------------------------------

result = array_a * 2

print("\nA * 2:")
print(result)


# ------------------------------------------------------------
# np.multiply()
# ------------------------------------------------------------

result = np.multiply(array_a, array_b)

print("\nUsing np.multiply():")
print(result)


# IMPORTANT:
# NumPy multiplication between arrays is element-wise.
#
# Example:
# [10, 20, 30] * [2, 4, 5]
#
# = [10*2, 20*4, 30*5]
# = [20, 80, 150]


# ============================================================
# 5. Division
# ============================================================

print("\n" + "=" * 60)
print("5. DIVISION")
print("=" * 60)

result = array_a / array_b

print("A / B:")
print(result)


# ------------------------------------------------------------
# Division with a scalar
# ------------------------------------------------------------

result = array_a / 10

print("\nA / 10:")
print(result)


# ------------------------------------------------------------
# np.divide()
# ------------------------------------------------------------

result = np.divide(array_a, array_b)

print("\nUsing np.divide():")
print(result)


# ============================================================
# 6. Power
# ============================================================

print("\n" + "=" * 60)
print("6. POWER")
print("=" * 60)

numbers = np.array([2, 3, 4, 5])

print("Numbers:")
print(numbers)


# Square each element
result = numbers ** 2

print("\nNumbers squared:")
print(result)


# Cube each element
result = numbers ** 3

print("\nNumbers cubed:")
print(result)


# ------------------------------------------------------------
# Power using np.power()
# ------------------------------------------------------------

result = np.power(numbers, 2)

print("\nUsing np.power(numbers, 2):")
print(result)


# ------------------------------------------------------------
# Array-to-array power
# ------------------------------------------------------------

base = np.array([2, 3, 4])
exponent = np.array([2, 3, 2])

result = base ** exponent

print("\nBase:")
print(base)

print("\nExponent:")
print(exponent)

print("\nBase ** Exponent:")
print(result)


# ============================================================
# 7. Modulo
# ============================================================

print("\n" + "=" * 60)
print("7. MODULO")
print("=" * 60)

numbers = np.array([10, 15, 20, 25, 30])

result = numbers % 3

print("Numbers:")
print(numbers)

print("\nRemainder after division by 3:")
print(result)


# ------------------------------------------------------------
# Array-to-array modulo
# ------------------------------------------------------------

array_a = np.array([10, 20, 30, 40, 50])
array_b = np.array([3, 6, 7, 9, 11])

result = array_a % array_b

print("\nArray A:")
print(array_a)

print("\nArray B:")
print(array_b)

print("\nA % B:")
print(result)


# ------------------------------------------------------------
# np.mod()
# ------------------------------------------------------------

result = np.mod(array_a, array_b)

print("\nUsing np.mod():")
print(result)


# ============================================================
# 8. Arithmetic with 2D Arrays
# ============================================================

print("\n" + "=" * 60)
print("8. ARITHMETIC WITH 2D ARRAYS")
print("=" * 60)

matrix_a = np.array([
    [10, 20],
    [30, 40]
])

matrix_b = np.array([
    [1, 2],
    [3, 4]
])

print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)


# Addition
print("\nA + B:")
print(matrix_a + matrix_b)


# Subtraction
print("\nA - B:")
print(matrix_a - matrix_b)


# Multiplication
print("\nA * B:")
print(matrix_a * matrix_b)


# Division
print("\nA / B:")
print(matrix_a / matrix_b)


# Power
print("\nA ** 2:")
print(matrix_a ** 2)


# Modulo
print("\nA % B:")
print(matrix_a % matrix_b)


# ============================================================
# 9. Scalar Arithmetic
# ============================================================

print("\n" + "=" * 60)
print("9. SCALAR ARITHMETIC")
print("=" * 60)

numbers = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(numbers)


print("\nAddition:")
print(numbers + 5)


print("\nSubtraction:")
print(numbers - 5)


print("\nMultiplication:")
print(numbers * 5)


print("\nDivision:")
print(numbers / 5)


print("\nPower:")
print(numbers ** 2)


print("\nModulo:")
print(numbers % 3)


# ============================================================
# 10. Practical Data Analysis Example - Sales
# ============================================================

print("\n" + "=" * 60)
print("10. PRACTICAL DATA ANALYSIS - SALES")
print("=" * 60)

sales_january = np.array([
    10000,
    15000,
    12000,
    18000,
    20000
])

sales_february = np.array([
    12000,
    14000,
    15000,
    20000,
    22000
])

print("January Sales:")
print(sales_january)

print("\nFebruary Sales:")
print(sales_february)


# ------------------------------------------------------------
# Total sales for each product
# ------------------------------------------------------------

total_sales = sales_january + sales_february

print("\nTotal Sales:")
print(total_sales)


# ------------------------------------------------------------
# Change in sales
# ------------------------------------------------------------

sales_change = sales_february - sales_january

print("\nChange in Sales:")
print(sales_change)


# ------------------------------------------------------------
# Percentage change
# ------------------------------------------------------------

percentage_change = (
    (sales_february - sales_january)
    / sales_january
) * 100

print("\nPercentage Change:")
print(percentage_change)


# ============================================================
# 11. Practical Data Analysis - Product Price
# ============================================================

print("\n" + "=" * 60)
print("11. PRACTICAL DATA ANALYSIS - PRODUCT PRICE")
print("=" * 60)

cost_price = np.array([
    500,
    800,
    1200,
    1500,
    2000
])

selling_price = np.array([
    700,
    1000,
    1500,
    1800,
    2500
])

print("Cost Price:")
print(cost_price)

print("\nSelling Price:")
print(selling_price)


# ------------------------------------------------------------
# Profit
# ------------------------------------------------------------

profit = selling_price - cost_price

print("\nProfit:")
print(profit)


# ------------------------------------------------------------
# Profit percentage
# ------------------------------------------------------------

profit_percentage = (
    profit / cost_price
) * 100

print("\nProfit Percentage:")
print(profit_percentage)


# ============================================================
# 12. Practical Data Analysis - Employee Salary
# ============================================================

print("\n" + "=" * 60)
print("12. PRACTICAL DATA ANALYSIS - EMPLOYEE SALARY")
print("=" * 60)

salary = np.array([
    25000,
    30000,
    35000,
    40000,
    50000
])

annual_salary = salary * 12

print("Monthly Salary:")
print(salary)

print("\nAnnual Salary:")
print(annual_salary)


# ------------------------------------------------------------
# 10% salary increase
# ------------------------------------------------------------

new_salary = salary * 1.10

print("\nSalary after 10% increase:")
print(new_salary)


# ------------------------------------------------------------
# Monthly salary after ₹2,000 increment
# ------------------------------------------------------------

updated_salary = salary + 2000

print("\nSalary after ₹2,000 increment:")
print(updated_salary)


# ============================================================
# 13. Practical Data Analysis - Quantity and Price
# ============================================================

print("\n" + "=" * 60)
print("13. PRACTICAL DATA ANALYSIS - REVENUE")
print("=" * 60)

quantity_sold = np.array([
    10,
    20,
    15,
    30,
    25
])

price_per_unit = np.array([
    100,
    250,
    150,
    300,
    200
])

print("Quantity Sold:")
print(quantity_sold)

print("\nPrice Per Unit:")
print(price_per_unit)


# Revenue = Quantity × Price
revenue = quantity_sold * price_per_unit

print("\nRevenue:")
print(revenue)


# ============================================================
# 14. Combining Multiple Arithmetic Operations
# ============================================================

print("\n" + "=" * 60)
print("14. COMBINING MULTIPLE ARITHMETIC OPERATIONS")
print("=" * 60)

prices = np.array([
    100,
    200,
    300,
    400,
    500
])

quantity = np.array([
    2,
    3,
    4,
    5,
    6
])

discount = 0.10

print("Prices:")
print(prices)

print("\nQuantity:")
print(quantity)

# Calculate original revenue
revenue = prices * quantity

print("\nOriginal Revenue:")
print(revenue)


# Calculate discount amount
discount_amount = revenue * discount

print("\nDiscount Amount:")
print(discount_amount)


# Calculate final revenue
final_revenue = revenue - discount_amount

print("\nFinal Revenue:")
print(final_revenue)


# ============================================================
# 15. Arithmetic with Boolean Conditions
# ============================================================

print("\n" + "=" * 60)
print("15. ARITHMETIC + BOOLEAN CONDITIONS")
print("=" * 60)

sales = np.array([
    1200,
    4500,
    800,
    6700,
    3200
])

print("Sales:")
print(sales)


# Apply 10% bonus only to sales above 3000
bonus = np.where(
    sales > 3000,
    sales * 0.10,
    0
)

print("\nBonus:")
print(bonus)


# Final amount
final_sales = sales + bonus

print("\nSales after bonus:")
print(final_sales)


# ============================================================
# 16. Understanding Element-wise Arithmetic
# ============================================================

print("\n" + "=" * 60)
print("16. ELEMENT-WISE ARITHMETIC")
print("=" * 60)

array_a = np.array([10, 20, 30])
array_b = np.array([2, 4, 5])

print("Array A:")
print(array_a)

print("\nArray B:")
print(array_b)

print("\nAddition:")
print(array_a + array_b)

print("\nSubtraction:")
print(array_a - array_b)

print("\nMultiplication:")
print(array_a * array_b)

print("\nDivision:")
print(array_a / array_b)

print("\nPower:")
print(array_a ** array_b)

print("\nModulo:")
print(array_a % array_b)


# ============================================================
# 17. Broadcasting Basics
# ============================================================

print("\n" + "=" * 60)
print("17. BROADCASTING BASICS")
print("=" * 60)

numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Original Matrix:")
print(numbers)

# Scalar is automatically applied to every element
result = numbers + 10

print("\nMatrix + 10:")
print(result)


# ------------------------------------------------------------
# Broadcasting with a 1D array
# ------------------------------------------------------------

prices = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

discount = np.array([
    10,
    20,
    30
])

result = prices - discount

print("\nPrices:")
print(prices)

print("\nDiscount:")
print(discount)

print("\nPrices after discount:")
print(result)


# ============================================================
# 18. Division by Zero
# ============================================================

print("\n" + "=" * 60)
print("18. DIVISION BY ZERO")
print("=" * 60)

numbers = np.array([10, 20, 30])

divisor = np.array([2, 0, 5])

print("Numbers:")
print(numbers)

print("\nDivisor:")
print(divisor)

# NumPy may produce inf and a runtime warning
# when dividing floating-point values by zero.

with np.errstate(divide="ignore", invalid="ignore"):
    result = numbers / divisor

print("\nDivision Result:")
print(result)


# ============================================================
# 19. Arithmetic Operation Summary
# ============================================================

print("\n" + "=" * 60)
print("19. ARITHMETIC OPERATION SUMMARY")
print("=" * 60)

array_a = np.array([10, 20, 30])
array_b = np.array([2, 4, 5])

print("""
Operation       Operator       NumPy Function

Addition           +            np.add()
Subtraction        -            np.subtract()
Multiplication     *            np.multiply()
Division           /            np.divide()
Power              **           np.power()
Modulo             %            np.mod()
""")


print("Array A:")
print(array_a)

print("\nArray B:")
print(array_b)

print("\nAddition:")
print(array_a + array_b)

print("\nSubtraction:")
print(array_a - array_b)

print("\nMultiplication:")
print(array_a * array_b)

print("\nDivision:")
print(array_a / array_b)

print("\nPower:")
print(array_a ** array_b)

print("\nModulo:")
print(array_a % array_b)


# ============================================================
# 20. Final Summary
# ============================================================

print("\n" + "=" * 60)
print("FINAL SUMMARY")
print("=" * 60)

print("""
NumPy performs arithmetic operations element by element.

Addition:
    array_a + array_b

Subtraction:
    array_a - array_b

Multiplication:
    array_a * array_b

Division:
    array_a / array_b

Power:
    array_a ** array_b

Modulo:
    array_a % array_b

Equivalent NumPy functions:

    np.add()
    np.subtract()
    np.multiply()
    np.divide()
    np.power()
    np.mod()

Important Concepts:
    - Element-wise arithmetic
    - Scalar arithmetic
    - Broadcasting
    - Arithmetic with 1D arrays
    - Arithmetic with 2D arrays
    - Combining arithmetic operations
    - Handling division by zero

Data Analysis Applications:
    - Revenue calculation
    - Profit calculation
    - Percentage change
    - Salary calculations
    - Discounts
    - Sales analysis
    - Pricing analysis
    - KPI calculations
""")

print("=" * 60)
print("End of NumPy Array Arithmetic")
print("=" * 60)
