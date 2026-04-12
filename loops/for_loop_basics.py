"""
========================================
FOR LOOP BASICS - COMPLETE GUIDE
========================================

WHAT IS A FOR LOOP?

A for loop is used to iterate over a sequence
(list, string, range, etc.)

WHEN TO USE?

✔ When the number of iterations is known
✔ When looping over a collection (list, string)
✔ When you want a clean, readable iteration

REAL THINKING:
"For each item in a collection → do something."
"""


# ========================================
# 1. BASIC FOR LOOP
# ========================================

# Loop from 0 to 4
for i in range(5):
    print("Iteration:", i)

# Flow:
# i = 0 → print
# i = 1 → print
# ...
# i = 4 → print


# ========================================
# 2. LOOPING THROUGH LIST
# ========================================

numbers = [10, 20, 30, 40]

for num in numbers:
    print("Number:", num)


# ========================================
# 3. LOOPING THROUGH A STRING
# ========================================

name = "Aziz"

for char in name:
    print(char)


# ========================================
# 4. USING INDEX (IMPORTANT)
# ========================================

numbers = [5, 10, 15]

# Access index using range + len
for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])


# ========================================
# 5. SUM OF NUMBERS
# ========================================

numbers = [1, 2, 3, 4, 5]

total = 0

for num in numbers:
    total += num

print("Total Sum:", total)


# ========================================
# 6. COUNTING EXAMPLE
# ========================================

count = 0

for i in range(1, 11):
    count += 1

print("Count:", count)


# ========================================
# 7. REAL-LIFE SCENARIO
# ========================================

# Calculate the total price of items
prices = [100, 200, 300]

total = 0

for price in prices:
    total += price

print("Total Bill:", total)


# ========================================
# 8. COMMON MISTAKES
# ========================================

# ❌ Forgetting colon :
# for i in range(5)

# ❌ Wrong indentation

# ❌ Misunderstanding range (range(5) = 0 to 4)


# ========================================
# 9. BEST PRACTICES
# ========================================

"""
✔ Use meaningful variable names
✔ Use direct iteration when possible
✔ Avoid unnecessary index usage
✔ Keep loops simple
"""


# ========================================
# 10. MINI PRACTICE
# ========================================

# Print squares of numbers 1 to 5

for i in range(1, 6):
    print("Square of", i, "=", i * i)

