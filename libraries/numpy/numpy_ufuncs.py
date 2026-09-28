"""
NumPy Universal Functions (ufuncs)
==================================

This file demonstrates commonly used NumPy Universal Functions:

1. np.sqrt()   - Square root
2. np.abs()    - Absolute value
3. np.exp()    - Exponential
4. np.log()    - Natural logarithm
5. np.round()  - Rounding
6. np.floor()  - Round down
7. np.ceil()   - Round up

Ufuncs perform operations element-by-element on NumPy arrays.
"""

import numpy as np


# ============================================================
# 1. np.sqrt() - Square Root
# ============================================================

print("=" * 60)
print("1. np.sqrt() - Square Root")
print("=" * 60)

numbers = np.array([1, 4, 9, 16, 25, 36])

square_root = np.sqrt(numbers)

print("Original Array :", numbers)
print("Square Root    :", square_root)


# ============================================================
# 2. np.abs() - Absolute Value
# ============================================================

print("\n" + "=" * 60)
print("2. np.abs() - Absolute Value")
print("=" * 60)

numbers = np.array([-20, -10, -5, 0, 5, 10, 20])

absolute_values = np.abs(numbers)

print("Original Array :", numbers)
print("Absolute Value :", absolute_values)


# ============================================================
# 3. np.exp() - Exponential
# ============================================================

print("\n" + "=" * 60)
print("3. np.exp() - Exponential")
print("=" * 60)

numbers = np.array([0, 1, 2, 3, 4])

exponential_values = np.exp(numbers)

print("Original Array :", numbers)
print("e^x Values     :", exponential_values)


# ============================================================
# 4. np.log() - Natural Logarithm
# ============================================================

print("\n" + "=" * 60)
print("4. np.log() - Natural Logarithm")
print("=" * 60)

numbers = np.array([1, 2.7182818, 7.389056, 20.085537])

log_values = np.log(numbers)

print("Original Array :", numbers)
print("Natural Log    :", log_values)


# ============================================================
# 5. np.round() - Rounding
# ============================================================

print("\n" + "=" * 60)
print("5. np.round() - Rounding")
print("=" * 60)

numbers = np.array([1.2345, 2.6789, 3.14159, 4.5678])

rounded_values = np.round(numbers)
rounded_to_2 = np.round(numbers, 2)

print("Original Array :", numbers)
print("Rounded        :", rounded_values)
print("Rounded (2 dp) :", rounded_to_2)


# ============================================================
# 6. np.floor() - Round Down
# ============================================================

print("\n" + "=" * 60)
print("6. np.floor() - Round Down")
print("=" * 60)

numbers = np.array([1.2, 1.8, 2.3, 4.7, 5.9])

floor_values = np.floor(numbers)

print("Original Array :", numbers)
print("Floor Values   :", floor_values)


# ============================================================
# 7. np.ceil() - Round Up
# ============================================================

print("\n" + "=" * 60)
print("7. np.ceil() - Round Up")
print("=" * 60)

numbers = np.array([1.2, 1.8, 2.3, 4.7, 5.9])

ceil_values = np.ceil(numbers)

print("Original Array :", numbers)
print("Ceil Values    :", ceil_values)


# ============================================================
# 8. Comparing round(), floor(), and ceil()
# ============================================================

print("\n" + "=" * 60)
print("8. Comparing round(), floor(), and ceil()")
print("=" * 60)

numbers = np.array([1.2, 1.5, 1.8, 2.3, 2.7, 3.5])

print("Original :", numbers)
print("Round    :", np.round(numbers))
print("Floor    :", np.floor(numbers))
print("Ceil     :", np.ceil(numbers))


# ============================================================
# 9. Ufuncs on a 2D Array
# ============================================================

print("\n" + "=" * 60)
print("9. Ufuncs on a 2D Array")
print("=" * 60)

matrix = np.array([
    [1, 4, 9],
    [16, 25, 36]
])

print("Original Matrix:")
print(matrix)

print("\nSquare Root:")
print(np.sqrt(matrix))

print("\nAbsolute Value:")
print(np.abs(matrix))

print("\nRounded Values:")
print(np.round(matrix))


# ============================================================
# 10. Practical Data Analytics Example
# ============================================================

print("\n" + "=" * 60)
print("10. Practical Data Analytics Example")
print("=" * 60)

# Actual and predicted sales
actual_sales = np.array([100, 200, 300, 400, 500])
predicted_sales = np.array([110, 190, 280, 420, 480])

# Calculate prediction error
error = actual_sales - predicted_sales

# Convert errors into positive values
absolute_error = np.abs(error)

print("Actual Sales    :", actual_sales)
print("Predicted Sales :", predicted_sales)
print("Error           :", error)
print("Absolute Error  :", absolute_error)

# Average absolute error
mean_absolute_error = np.mean(absolute_error)

print("Mean Absolute Error:", np.round(mean_absolute_error, 2))


# ============================================================
# 11. Summary
# ============================================================

print("\n" + "=" * 60)
print("Ufunc Summary")
print("=" * 60)

print("""
np.sqrt()  -> Calculates square root
np.abs()   -> Calculates absolute value
np.exp()   -> Calculates e raised to the power of x
np.log()   -> Calculates natural logarithm
np.round() -> Rounds values
np.floor() -> Rounds values down
np.ceil()  -> Rounds values up

Main Advantage:
NumPy ufuncs perform operations element-by-element
without requiring an explicit Python for loop.
""")
