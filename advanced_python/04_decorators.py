"""
=========================================================
04. DECORATORS (PIPELINE METRICS)
=========================================================
A Decorator is a function that wraps around another function 
to modify its behavior. 

In Data Analytics, you use decorators constantly to measure 
how long your ETL functions take to run without altering the 
core logic of the functions themselves.
=========================================================
"""
import time

# 1. Define the Decorator (The Wrapper)
def timer_decorator(func):
    """A wrapper that calculates function execution time."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # Execute the actual function
        result = func(*args, **kwargs)
        
        end_time = time.time()
        print(f"[METRIC] Function '{func.__name__}' completed in {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

# 2. Apply the Decorator using the @ symbol
@timer_decorator
def heavy_computation():
    """Simulates a complex data aggregation."""
    print("Starting massive calculation...")
    total = sum(x**2 for x in range(2000000))
    return total

print("--- EXECUTING DECORATED FUNCTION ---")
final_result = heavy_computation()
