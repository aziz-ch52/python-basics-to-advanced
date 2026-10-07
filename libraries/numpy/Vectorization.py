"""
NumPy Vectorization Example

This script demonstrates Vectorization in NumPy. Vectorization allows us to
perform element-by-element mathematical operations on entire arrays at once.
The looping happens under the hood in optimized C code, bypassing slow Python loops.

Prerequisites:
    pip install numpy
"""

import numpy as np


def main():
    print("--- DEMONSTRATING NUMPY VECTORIZATION ---")

    # Imagine managing an e-commerce store with 5 core products
    # Both arrays have the same shape: (5,)
    base_prices = np.array([100, 250, 500, 750, 1200])
    shipping_fees = np.array([5, 12, 20, 25, 45])

    print(f"Base Prices Array Shape:  {base_prices.shape}")
    print(f"Shipping Fees Array Shape: {shipping_fees.shape}\n")

    # VECTORIZATION IN ACTION:
    # NumPy adds the two arrays element-by-element instantly.
    # [100+5, 250+12, 500+20, 750+25, 1200+45]
    final_checkout_prices = base_prices + shipping_fees

    # Displaying the results
    print("Original Base Prices:   ", base_prices)
    print("Individual Shipping:    ", shipping_fees)
    print("-----------------------------------------")
    print("Final Checkout Prices:  ", final_checkout_prices)


if __name__ == "__main__":
    main()
