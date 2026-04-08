"""
========================================
BASIC IF STATEMENT - COMPLETE GUIDE
========================================

WHAT IS IF?

The 'if' statement is used to execute code ONLY when a condition is True.

There is NO 'else' here.
If the condition is False → nothing happens.


WHEN TO USE BASIC IF?

Use 'if' when:
✔ You only care about the True case
✔ No action is needed for the false case
✔ You want to check a condition and act only if it's satisfied

REAL-LIFE THINKING:
"If it rains → take an umbrella."
(No need for else logic)
"""


# ========================================
# 1. BASIC EXAMPLE
# ========================================

age = 20

# Flow:
# Step 1 → Check condition (age >= 18)
# Step 2 → If True → execute block
# Step 3 → If False → skip block

if age >= 18:
    print("You are eligible to vote")


# ========================================
# 2. TEMPERATURE CHECK
# ========================================

temperature = 35

# Only act if the condition is met
if temperature > 30:
    print("It's a hot day")


# ========================================
# 3. LOGIN CHECK (PARTIAL)
# ========================================

is_logged_in = True

# Only show message if user is logged in
if is_logged_in:
    print("Welcome back!")


# ========================================
# 4. LIST CHECK
# ========================================

numbers = [1, 2, 3]

# Check if the list is not empty
if numbers:
    print("List is not empty")


# ========================================
# 5. STRING CHECK
# ========================================

name = "Aziz"

# Check if string has value
if name:
    print("Name is provided")


# ========================================
# 6. REAL-LIFE SCENARIO
# ========================================

marks = 85

# Only reward if high score
if marks >= 80:
    print("You got distinction!")


# ========================================
# 7. COMMON MISTAKES
# ========================================

# ❌ Missing colon :
# if age >= 18

# ❌ Wrong indentation
# if age >= 18:
# print("Error")

# ❌ Expecting else behavior (it doesn't exist here)


# ========================================
# 8. BEST PRACTICES
# ========================================

"""
✔ Use 'if' when only the true case matters
✔ Keep the condition simple
✔ Avoid unnecessary checks
✔ Use meaningful variable names
"""


# ========================================
# 9. MINI PRACTICE
# ========================================

# Take a number and print only if it's positive

num = int(input("Enter number: "))

if num > 0:
    print("Positive number")

