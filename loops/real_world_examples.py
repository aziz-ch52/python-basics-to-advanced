"""
========================================
REAL WORLD LOOP EXAMPLES
========================================

Purpose:
✔ Apply loops to real problems
✔ Combine loops + conditionals
✔ Build problem-solving ability
"""


# ========================================
# 1. PASSWORD RETRY SYSTEM
# ========================================

"""
Logic:
✔ Keep asking until correct password
✔ Limit attempts
"""

correct_password = "1234"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access Granted")
        break
    else:
        attempts -= 1
        print("Wrong password. Attempts left:", attempts)

if attempts == 0:
    print("Account Locked")


# ========================================
# 2. MENU-DRIVEN PROGRAM
# ========================================

"""
Logic:
✔ Show menu repeatedly
✔ Stop when user chooses exit
"""

while True:
    print("\n1. Say Hello")
    print("2. Add Numbers")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Hello!")

    elif choice == 2:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print("Sum:", a + b)

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice")


# ========================================
# 3. SUM OF DIGITS
# ========================================

"""
Logic:
✔ Extract digits using % and //
✔ Add them
"""

num = int(input("Enter number: "))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10

print("Sum of digits:", total)


# ========================================
# 4. SEARCH IN LIST
# ========================================

"""
Logic:
✔ Loop through list
✔ Check if element exists
"""

numbers = [10, 20, 30, 40]
target = int(input("Enter number to search: "))

found = False

for num in numbers:
    if num == target:
        found = True
        break

if found:
    print("Element Found")
else:
    print("Not Found")


# ========================================
# 5. COUNT FREQUENCY
# ========================================

"""
Logic:
✔ Count occurrences of element
"""

numbers = [1, 2, 2, 3, 2, 4]
target = 2

count = 0

for num in numbers:
    if num == target:
        count += 1

print("Frequency:", count)


# ========================================
# 6. FACTORIAL CALCULATION
# ========================================

"""
Logic:
✔ Multiply numbers from 1 to n
"""

n = int(input("Enter number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial:", factorial)


# ========================================
# 7. NUMBER REVERSAL
# ========================================

"""
Logic:
✔ Extract digits and rebuild number
"""

num = int(input("Enter number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed:", reverse)


# ========================================
# 8. PRIME NUMBER CHECK
# ========================================

"""
Logic:
✔ Check divisibility from 2 to n-1
"""

num = int(input("Enter number: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime Number")
else:
    print("Not Prime")


# ========================================
# 9. MULTIPLICATION TABLE GENERATOR
# ========================================

num = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# ========================================
# 10. COMMON MISTAKES
# ========================================

"""
❌ Infinite loops
❌ Forgetting break
❌ Wrong loop condition
❌ Not updating variables
"""


# ========================================
# 11. BEST PRACTICES
# ========================================

"""
✔ Break problems into steps
✔ Use flags (like found = False)
✔ Keep loops simple
✔ Test with different inputs
"""


# ========================================
# FINAL CHALLENGE
# ========================================

"""
Build yourself:

✔ ATM system with retry limit
✔ Calculator with loop menu
✔ Guess the number game
"""
