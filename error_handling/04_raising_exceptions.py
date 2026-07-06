"""
=========================================================
04. INTENTIONAL CRASHES (THE 'RAISE' KEYWORD)
=========================================================
Sometimes, you WANT your script to crash. 

If a financial dataset is supposed to have 10 columns, and 
today's file only has 9, you must halt the pipeline immediately. 
If you let it continue, it will overwrite good database tables 
with shifted, corrupted data.
=========================================================
"""

def validate_schema(data_row, expected_columns):
    """ Validates that incoming data matches expected infrastructure requirements."""
    
    actual_columns = len(data_row)
    
    if actual_columns != expected_columns:
        # The 'raise' keyword manually triggers an exception and halts the script.
        raise ValueError(
            f"SCHEMA MISMATCH: Expected {expected_columns} columns, "
            f"but received {actual_columns}. Pipeline halted."
        )
    
    print("[VALID] Schema matches expectations. Proceeding to load data.")
    return True

print("--- 1. VALID DATA ---")
valid_row = ["TXN-01", "2026-07-04", 450.00, "COMPLETED"]
validate_schema(valid_row, expected_columns=4)

print("\n--- 2. CORRUPTED DATA ---")
invalid_row = ["TXN-02", "2026-07-04", 450.00] # Missing the status column

try:
    # This will trigger the intentional crash we built
    validate_schema(invalid_row, expected_columns=4)
except ValueError as e:
    print(f"\n[ALERT] Caught the intentional crash: {e}")
