"""
=========================================================
01. READING TEXT FILES (CONTEXT MANAGERS)
=========================================================
The old way of opening files required explicitly calling file.close().
If an error happened before close(), memory leaked.

The professional standard is using a Context Manager ('with' block).
It automatically guarantees that the file resource is closed safely
the millisecond the code leaves the block, even if the script crashes.
=========================================================
"""

# First, let's programmatically create a sample log file to read
with open("sample_logs.txt", "w", encoding="utf-8") as f:
    f.write("2026-06-22 10:00:00 - INFO - Pipeline Started\n")
    f.write("2026-06-22 10:01:15 - WARNING - High Latency Detected\n")
    f.write("2026-06-22 10:05:00 - INFO - Ingestion Complete\n")

# ---------------------------------------------------------
# 1. READING THE ENTIRE FILE AT ONCE (.read)
# ---------------------------------------------------------
print("--- 1. READING WHOLE FILE ---")

with open("sample_logs.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)


# ---------------------------------------------------------
# 2. READING LINE BY LINE (MEMORY EFFICIENT)
# ---------------------------------------------------------
print("--- 2. ITERATING LINE BY LINE (BEST PRACTICE) ---")
# If a log file is 10GB, .read() will crash your RAM. 
# Iterating directly over the file object processes one line at a time.

with open("sample_logs.txt", "r", encoding="utf-8") as file:
    for line in file:
        # strip() removes the newline character (\n) from the end of each line
        clean_line = line.strip()
        
        # Simple string matching to filter warnings
        if "WARNING" in clean_line:
            print(f"🚨 ANOMALY FOUND: {clean_line}")
          
