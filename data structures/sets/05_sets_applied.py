"""
=========================================================
05. APPLIED SETS (ETL COMPARISON PIPELINE)
=========================================================
This script simulates comparing yesterday's server logs 
With today's technology to identify anomalies, new IP addresses, 
and retained connections.
=========================================================
"""

# 1. Raw Data Extraction (Simulated)
yesterday_logs = ["192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.2"]
today_logs = ["10.0.0.5", "10.0.0.5", "10.0.0.99", "192.168.1.1"]

# 2. Transformation (List to Set Deduplication)
yesterday_unique = set(yesterday_logs)
today_unique = set(today_logs)

# 3. Analytics (Set Math Operations)
# Find IPs that connected both days
retained_ips = yesterday_unique & today_unique

# Find brand new IPs that appeared today
new_ips = today_unique - yesterday_unique

# Find IPs that dropped off today
dropped_ips = yesterday_unique - today_unique

# 4. Output Reporting
print("--- DAILY SERVER CONNECTION REPORT ---")
print(f"Total Unique IPs Yesterday: {len(yesterday_unique)}")
print(f"Total Unique IPs Today: {len(today_unique)}")
print("-" * 30)
print(f"Retained Connections: {retained_ips}")
print(f"New Connections Today: {new_ips}")
print(f"Dropped Connections: {dropped_ips}")
