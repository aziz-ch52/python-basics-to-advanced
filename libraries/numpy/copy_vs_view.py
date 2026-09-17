"""
NumPy: Copy vs. View

This script demonstrates the critical difference between copying an array 
and creating a view of an array in NumPy.

Key Differences:
1. COPY: A deep copy of the original array. It owns its data. Changes to the 
   copy do NOT affect the original array, and vice versa.
2. VIEW: A shallow reference to the original array. It does NOT own its data. 
   Changes to the view DIRECTLY affect the original array. (Note: Slicing a 
   NumPy array creates a view, unlike standard Python lists where slicing creates a copy).
"""

import numpy as np

def demonstrate_copy():
    print("--- 1. THE COPY ---")
    
    # Initialize the original array
    original_array = np.array([23, 43, 45, 76, 67])
    print(f"Initial Original Array: {original_array}")

    # Create a true copy using the .copy() method
    copied_array = original_array.copy()
    
    # Modify the copied array
    copied_array[2] = 354
    print("\nAction: Changed index 2 of the COPIED array to 354.")

    # Output the results
    print(f"Original Array now:     {original_array}")
    print(f"Copied Array now:       {copied_array}")
    print("Takeaway: The original array remains untouched because the copy owns its own data.\n")


def demonstrate_view():
    print("--- 2. THE VIEW (Slicing) ---")
    
    # Initialize a new original array
    source_array = np.array([23, 43, 45, 65, 98, 68])
    print(f"Initial Source Array:   {source_array}")

    # Slicing in NumPy creates a VIEW, not a new array
    view_array = source_array[1:4]
    print(f"Initial View Array:     {view_array} (Sliced from index 1 to 3)")

    # Modify the view
    view_array[1] = 1000
    print("\nAction: Changed index 1 of the VIEW array to 1000.")

    # Output the results
    print(f"Source Array now:       {source_array}")
    print(f"View Array now:         {view_array}")
    print("Takeaway: The source array WAS MUTATED because the view shares the exact same memory.\n")


def check_ownership():
    print("--- 3. VERIFYING OWNERSHIP (.base attribute) ---")
    # You can check if an array owns its data by looking at the `.base` attribute.
    # If it returns None, the array owns the data (it's a copy/original). 
    # If it returns an array, it does not own the data (it's a view).
    
    arr = np.array([1, 2, 3, 4, 5])
    my_copy = arr.copy()
    my_view = arr[1:3]
    
    print(f"my_copy.base returns: {my_copy.base} -> (Owns its data)")
    print(f"my_view.base returns: {my_view.base} -> (Does NOT own its data, points to original)")


if __name__ == "__main__":
    demonstrate_copy()
    demonstrate_view()
    check_ownership()
