"""
========================================
LOOPS PRACTICE - TEST YOUR SKILLS
========================================

RULES:
✔ Do NOT look at solutions immediately
✔ Try yourself first
✔ Break problem into steps
✔ Use print() to debug

If you struggle → GOOD (that’s where learning happens)
"""


# ========================================
# 1. SUM OF FIRST N NUMBERS
# ========================================

"""
Input: n = 5
Output: 1+2+3+4+5 = 15
"""

n = int(input("Enter n: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Sum:", total)


# ========================================
# 2. FACTORIAL
# ========================================

"""
Input: 5
Output: 120
"""

n = int(input("Enter number: "))

fact = 1
for i in range(1, n + 1):
    fact *= i

print("Factorial:", fact)


# ========================================
# 3. FIBONACCI SERIES
# ========================================

"""
0 1 1 2 3 5 8 ...
"""

n = int(input("Enter number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# ========================================
# 4. COUNT DIGITS
# ========================================

num = int(input("Enter number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print("Digits:", count)


# ========================================
# 5. PALINDROME NUMBER
# ========================================

num = int(input("Enter number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# ========================================
# 6. PRIME NUMBERS IN RANGE
# ========================================

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end=" ")


# ========================================
# 7. MULTIPLICATION TABLE (USER INPUT)
# ========================================

num = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# ========================================
# 8. SUM OF DIGITS
# ========================================

num = int(input("Enter number: "))
total = 0

while num > 0:
    total += num % 10
    num //= 10

print("Sum of digits:", total)


# ========================================
# 9. REVERSE STRING
# ========================================

text = input("Enter string: ")
reverse = ""

for char in text:
    reverse = char + reverse

print("Reversed:", reverse)


# ========================================
# 10. GUESS THE NUMBER GAME
# ========================================

"""
Hint-based guessing game
"""

secret = 7

while True:
    guess = int(input("Guess number (1-10): "))

    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")


# ========================================
# 11. STAR PATTERN (CHALLENGE)
# ========================================

"""
*
**
***
****
*****
"""

n = int(input("Enter rows: "))

for i in range(1, n + 1):
    print("*" * i)


# ========================================
# 12. ADVANCED CHALLENGE
# ========================================

"""
Find largest number in list WITHOUT using max()
"""

numbers = [10, 45, 23, 89, 67]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)
