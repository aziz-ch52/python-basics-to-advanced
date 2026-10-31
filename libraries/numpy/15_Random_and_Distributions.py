"""
Core Concept: Generating synthetic data, shuffling arrays, and statistical distributions.
In machine learning and data testing, you constantly need random weights, dummy data, 
or random samples. We use NumPy's modern Generator API for this.
"""

import numpy as np

# ==========================================
# 1. THE MODERN RANDOM GENERATOR & SEEDING
# Do not use the old `np.random.rand()` methods. The modern, faster, and safer 
# way is to create a Generator object using `default_rng()`.
# Setting a "seed" ensures your random numbers are the exact same every time you run the script,
# which is mandatory for reproducible science and debugging.
# ==========================================
print("--- 1. Generator and Seeding ---")
seed_value = 42  # The answer to life, the universe, and everything.
rng = np.random.default_rng(seed=seed_value)

print(f"Generator initialized with seed: {seed_value}")
print("-" * 40)


# ==========================================
# 2. BASIC RANDOM NUMBERS (Uniform Distribution)
# Generating basic decimals and integers where every number has an equal chance of appearing.
# ==========================================
print("\n--- 2. Basic Random Numbers ---")

# Random floats between 0.0 and 1.0
random_floats = rng.random((2, 3))  # 2x3 matrix
print(f"Random Floats (0.0 to 1.0):\n{random_floats}\n")

# Random integers between a low and high bound
# rng.integers(low, high, size). Note: The high bound is EXCLUSIVE.
random_ints = rng.integers(0, 100, size=(5,))
print(f"Random Integers (0 to 99): {random_ints}")
print("-" * 40)


# ==========================================
# 3. STATISTICAL DISTRIBUTIONS
# Real-world data isn't perfectly uniform. It usually follows a bell curve (Normal Distribution).
# You need to know how to simulate this to test your statistical pipelines.
# ==========================================
print("\n--- 3. Normal (Gaussian) Distribution ---")

# rng.normal(loc, scale, size)
# loc = Mean (average or center of the bell curve)
# scale = Standard Deviation (how spread out the data is)
mean = 0
std_dev = 1
normal_data = rng.normal(mean, std_dev, size=5)

print(f"Normally Distributed Data (Mean={mean}, Std={std_dev}):\n{normal_data}")
# If we generated 10,000 of these and plotted them, it would look like a perfect bell curve.
print("-" * 40)


# ==========================================
# 4. SHUFFLING AND SAMPLING (Crucial for Machine Learning)
# Before training an AI, you must shuffle your dataset so the model doesn't 
# memorize the order of the data. You also need to pull random samples.
# ==========================================
print("\n--- 4. Shuffling and Sampling ---")
dataset = np.array(["Apples", "Bananas", "Cherries", "Dates", "Elderberries"])
print(f"Original Dataset: {dataset}")

# rng.choice() picks random elements. 
# replace=False means it won't pick the same item twice (like dealing cards).
sample = rng.choice(dataset, size=3, replace=False)
print(f"Random Sample of 3: {sample}\n")

# rng.shuffle() modifies the array IN-PLACE (it ruins the original order).
# If it's a 2D array, it only shuffles the rows, not the individual columns!
rng.shuffle(dataset)
print(f"Shuffled Dataset: {dataset}")
