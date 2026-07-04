"""
=========================================================
01. THE TRY-EXCEPT BLOCK (BASIC SAFETY NET)
=========================================================
In data ingestion, you will constantly receive bad data types.
If you try to cast a string like "N/A" into a float, Python 
will crash with a ValueError. 

The try-except block allows you to catch that crash, handle 
It gracefully and keep your pipeline running.
=========================================================
"""

print("--- 1. HANDLING MESSY DATA STRINGS ---")

# A simulated column of raw data scraped from a website
raw_prices = ["45.50", "120.00", "N/A", "89.99", "Missing", "50.25"]
cleaned_prices = []
error_count = 0

for price in raw_prices:
    # 1. TRY: Put the risky operation inside this block.
    try:
        clean_val = float(price)
        cleaned_prices.append(clean_val)
        
    # 2. EXCEPT: If the code in the 'try' block fails, this runs instead.
    except ValueError:
        print(f"[WARNING] Could not convert '{price}' to float. Skipping record.")
        error_count += 1

print("\n--- PIPELINE RESULTS ---")
print(f"Cleaned Data Array: {cleaned_prices}")
print(f"Total Corrupted Records Skipped: {error_count}")
