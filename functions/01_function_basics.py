"""
=========================================================
01. FUNCTION BASICS & DOCSTRINGS
=========================================================
A function is a reusable block of code that only runs when called.
In data pipelines, you use functions to isolate specific tasks
like 'clean_data', 'calculate_metrics', or 'load_to_database'.

This file also introduces 'Docstrings'—the professional standard 
for documenting what your function does.
=========================================================
"""

# ---------------------------------------------------------
# 1. DEFINING A PROFESSIONAL FUNCTION
# ---------------------------------------------------------
print("--- 1. BASIC FUNCTION WITH DOCSTRING ---")

def calculate_average(data_list):
    """
    Calculates the average of a list of numbers.
    
    Args:
        data_list (list): A list of numerical values.
        
    Returns:
        float: The calculated average, or 0 if the list is empty.
    """
    if not data_list:
        return 0.0
    
    total = sum(data_list)
    average = total / len(data_list)
    
    # The 'return' keyword sends data BACK to wherever the function was called.
    # Without 'return', a function evaluates to None.
    return average

# ---------------------------------------------------------
# 2. CALLING THE FUNCTION
# ---------------------------------------------------------
print("\n--- 2. EXECUTION ---")

daily_sales = [250, 300, 150, 400, 500]
empty_dataset = []

# You must assign the returned value to a variable to use it
avg_sales = calculate_average(daily_sales)
avg_empty = calculate_average(empty_dataset)

print(f"Average Sales: ${avg_sales:.2f}")
print(f"Empty Dataset Output: {avg_empty}")

