"""
=========================================================
05. CHAINING GENERATORS (STREAMING ETL)
=========================================================
This is a professional Streaming ETL pipeline.
By chaining generators together, you can read, clean, and 
filter data one row at a time. 

If this file had 10 billion rows, this script would run 
perfectly without ever maxing out your RAM.
=========================================================
"""

# Simulated raw data file (pretend this is 100GB on disk)
raw_logs = [
    "2026-09-08,ERROR,Timeout",
    "2026-09-08,INFO,Success",
    "2026-09-08,ERROR,Connection Dropped",
    "bad_data_row_ignore_me",
    "2026-09-08,WARNING,High Latency"
]

# STEP 1: Extract (Read one line at a time)
def extract_logs(log_data):
    for line in log_data:
        yield line

# STEP 2: Transform (Clean the strings)
def split_columns(log_stream):
    for line in log_stream:
        yield line.split(",")

# STEP 3: Filter (Keep only errors)
def filter_errors(parsed_stream):
    for columns in parsed_stream:
        if len(columns) == 3 and columns[1] == "ERROR":
            yield columns

print("--- STREAMING PIPELINE EXECUTION ---")

# Chain them together (Nothing has actually executed yet!)
stream_1 = extract_logs(raw_logs)
stream_2 = split_columns(stream_1)
pipeline = filter_errors(stream_2)

# The data is pulled through the pipeline only when we iterate
for error_record in pipeline:
    print(f"Alert Logged: {error_record[2]}")
