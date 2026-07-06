"""
=========================================================
05. CUSTOM EXCEPTIONS (OOP INTEGRATION)
=========================================================
Professional Python libraries (like Pandas or requests) don't 
just use generic ValueErrors. They build their own custom 
error classes for maximum clarity.

You do this by inheriting from Python's built-in Exception class.
=========================================================
"""

# ---------------------------------------------------------
# 1. DEFINING CUSTOM ERROR CLASSES
# ---------------------------------------------------------
class DataValidationError(Exception):
    """ Raised when data does not meet business logic rules."""
    pass

class MissingColumnError(Exception):
    """ Raised when a required column is missing from a dataset."""
    pass


# ---------------------------------------------------------
# 2. IMPLEMENTING CUSTOM ERRORS IN A PIPELINE
# ---------------------------------------------------------
def process_user_age(age_val):
    """Simulates business logic validation for user data."""
    
    # 1. Type validation
    if not isinstance(age_val, int):
        # We can still use built-in errors for generic Python issues
        raise TypeError(f"Age must be an integer, got {type(age_val).__name__}")
        
    # 2. Business logic validation (Using our custom error)
    if age_val < 0 or age_val > 120:
        raise DataValidationError(f"Invalid age detected: {age_val}. Must be between 0 and 120.")
        
    print(f"[SUCCESS] Age {age_val} is valid and stored.")


print("--- TESTING CUSTOM EXCEPTIONS ---")

test_cases = [25, 150, -5, 30]

for test in test_cases:
    try:
        print(f"\nEvaluating age: {test}")
        process_user_age(test)
    
    # We can now catch our highly specific custom error
    except DataValidationError as e:
        print(f"[BUSINESS LOGIC EXCEPTION] -> {e}")
