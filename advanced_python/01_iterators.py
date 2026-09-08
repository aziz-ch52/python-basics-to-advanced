"""
=========================================================
01. ITERABLES VS ITERATORS
=========================================================
Under the hood, a 'for' loop doesn't just magically read a list. 
It converts the list into an iterator and calls next() on it 
until it runs out of data.

Understanding this allows you to manually control data flow 
one record at a time.
=========================================================
"""

print("--- 1. THE UNDERLYING MECHANICS ---")

# This is an Iterable (it holds data, but doesn't track state)
raw_dataset = ["Row 1", "Row 2", "Row 3"]

# This is an Iterator (it tracks exactly where you are in the data)
data_stream = iter(raw_dataset)

print(next(data_stream)) # Pulls Row 1
print(next(data_stream)) # Pulls Row 2

print("\n--- 2. MANUAL DATA EXTRACTION ---")
# We can pull the next record exactly when we need it, without a loop.
current_record = next(data_stream)
print(f"Manually pulled: {current_record}")

# If we call next() again, the script will crash with a StopIteration error
# because the stream is empty. This is exactly how 'for' loops know when to stop.
