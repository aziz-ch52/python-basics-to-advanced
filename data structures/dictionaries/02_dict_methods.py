"""
=========================================================
02. DICTIONARY METHODS (SAFE EXTRACTION)
=========================================================
Pipelines break because of missing data. Mastering dictionary
methods allows you to extract data safely, provide default 
values when data is missing, and iterate through massive payloads.
=========================================================
"""

server_config = {
    "host": "192.168.1.1",
    "port": 8080,
    "environment": "production"
}

# ---------------------------------------------------------
# 1. SAFE DATA EXTRACTION (CRITICAL)
# ---------------------------------------------------------
print("--- 1. THE .get() METHOD ---")

# get(key, default) returns the value if the key exists.
# If the key is missing, it returns the default value instead of crashing.
port = server_config.get("port", 80)
timeout = server_config.get("timeout_seconds", 30) # Key doesn't exist, returns 30 safely.

print(f"Port: {port} | Timeout: {timeout}")


# ---------------------------------------------------------
# 2. ITERATION ARRAYS
# ---------------------------------------------------------
print("\n--- 2. KEYS, VALUES, AND ITEMS ---")

# .keys(): Returns just the keys
print(f"Keys: {list(server_config.keys())}")

# .values(): Returns just the values
print(f"Values: {list(server_config.values())}")

# .items(): Returns tuples of (key, value). 
# This is mandatory for iterating through a dictionary in a 'for' loop.
for key, value in server_config.items():
    print(f"Config -> {key}: {value}")


# ---------------------------------------------------------
# 3. REMOVING & MERGING DATA
# ---------------------------------------------------------
print("\n--- 3. POP & UPDATE ---")

# pop(key, default): Removes the key-value pair and returns the value.
environment = server_config.pop("environment", "unknown")
print(f"Popped Env: {environment} | Remaining Dict: {server_config}")

# update(dict): Merges another dictionary into the current one.
new_settings = {"ssl_enabled": True, "port": 443} # Notice 'port' will be overwritten
server_config.update(new_settings)

print(f"Merged Config: {server_config}")

