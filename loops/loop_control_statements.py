"""
========================================
LOOP CONTROL STATEMENTS - COMPLETE GUIDE
========================================

These statements control how loops behave.

Types:
✔ break    → stops the loop completely
✔ continue → skips current iteration
✔ pass     → does nothing (placeholder)
"""


# ========================================
# 1. BREAK STATEMENT
# ========================================

"""
WHAT IS BREAK?

Stops the loop immediately when the condition is met.
"""

for i in range(10):
    if i == 5:
        print("Stopping at:", i)
        break   # loop stops here

    print(i)

# Output: 0 1 2 3 4


# ========================================
# 2. BREAK (REAL-LIFE SCENARIO)
# ========================================

# Stop when correct password is entered
correct_password = "1234"

while True:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access Granted")
        break   # exit loop
    else:
        print("Try again")


# ========================================
# 3. CONTINUE STATEMENT
# ========================================

"""
WHAT IS CONTINUE?

Skips current iteration and moves to next loop cycle.
"""

for i in range(5):
    if i == 2:
        continue   # skip this iteration

    print(i)

# Output: 0 1 3 4


# ========================================
# 4. CONTINUE (REAL-LIFE SCENARIO)
# ========================================

# Print only even numbers
for i in range(1, 11):
    if i % 2 != 0:
        continue

    print("Even:", i)


# ========================================
# 5. PASS STATEMENT
# ========================================

"""
WHAT IS PASS?

Does nothing.
Used as a placeholder for future code.
"""

for i in range(3):
    pass   # no operation


# Example usage
if True:
    pass   # code will be added later


# ========================================
# 6. COMBINING CONTROL STATEMENTS
# ========================================

# Skip negative numbers, stop at zero
numbers = [5, -2, 8, 0, 3]

for num in numbers:
    if num < 0:
        continue

    if num == 0:
        print("Stopping at zero")
        break

    print("Number:", num)


# ========================================
# 7. COMMON MISTAKES
# ========================================

# ❌ Using break accidentally → loop stops early
# ❌ Overusing continue → skipping too much logic
# ❌ Misunderstanding pass (it does nothing)


# ========================================
# 8. BEST PRACTICES
# ========================================

"""
✔ Use break to exit early when needed
✔ Use continue to skip unwanted cases
✔ Use pass only as a placeholder
✔ Keep loop logic clear and readable
"""


# ========================================
# 9. MINI PRACTICE
# ========================================

# Print numbers from 1–10
# Skip multiples of 3
# Stop if the number is 8

for i in range(1, 11):
    if i % 3 == 0:
        continue

    if i == 8:
        break

    print(i)
