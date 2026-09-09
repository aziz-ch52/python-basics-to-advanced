"""
=========================================================
02. GENERATORS & THE YIELD KEYWORD
=========================================================
A standard function uses 'return' to send back ALL data at once.
A Generator uses 'yield' to pause execution and send back ONE 
piece of data at a time.

This is the most important concept in Python memory management.
=========================================================
"""

def standard_extraction(limit):
    """ Loads everything into RAM at once."""
    result = []
    for i in range(limit):
        result.append(i)
    return result

def generator_extraction(limit):
    """Yields one row at a time. Memory footprint is near zero."""
    for i in range(limit):
        yield i

print("--- 1. STANDARD RETURN ---")
# The entire list is built in memory before printing
full_list = standard_extraction(5)
print(f"List loaded into memory: {full_list}")

print("\n--- 2. GENERATOR YIELD ---")
# The generator does not hold the data in memory. It generates it on the fly.
data_stream = generator_extraction(5)
print(f"Generator Object created: {data_stream}")

# We must iterate over it to actually compute and extract the values
for value in data_stream:
    print(f"Yielded on the fly: {value}")
