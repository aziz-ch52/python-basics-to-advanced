"""
=========================================================
02. ARGUMENTS & DEFAULT PARAMETERS
=========================================================
Functions need inputs (arguments) to process data. 
You must master the difference between positional arguments 
(where order matters) and keyword arguments (where names matter), 
as well as setting default values to prevent crashes.
=========================================================
"""

# ---------------------------------------------------------
# 1. DEFAULT PARAMETERS (CRITICAL FOR ETL)
# ---------------------------------------------------------
print("--- 1. DEFAULTS & KEYWORDS ---")

# By setting 'retries=3', we make this argument optional. 
# If the user doesn't provide it, the script defaults to 3 instead of crashing.
def extract_data(source_url, format_type, retries=3):
    """Simulates extracting data from a source."""
    print(f"Connecting to {source_url}...")
    print(f"Format expected: {format_type}")
    print(f"Max retries allowed: {retries}")
    return True

print("\n--- Positional Call (Order strictly matters) ---")
# Arguments map exactly to the order defined in the function
extract_data("api.datasource.com", "JSON") 

print("\n--- Keyword Call (Order does not matter) ---")
# Explicitly naming the arguments makes your code highly readable
extract_data(format_type="CSV", source_url="ftp.server.net", retries=5)

# ---------------------------------------------------------
# 2. THE MUTABLE DEFAULT TRAP (DANGER)
# ---------------------------------------------------------
print("\n--- 2. THE MUTABLE DEFAULT TRAP ---")

# ❌ NEVER use a mutable object (like an empty list []) as a default argument.
# It is evaluated ONCE when the script loads, meaning subsequent calls will share the same list.
def bad_logger(error_msg, log_list=[]):
    log_list.append(error_msg)
    return log_list

print(f"Bad call 1: {bad_logger('Timeout')}")
print(f"Bad call 2: {bad_logger('404 Error')}") # Notice 'Timeout' is still there!

# ✅ THE PROFESSIONAL FIX: Use None.
def good_logger(error_msg, log_list=None):
    if log_list is None:
        log_list = [] # Created fresh on every call
    log_list.append(error_msg)
    return log_list

print(f"\nGood call 1: {good_logger('Timeout')}")
print(f"Good call 2: {good_logger('404 Error')}")

