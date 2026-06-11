"""
=========================================================
04. SET COMPREHENSIONS (FAST CLEANING)
=========================================================
Similar to list comprehensions, but immediately enforces
uniqueness. 

Syntax: {expression for item in iterable if condition}
=========================================================
"""

print("--- STANDARDIZING AND DEDUPLICATING ---")

# Scenario: You scrape product categories, but the casing is a mess, 
# and there are hundreds of duplicates.
raw_categories = ["Electronics", " APPAREL ", "electronics", "Home ", "Apparel", "HOME"]

# In one line: strip whitespace, convert to lowercase, and drop all duplicates.
clean_unique_categories = {category.strip().lower() for category in raw_categories}

print(f"Raw count: {len(raw_categories)}")
print(f"Cleaned distinct categories: {clean_unique_categories}")


print("\n--- FILTERING UNIQUE VALUES ---")

# Scenario: Extract all unique system error codes, ignoring successful 200s
system_logs = [200, 404, 500, 200, 403, 500, 404]

# Keep only codes that are not 200, and store them as a distinct set
unique_errors = {code for code in system_logs if code != 200}

print(f"Distinct errors encountered: {unique_errors}")
