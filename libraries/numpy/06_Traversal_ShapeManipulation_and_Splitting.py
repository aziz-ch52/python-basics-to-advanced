# 10. Iteration & Traversal
for x in np.nditer(arr_2d, order='C'):  # Flat C-contiguous iteration
    pass 

# 11. Shape Manipulation & Transformations
reshaped = arr_1d.reshape(2, 2)         # Changes shape without altering data
flattened = arr_2d.flatten()            # Returns a 1D copy
raveled = arr_2d.ravel()                # Returns a 1D view (if possible)
transposed = arr_2d.T                   # Swaps rows and columns
expanded = np.expand_dims(arr_1d, axis=0) # Adds a unit dimension (shape becomes 1x4)

# 12. Splitting & Concatenation
a = np.array([[1, 2]])
b = np.array([[3, 4]])
joined_v = np.vstack((a, b))            # Stack vertically
joined_h = np.hstack((a, b))            # Stack horizontally
stacked = np.stack((a, b), axis=0)      # Creates a new axis

split_arr = np.split(arr_1d, 2)         # Splits into 2 equal sub-arrays
