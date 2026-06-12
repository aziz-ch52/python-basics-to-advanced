"""
=========================================================
03. NAMED TUPLES (ADVANCED RECORDS)
=========================================================
Standard tuples require you to access data by index (e.g., row[1]).
This gets confusing in wide datasets. 

'namedtuple' from the 'collections' module allows you to access 
fields by name, making your code infinitely more readable 
while maintaining strict immutability.
=========================================================
"""

from collections import namedtuple

print("--- 1. DEFINING A NAMED TUPLE ---")

# Step 1: Define the "blueprint" (Schema)
# Arguments: The name of the tuple class, and a string of field names
CustomerRecord = namedtuple("CustomerRecord", "id name tier lifetime_value")

# Step 2: Instantiate records based on the blueprint
customer_1 = CustomerRecord(id=101, name="John Doe", tier="Gold", lifetime_value=5000.50)
customer_2 = CustomerRecord(id=102, name="Jane Smith", tier="Platinum", lifetime_value=12500.00)

print(f"Record 1 created: {customer_1}")


print("\n--- 2. ACCESSING DATA BY NAME ---")

# ❌ The Old Way (Standard Tuple): print(customer_1[2])
# ✅ The Professional Way: 
print(f"Customer 1 Tier: {customer_1.tier}")
print(f"Customer 2 LTV: ${customer_2.lifetime_value}")


print("\n--- 3. IMMUTABILITY REMAINS ---")

# Just like standard tuples, they cannot be mutated.
# customer_1.tier = "Silver"  # ❌ This will throw an AttributeError

print("Like standard tuples, namedtuples are strictly read-only.")
