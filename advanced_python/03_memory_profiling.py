"""
=========================================================
03. PROVING THE MEMORY DIFFERENCE
=========================================================
This script proves why Data Engineers use Generators. 
We will compare the RAM usage of a standard List comprehension 
vs a Generator expression when processing 1 million records.
=========================================================
"""
import sys

print("--- MEMORY FOOTPRINT COMPARISON ---")

# 1. Standard List Comprehension (Uses brackets [])
# This forces Python to calculate all 1,000,000 numbers and store them in RAM.
list_of_data = [x for x in range(1000000)]

# 2. Generator Expression (Uses parentheses ())
# This tells Python HOW to calculate the numbers, but waits until asked.
generator_of_data = (x for x in range(1000000))

# Let's check the exact byte size in memory
list_size_mb = sys.getsizeof(list_of_data) / (1024 * 1024)
gen_size_bytes = sys.getsizeof(generator_of_data)

print(f"List Size in RAM:      {list_size_mb:.2f} MB")
print(f"Generator Size in RAM: {gen_size_bytes} Bytes")

print("\n[CONCLUSION] The List consumed Megabytes of RAM.")
print("[CONCLUSION] The Generator consumed slightly over 100 Bytes. It is infinitely more scalable.")
