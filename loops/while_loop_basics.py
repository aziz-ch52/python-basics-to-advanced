"""
========================================
WHILE LOOP BASICS - COMPLETE GUIDE
========================================

WHAT IS A WHILE LOOP?

A while loop runs as long as a condition is True.

Syntax:
while condition:
    code block


WHEN TO USE?

✔ When number of iterations is NOT fixed
✔ When loop depends on condition (user input, state)
✔ When you don’t know how many times loop should run

REAL THINKING:
"Keep doing this UNTIL condition becomes False"
"""


# ========================================
# 1. BASIC WHILE LOOP
# ========================================

i = 0

# Flow:
# Step 1 → Check condition (i < 5)
# Step 2 → If True → execute
# Step 3 → Update i
while i < 5:
    print("Iteration:", i)
    i += 1   # IMPORTANT (update condition)


# ========================================
# 2. COUNTING EXAMPLE
# ========================================

num = 1

while num <= 5:
    print(num)
    num += 1


# ========================================
# 3. SUM USING WHILE LOOP
# ========================================

i = 1
total = 0

while i <= 5:
    total += i
    i += 1

print("Sum:", total)


# ========================================
# 4. USER INPUT CONTROLLED LOOP
# ========================================

# Loop until user enters 0
num = int(input("Enter number (0 to stop): "))

while num != 0:
    print("You entered:", num)
    num = int(input("Enter number (0 to stop): "))


# ========================================
# 5. INFINITE LOOP (IMPORTANT)
# ========================================

"""
An infinite loop runs forever if condition never becomes False.
"""

# ❌ Example (DON'T RUN)
# while True:
#     print("This runs forever")


# ========================================
# 6. CONTROLLED INFINITE LOOP
# ========================================

# Controlled using break
while True:
    user_input = input("Type 'exit' to stop: ")

    if user_input == "exit":
        print("Loop stopped")
        break


# ========================================
# 7. REAL-LIFE SCENARIO (PASSWORD CHECK)
# ========================================

correct_password = "1234"
entered_password = ""

# Keep asking until correct password
while entered_password != correct_password:
    entered_password = input("Enter password: ")

    if entered_password != correct_password:
        print("Wrong password, try again")

print("Access Granted")


# ========================================
# 8. COMMON MISTAKES
# ========================================

# ❌ Forgetting update → infinite loop
# i = 0
# while i < 5:
#     print(i)   # i never changes

# ❌ Wrong condition

# ❌ Not handling exit condition


# ========================================
# 9. BEST PRACTICES
# ========================================

"""
✔ Always update loop variable
✔ Avoid unnecessary infinite loops
✔ Use break for control
✔ Keep conditions clear
"""


# ========================================
# 10. MINI PRACTICE
# ========================================

# Reverse a number

num = int(input("Enter number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed Number:", reverse)
