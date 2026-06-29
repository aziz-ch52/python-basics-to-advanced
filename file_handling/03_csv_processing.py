"""
=========================================================
03. TABULAR DATA INGESTION (THE CSV MODULE)
=========================================================
Before jumping to advanced frameworks like Pandas, a data 
engineer must know how to parse native comma-separated datasets 
manually. 

Using Python's built-in 'csv' module preserves headers 
and properly maps values.
=========================================================
"""
import csv

# Programmatically generate raw CSV test data
raw_sales_data = [
    ["transaction_id", "product", "revenue"],
    ["TXN001", "Laptop", "1200.50"],
    ["TXN002", "Monitor", "300.00"],
    ["TXN003", "Keyboard", "85.25"]
]

with open("raw_sales.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(raw_sales_data)

# ---------------------------------------------------------
# 1. READING CSV VIA DICTIONARIES (RECOMMENDED)
# ---------------------------------------------------------
print("--- 1. READING CSV WITH DictReader ---")
# csv.DictReader maps rows straight to Python dictionaries using headers as keys.

with open("raw_sales.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    total_pipeline_revenue = 0.0
    
    for row in reader:
        # Values read from text files are ALWAYS strings. They must be explicitly cast.
        rev = float(row["revenue"])
        total_pipeline_revenue += rev
        print(f"Processed item: {row['product']} | Sales: ${rev}")

print(f"\nTotal Pipeline Revenue Aggregated: ${total_pipeline_revenue:.2f}")


# ---------------------------------------------------------
# 2. WRITING CSV VIA DICTIONARIES
# ---------------------------------------------------------
print("\n--- 2. WRITING CSV WITH DictWriter ---")

cleaned_records = [
    {"user_id": 101, "tier": "Gold", "status": "Active"},
    {"user_id": 102, "tier": "Silver", "status": "Inactive"}
]

fieldnames = ["user_id", "tier", "status"]

with open("processed_users.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Must write the header row first
    writer.writeheader()
    # Write structural dictionaries safely
    writer.writerows(cleaned_records)

print("processed_users.csv written out successfully.")

