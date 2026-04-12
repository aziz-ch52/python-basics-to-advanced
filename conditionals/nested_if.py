"""
========================================
NESTED IF - COMPLETE GUIDE
========================================

WHAT IS NESTED IF?

A nested if means:
👉 An 'if' statement inside another 'if' statement

Used when:
✔ Second condition depends on the first condition
✔ You want hierarchical decision-making


WHEN TO USE NESTED IF?

Use nested if when:
✔ Conditions are dependent
✔ One condition must be checked BEFORE another

REAL-LIFE THINKING:
"If age ≥ 18:
    THEN check ID
ELSE:
    Not allowed"
"""


# ========================================
# 1. BASIC EXAMPLE
# ========================================

age = 20
has_id = True

# Flow:
# Step 1 → Check age
# Step 2 → If True → go inside
# Step 3 → Check ID

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Not Allowed")


# ========================================
# 2. LOGIN + ROLE CHECK
# ========================================

username = "admin"
password = "1234"
role = "admin"

# Step-by-step logic:
if username == "admin" and password == "1234":
    print("Login Successful")

    # Nested check
    if role == "admin":
        print("Full Access Granted")
    else:
        print("Limited Access")
else:
    print("Invalid Credentials")


# ========================================
# 3. NUMBER ANALYSIS
# ========================================

num = 10

# Check positive first, then even/odd
if num > 0:
    print("Positive Number")

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Not Positive")


# ========================================
# 4. REAL-LIFE SCENARIO (LOAN APPROVAL)
# ========================================

age = 25
income = 40000
credit_score = 750

# Flow:
# Step 1 → Age check
# Step 2 → Income check
# Step 3 → Credit score check

if age >= 18:
    if income >= 25000:
        if credit_score >= 700:
            print("Loan Approved")
        else:
            print("Low Credit Score")
    else:
        print("Insufficient Income")
else:
    print("Underage")


# ========================================
# 5. COMMON MISTAKES
# ========================================

# ❌ Too much nesting (hard to read)
# ❌ Wrong indentation
# ❌ Using nested if when not needed


# ========================================
# 6. BETTER ALTERNATIVE (IMPORTANT)
# ========================================

"""
Sometimes nested if can be replaced with logical operators
→ cleaner and shorter
"""

age = 25
income = 40000

# Instead of nested if
if age >= 18 and income >= 25000:
    print("Eligible")


# ========================================
# 7. BEST PRACTICES
# ========================================

"""
✔ Use nested if ONLY when necessary
✔ Avoid deep nesting (max 2–3 levels)
✔ Prefer logical operators when possible
✔ Keep readability high
"""


# ========================================
# 8. MINI PRACTICE
# ========================================

# ATM withdrawal system

balance = 5000
pin = 1234

entered_pin = int(input("Enter PIN: "))
amount = int(input("Enter amount: "))

if entered_pin == pin:
    if amount <= balance:
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")
