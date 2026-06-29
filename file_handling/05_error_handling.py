"""
=========================================================
05. SECURING INGESTION PIPELINES (TRY / EXCEPT)
=========================================================
Data pipelines live in unpredictable environments. Files will be 
missing, columns will be corrupt, and files will drop out.

If you don't wrap file operations inside a try-except structure,
One missing raw file will halt your entire data operations stack.
=========================================================
"""

# ---------------------------------------------------------
# 1. GRACEFUL FALLBACKS FOR MISSING FILES
# ---------------------------------------------------------
print("--- 1. CATCHING FILENOTFOUNDERRORS ---")

target_file = "missing_dataset.csv"

try:
    with open(target_file, "r", encoding="utf-8") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    # Instead of halting the script execution, we issue a clear alert and fall back safely
    print(f"⚠️ PIPELINE ALERT: '{target_file}' could not be located on disk. Proceeding with default empty metrics.")
    data = []

except Exception as e:
    # A generic catch-all for unknown edge cases (e.g., access rights issues)
    print(f"❌ UNEXPECTED CRITICAL ERROR: {e}")


# ---------------------------------------------------------
# 2. THE COMPREHENSIVE TRY/EXCEPT/FINALLY TEMPLATE
# ---------------------------------------------------------
print("\n--- 2. THE COMPLETE EXECUTION CYCLE ---")

try:
    print("Opening metric database log tracking...")
    with open("config.json", "r", encoding="utf-8") as file:
        conf = json.load(file)
    print("Configuration extracted successfully.")

except json.JSONDecodeError:
    print("❌ ERROR: File exists but content contains invalid, corrupted JSON formatting.")

finally:
    # Code inside this block executes NO MATTER WHAT, even if a crash occurs above.
    # Essential for closing DB connections, network sockets, or cleanup scripts.
    print("🔒 Pipeline Operations cleanup block cleared.")
