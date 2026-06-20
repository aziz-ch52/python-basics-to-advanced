"""
=========================================================
04. VARIABLE SCOPE (LOCAL VS. GLOBAL)
=========================================================
Scope determines where variables can be accessed. 
A variable created inside a function is LOCAL and ceases 
to exist when the function finishes. 

Understanding this prevents hours of debugging when your 
variables mysteriously return 'undefined'.
=========================================================
"""

# ---------------------------------------------------------
# 1. LOCAL VS GLOBAL
# ---------------------------------------------------------
print("--- 1. LOCAL VS GLOBAL VARIABLES ---")

# This is a GLOBAL variable. Accessible anywhere.
system_status = "ONLINE"

def process_data():
    # This is a LOCAL variable. It only exists inside this block.
    rows_processed = 5000
    print(f"[Inside Function] System is {system_status}")
    print(f"[Inside Function] Processed {rows_processed} rows.")

process_data()

# ❌ Trying to print 'rows_processed' here would crash the script.
# print(rows_processed) # NameError: name 'rows_processed' is not defined


# ---------------------------------------------------------
# 2. THE 'GLOBAL' KEYWORD (USE WITH CAUTION)
# ---------------------------------------------------------
print("\n--- 2. MODIFYING GLOBALS ---")

error_count = 0

def log_error():
    # Without the 'global' keyword, Python would create a new LOCAL 
    # variable called 'error_count' and leave the global one at 0.
    global error_count
    error_count += 1
    print("Error logged.")

log_error()
log_error()

print(f"Total Pipeline Errors: {error_count}")
print("Note: Heavy reliance on 'global' is bad practice. Return values instead.")
