"""
========================================
REAL WORLD CONDITIONAL EXAMPLES
========================================

Purpose:
✔ Apply all conditional concepts together
✔ Build real-life logic
✔ Think like a developer, not a student
"""


# ========================================
# 1. LOGIN SYSTEM
# ========================================

"""
Logic:
✔ Check username
✔ Check password
✔ Allow or deny access
"""

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")


# ========================================
# 2. ATM WITHDRAWAL SYSTEM
# ========================================

"""
Logic:
✔ Verify PIN
✔ Check balance
✔ Allow withdrawal
"""

balance = 5000
correct_pin = 1234

entered_pin = int(input("Enter PIN: "))
amount = int(input("Enter withdrawal amount: "))

if entered_pin == correct_pin:
    if amount <= balance:
        print("Withdrawal Successful")
        balance -= amount
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")


# ========================================
# 3. GRADE SYSTEM
# ========================================

"""
Logic:
✔ Assign grade based on marks
✔ Use proper order (important)
"""

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# ========================================
# 4. SIMPLE E-COMMERCE DISCOUNT SYSTEM
# ========================================

"""
Logic:
✔ Apply discount based on cart value
"""

cart_total = float(input("Enter cart total: "))

if cart_total >= 5000:
    discount = 20
elif cart_total >= 2000:
    discount = 10
elif cart_total >= 1000:
    discount = 5
else:
    discount = 0

final_amount = cart_total - (cart_total * discount / 100)

print("Discount:", discount, "%")
print("Final Amount:", final_amount)


# ========================================
# 5. LEAP YEAR CHECK
# ========================================

"""
Logic:
✔ Divisible by 4 AND not by 100
✔ OR divisible by 400
"""

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# ========================================
# 6. NUMBER CLASSIFICATION
# ========================================

"""
Logic:
✔ Positive / Negative / Zero
✔ Even / Odd (nested logic)
"""

num = int(input("Enter number: "))

if num > 0:
    print("Positive")

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif num < 0:
    print("Negative")
else:
    print("Zero")


# ========================================
# 7. SIMPLE ROLE-BASED ACCESS
# ========================================

"""
Logic:
✔ Check login
✔ Then check the role
"""

user = input("Enter username: ")
role = input("Enter role (admin/user): ")

if user == "admin":
    if role == "admin":
        print("Full Access")
    else:
        print("Limited Access")
else:
    print("Guest Access")


# ========================================
# 8. ELIGIBILITY SYSTEM (LOAN / JOB)
# ========================================

"""
Logic:
✔ Age check
✔ Income check
✔ Credit score check
"""

age = int(input("Enter age: "))
income = int(input("Enter income: "))
credit_score = int(input("Enter credit score: "))

if age >= 18 and income >= 25000 and credit_score >= 700:
    print("Eligible")
else:
    print("Not Eligible")


# ========================================
# 9. COMMON MISTAKES
# ========================================

"""
❌ Wrong condition order
❌ Missing type conversion
❌ Overcomplicated logic
❌ Not handling edge cases
"""


# ========================================
# 10. BEST PRACTICES
# ========================================

"""
✔ Break problems into steps
✔ Think before coding
✔ Use meaningful variables
✔ Keep logic readable
✔ Test multiple inputs
"""


# ========================================
# FINAL CHALLENGE (IMPORTANT)
# ========================================

"""
Build your own:
✔ Login system with 3 users
✔ Shopping cart with tax + discount
✔ Student result system (with pass/fail + grade)
"""
