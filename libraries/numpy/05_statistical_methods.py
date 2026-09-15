"""
=========================================================
05. STATISTICAL AGGREGATION & FILTERING
=========================================================
This is the core of data analytics. Once your data is in a 
NumPy array, extracting business intelligence takes seconds.
=========================================================
"""
import numpy as np

print("--- AGGREGATING METRICS ---")
# Simulated user ages
ages = np.array([22, 25, 29, 35, 42, 22, 19, 55, 38, 27])

print(f"Total Users:     {ages.size}")
print(f"Average Age:     {ages.mean():.1f}")
print(f"Median Age:      {np.median(ages)}")
print(f"Standard Dev:    {ages.std():.2f}")
print(f"Oldest User:     {ages.max()}")
print(f"Youngest User:   {ages.min()}")

print("\n--- CONDITIONAL FILTERING (np.where) ---")
# np.where is critical for cleaning data. 
# Syntax: np.where(condition, value_if_true, value_if_false)

# Let's say anyone under 21 is categorized as a "Minor", else "Adult"
categories = np.where(ages < 21, "Minor", "Adult")
print(f"Categorized Users: {categories}")

# Extracting only the data that meets a condition (Masking)
# Give me the actual numbers of users older than 30
over_30 = ages[ages > 30]
print(f"Ages over 30: {over_30}")
