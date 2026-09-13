"""
=========================================================
02. VECTORIZATION (NO MORE FOR LOOPS)
=========================================================
In data analytics, if you are writing a 'for' loop to do math 
on a dataset, you are doing it wrong. 

Vectorization allows you to apply a mathematical operation 
to an entire array of data simultaneously.
=========================================================
"""
import numpy as np

print("--- 1. SCALAR MATH (APPLYING A NUMBER TO AN ARRAY) ---")
base_prices = np.array([10.0, 25.5, 50.0, 100.0])
print(f"Raw Prices: {base_prices}")

# Add a $5 shipping fee to EVERY item instantly
total_prices = base_prices + 5.0
print(f"With Shipping: {total_prices}")

# Apply a 20% discount to EVERY item instantly
discounted = base_prices * 0.8
print(f"20% Off: {discounted}")


print("\n--- 2. ARRAY-TO-ARRAY MATH ---")
revenue = np.array([5000, 7500, 9000])
costs = np.array([2000, 3000, 8500])

# Calculate profit for all months instantly
profit = revenue - costs
print(f"Monthly Profit: {profit}")

# Identify which months were actually profitable using boolean logic
profitable_months = profit > 0
print(f"Was profitable? {profitable_months}")
