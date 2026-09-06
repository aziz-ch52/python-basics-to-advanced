import numpy as np

# 1. Base Array
arr = np.array([10, 20, 30, 40, 50])

# 2. Accessing Elements
first_val = arr[0]
last_val = arr[-1]
slice_window = arr[1:4]
step_slice = arr[::2]
clamped_slice = arr[2:100]  # Out-of-bounds slice auto-clamps to end

# 3. Updating Elements
u1 = arr.copy()
u1[0] = 999  # Single update

u2 = arr.copy()
u2[1:3] = [200, 300]  # Multi-element update via slice

u3 = arr.copy()
u3[3:] = 0  # Broadcast update

u4 = arr.copy()
u4[2:100] = 777  # Out-of-bounds slice update (silently clamped)

# 4. Iterating Elements
# Python loop iteration (educational only)
loop_outputs = []
for val in arr:
    loop_outputs.append(val)

# Vectorized operations (Analytics standard - no loops)
vectorized_mult = arr * 2
vectorized_mask = arr[arr > 25]


# ----------------------------------------------------
# Outputs with actual values in comments
# ----------------------------------------------------

# Accessing
print("first_val:\n", first_val)
# 10

print("\nlast_val:\n", last_val)
# 50

print("\nslice_window:\n", slice_window)
# [20 30 40]

print("\nstep_slice:\n", step_slice)
# [10 30 50]

print("\nclamped_slice:\n", clamped_slice)
# [30 40 50]

# Updating
print("\nu1 (single update):\n", u1)
# [999  20  30  40  50]

print("\nu2 (multi update):\n", u2)
# [ 10 200 300  40  50]

print("\nu3 (broadcast update):\n", u3)
# [10 20 30  0  0]

print("\nu4 (clamped out-of-bounds update):\n", u4)
# [ 10  20 777 777 777]

# Iterating
print("\nloop_outputs:\n", loop_outputs)
# [10, 20, 30, 40, 50]

print("\nvectorized_mult (all elements multiplied without loop):\n", vectorized_mult)
# [ 20  40  60  80 100]

print("\nvectorized_mask (filtered > 25 without loop):\n", vectorized_mask)
# [30 40 50]
