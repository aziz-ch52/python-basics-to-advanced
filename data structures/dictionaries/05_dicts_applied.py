"""
=========================================================
05. APPLIED DICTIONARIES (FREQUENCY COUNTER)
=========================================================
This is a standard technical interview question and a core 
analytics task: taking a raw, messy array of items and 
aggregating them into a clean dictionary of frequency counts.
=========================================================
"""

# The Raw Data: A list of product categories purchased today.
purchases = ["Electronics", "Apparel", "Electronics", "Home", "Apparel", "Apparel", "Toys", "Home"]

print("--- 1. MANUAL AGGREGATION (THE ANALYST WAY) ---")

frequency_counter = {}

for category in purchases:
    # If the category is already in our dict, increment the count by 1
    if category in frequency_counter:
        frequency_counter[category] += 1
    # If it's a new category, add it to the dict and set the count to 1
    else:
        frequency_counter[category] = 1

print(f"Manual Aggregation: {frequency_counter}")


# ---------------------------------------------------------
# THE 'COLLECTIONS' MODULE (THE PROFESSIONAL WAY)
# ---------------------------------------------------------
print("\n--- 2. USING collections.Counter ---")
# Python has a built-in library specifically designed for this exact analytical task.
# Never write a manual frequency counter in production if you can use Counter.

from collections import Counter

# Instantly counts the frequencies and stores them in a specialized dictionary
professional_counter = Counter(purchases)

print(f"Counter Aggregation: {dict(professional_counter)}")

# Counter also unlocks advanced analytical methods instantly:
print(f"Top 2 most common categories: {professional_counter.most_common(2)}")
