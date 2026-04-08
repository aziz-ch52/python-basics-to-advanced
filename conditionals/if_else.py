"""
========================================
IF-ELSE STATEMENT:
========================================

WHAT IS IF-ELSE?

If-else is used when you have TWO possible outcomes:
1. Condition is True  → run 'if' block
2. Condition is False → run 'else' block


WHEN TO USE IF-ELSE?

Use if-else when:
✔ You need a decision between two paths
✔ Only one block should execute
✔ There is a clear True/False outcome

REAL-LIFE THINKING:
"IF it rains → take an umbrella
ELSE → go normally."
"""


# ========================================
# 1. BASIC EXAMPLE
# ========================================

num = 10

# Flow:
# Step 1 → Check condition (num % 2 == 0)
# Step 2 → If True → run 'if' block
# Step 3 → Else → run 'else' block

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# ========================================
# 2. AGE CHECK (REAL-LIFE SCENARIO)
# ========================================

age = 16

# Decision:
# IF age >= 18 → Adult
# ELSE → Minor

if age >= 18:
    print("Adult")
else:
    print("Minor")


# ========================================
# 3. LOGIN VALIDATION
# ========================================

username = "admin"
password = "1234"

# Check credentials
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")


# ========================================
# 4. NUMBER COMPARISON
# ========================================

a = 5
b = 10

# Compare two numbers
if a > b:
    print("a is greater")
else:
    print("b is greater or equal")


# ========================================
# 5. PRACTICAL SCENARIO (DISCOUNT)
# ========================================

amount = 1200

# If amount > 1000 → give discount
if amount > 1000:
    print("Discount Applied")
else:
    print("No Discount")


# ========================================
# 6. COMMON MISTAKES
# ========================================

# ❌ Using = instead of ==
# if num = 10:

# ❌ Missing colon :
# if num > 5

# ❌ Wrong indentation


# ========================================
# 7. BEST PRACTICES
# ========================================

"""
✔ Keep conditions simple and readable
✔ Use meaningful variable names
✔ Avoid deeply nested conditions here
✔ Always handle both outcomes properly
"""


# ========================================
# 8. MINI PRACTICE
# ========================================

# Take number from user and check positive/negative

num = int(input("Enter a number: "))

if num >= 0:
    print("Positive")
else:
    print("Negative")
