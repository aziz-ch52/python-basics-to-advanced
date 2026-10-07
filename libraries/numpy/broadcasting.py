"""
NumPy Broadcasting Example

This script demonstrates Broadcasting in NumPy. Broadcasting is a feature 
within vectorization that allows arithmetic operations on arrays of different 
shapes. NumPy conceptually 'stretches' the smaller array to match the larger 
one without copying data in memory.

Prerequisites:
    pip install numpy
"""

import numpy as np


def main():
    print("--- DEMONSTRATING NUMPY BROADCASTING ---")

    # Shape: (5,) -> A 1D array representing item base prices
    base_prices = np.array([100, 250, 500, 750, 1200])

    # Shape: () -> A single numeric scalar value representing a 2% tax rate
    # Mathematically: 1.02 represents 100% of the price + 2% tax addition
    tax_multiplier = 1.02

    print(f"Base Prices Array Shape:   {base_prices.shape}")
    print(f"Tax Multiplier Scalar Shape: {np.shape(tax_multiplier)}\n")

    # BROADCASTING IN ACTION:
    # Because shapes do not match, NumPy automatically 'broadcasts' (stretches)
    # the scalar 1.02 into a matching array: [1.02, 1.02, 1.02, 1.02, 1.02]
    # It then performs a high-speed vectorized multiplication.
    taxed_prices = base_prices * tax_multiplier

    # Displaying the results
    print("Original Base Prices:      ", base_prices)
    print("Tax Applied:               2%")
    print("-----------------------------------------")
    print("Taxed Prices (Broadcasted):", np.round(taxed_prices, 2))


if __name__ == "__main__":
    main()
