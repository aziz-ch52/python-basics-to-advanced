"""
========================================
IF-ELIF-ELSE - COMPLETE GUIDE
========================================

WHAT IS IF-ELIF-ELSE?

Used when you have MULTIPLE conditions to check.

Flow:
✔ Python checks conditions from TOP to BOTTOM
✔ As soon as one condition is True → it executes and STOPS
✔ Remaining conditions are NOT checked


WHEN TO USE?

Use when:
✔ You have more than 2 possible outcomes
✔ Conditions are mutually exclusive
✔ Only ONE block should run

REAL-LIFE THINKING:
"If marks ≥ 90 → Grade A
elif ≥ 75 → Grade B
elif ≥ 50 → Grade C
else → Fail"
"""


# ========================================
# 1. BASIC EXAMPLE
# ========================================

marks = 82

# Flow:
# Check 90 → False
# Check 75 → True → Execute → STOP
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# ========================================
# 2. NUMBER CATEGORY
# ========================================

num = -5

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# ========================================
# 3. REAL-LIFE SCENARIO (DISCOUNT SYSTEM)
# ========================================

amount = 2500

# Different discounts based on amount
if amount >= 5000:
    print("20% Discount")
elif amount >= 2000:
    print("10% Discount")
elif amount >= 1000:
    print("5% Discount")
else:
    print("No Discount")


# ========================================
# 4. GRADE SYSTEM (INPUT BASED)
# ========================================

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Excellent (A)")
elif marks >= 75:
    print("Good (B)")
elif marks >= 50:
    print("Average (C)")
else:
    print("Fail")


# ========================================
# 5. IMPORTANT LOGIC RULE (VERY IMPORTANT)
# ========================================

"""
Order matters!

The wrong order can break logic.
"""

marks = 85

# ❌ WRONG ORDER
if marks >= 50:
    print("Pass")
elif marks >= 90:
    print("Topper")   # This will NEVER run


# ✔ CORRECT ORDER (Specific → General)
if marks >= 90:
    print("Topper")
elif marks >= 50:
    print("Pass")


# ========================================
# 6. COMMON MISTAKES
# ========================================

# ❌ Using multiple 'if' instead of elif
marks = 85

if marks >= 90:
    print("A")
if marks >= 75:
    print("B")   # This ALSO runs (wrong behavior)

# ✔ Use elif instead
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")


# ❌ Missing colon :
# ❌ Wrong indentation


# ========================================
# 7. BEST PRACTICES
# ========================================

"""
✔ Always write conditions in the correct order
✔ Use elif instead of multiple ifs
✔ Keep logic simple and readable
✔ Think flow before writing code
"""


# ========================================
# 8. MINI PRACTICE
# ========================================

# Menu-based program
choice = int(input("Enter choice (1-3): "))

if choice == 1:
    print("You selected Option 1")
elif choice == 2:
    print("You selected Option 2")
elif choice == 3:
    print("You selected Option 3")
else:
    print("Invalid choice")

