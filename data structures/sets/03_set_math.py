"""
=========================================================
03. SET MATH (DATASET COMPARISONS)
=========================================================
This is where Sets shine. You can compare millions of records
across two sets in milliseconds using mathematical operators.

Think of these as natively executed SQL Joins.
=========================================================
"""

# Imagine comparing last month's buyers to this month's buyers
jan_buyers = {"Alice", "Bob", "Charlie", "David"}
feb_buyers = {"Charlie", "David", "Eve", "Frank"}

# ---------------------------------------------------------
# 1. INTERSECTION (&) -> SQL INNER JOIN
# ---------------------------------------------------------
# Who bought in BOTH January and February?
repeat_customers = jan_buyers & feb_buyers
print(f"Intersection (Repeat): {repeat_customers}")


# ---------------------------------------------------------
# 2. DIFFERENCE (-) -> SQL LEFT ANTI JOIN
# ---------------------------------------------------------
# Who bought in January but NOT in February?
churned_customers = jan_buyers - feb_buyers
print(f"Difference (Churned): {churned_customers}")

# Note: Order matters! Who are the completely new buyers in Feb?
new_customers = feb_buyers - jan_buyers
print(f"Difference (Brand New): {new_customers}")


# ---------------------------------------------------------
# 3. UNION (|) -> SQL FULL OUTER JOIN
# ---------------------------------------------------------
# Give me a master list of EVERY unique customer across both months.
all_unique_buyers = jan_buyers | feb_buyers
print(f"Union (Master List): {all_unique_buyers}")


# ---------------------------------------------------------
# 4. SYMMETRIC DIFFERENCE (^) -> EXCLUSIVE OR
# ---------------------------------------------------------
# Who bought in exactly ONE of the months, but NOT both?
one_time_buyers = jan_buyers ^ feb_buyers
print(f"Symmetric Diff (One-Timers): {one_time_buyers}")
