"""
========================================
LOGICAL CONDITIONS - COMPLETE GUIDE
========================================

WHAT ARE LOGICAL OPERATORS?

Used to combine multiple conditions.

Operators:
✔ and → True if BOTH conditions are True
✔ or  → True if ANY ONE condition is True
✔ not → Reverses the condition


WHEN TO USE?

Use logical operators when:
✔ You have multiple conditions to check
✔ You want to avoid nested if (cleaner code)
✔ You want compact decision logic

REAL-LIFE THINKING:
"Eligible if age ≥ 18 AND income ≥ 25000"
"""


# ========================================
# 1. AND OPERATOR
# ========================================

age = 25
income = 30000

# Both conditions must be True
if age >= 18 and income >= 25000:
    print("Loan Eligible")
else:
    print("Not Eligible")


# ========================================
# 2. OR OPERATOR
# ========================================

has_degree = False
experience = 3

# Only one condition needs to be True
if has_degree or experience >= 2:
    print("Eligible for job")
else:
    print("Not Eligible")


# ========================================
# 3. NOT OPERATOR
# ========================================

is_logged_in = False

# NOT reverses the value
if not is_logged_in:
    print("Please login")
else:
    print("Welcome")


# ========================================
# 4. COMBINED CONDITIONS
# ========================================

age = 22
income = 40000
credit_score = 750

# Multiple conditions together
if age >= 18 and income >= 25000 and credit_score >= 700:
    print("Loan Approved")
else:
    print("Loan Rejected")


# ========================================
# 5. REAL-LIFE SCENARIO (ADMISSION SYSTEM)
# ========================================

marks = 85
sports_quota = True

# Either high marks OR sports quota
if marks >= 90 or sports_quota:
    print("Admission Granted")
else:
    print("Admission Denied")


# ========================================
# 6. REPLACING NESTED IF (IMPORTANT)
# ========================================

# ❌ Nested version (long)
age = 25
income = 30000

if age >= 18:
    if income >= 25000:
        print("Eligible")

# ✔ Logical version (clean)
if age >= 18 and income >= 25000:
    print("Eligible")


# ========================================
# 7. ORDER OF EVALUATION
# ========================================

"""
and → evaluated first
or  → evaluated later

Use parentheses to control logic
"""

age = 20
income = 20000
vip = True

# Without parentheses → confusing
if age >= 18 and income >= 25000 or vip:
    print("Access Granted")

# Better (clear logic)
if (age >= 18 and income >= 25000) or vip:
    print("Access Granted")


# ========================================
# 8. TRUTHY & FALSY VALUES
# ========================================

"""
False values:
0, "", None, [], {}, False

Everything else → True
"""

if "":
    print("Won't run")
else:
    print("Empty string is False")


# ========================================
# 9. COMMON MISTAKES
# ========================================

# ❌ Wrong operator usage
# if age >= 18 & income >= 25000   (wrong → use 'and')

# ❌ Confusing logic order

# ❌ Missing parentheses in complex conditions


# ========================================
# 10. BEST PRACTICES
# ========================================

"""
✔ Use logical operators to simplify code
✔ Avoid unnecessary nesting
✔ Use parentheses for clarity
✔ Keep conditions readable
"""


# ========================================
# 11. MINI PRACTICE
# ========================================

# Check if the number is between 10 and 50
num = int(input("Enter number: "))

if num >= 10 and num <= 50:
    print("Within range")
else:
    print("Out of range")


# Check login OR OTP
password = input("Enter password: ")
otp = input("Enter OTP: ")

if password == "1234" or otp == "9999":
    print("Access Granted")
else:
    print("Access Denied")
