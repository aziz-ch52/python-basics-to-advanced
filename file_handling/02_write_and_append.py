"""
=========================================================
02. WRITE VS. APPEND MODES
=========================================================
Understanding file access modes prevents devastating data loss.

'w' (Write): Overwrites the file completely. If the file exists, 
             its entire history is wiped out instantly.
'a' (Append): Retains existing data and tacks new strings onto 
              the very bottom of the file.
=========================================================
"""

# ---------------------------------------------------------
# 1. THE WRITE OVERWRITE ('w')
# ---------------------------------------------------------
print("--- 1. EXECUTING WRITE OVERWRITE ---")

# First write
with open("report.txt", "w", encoding="utf-8") as file:
    file.write("Initial System Report - Run 1\n")

# Overwriting the exact same file
with open("report.txt", "w", encoding="utf-8") as file:
    file.write("Completely New System Report - Run 2\n")

# Read it back to verify: Run 1 is completely gone.
with open("report.txt", "r", encoding="utf-8") as file:
    print(f"Current file state:\n{file.read()}")


# ---------------------------------------------------------
# 2. THE APPEND MODE ('a')
# ---------------------------------------------------------
print("\n--- 2. EXECUTING APPENDS ---")

# Using 'a' mode ensures existing content remains safe
with open("report.txt", "a", encoding="utf-8") as file:
    file.write("Appending Log Record: Component Alpha Operational\n")
    file.write("Appending Log Record: Component Beta Operational\n")

# Verify both are preserved together
with open("report.txt", "r", encoding="utf-8") as file:
    print(f"Appended file state:\n{file.read()}")
  
