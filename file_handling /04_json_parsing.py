"""
=========================================================
04. SEMI-STRUCTURED DATA PARSING (JSON MODULE)
=========================================================
Web API payloads, server configuration parameters, and NoSQL 
Extractions are built almost entirely out of JSON objects.

Python provides the 'json' module to deserialize JSON strings 
into native Python dictionaries/lists, and vice-versa.
=========================================================
"""
import json

# ---------------------------------------------------------
# 1. PARSING JSON STRINGS (json.loads)
# ---------------------------------------------------------
print("--- 1. DESERIALIZING STRINGS (json.loads) ---")

# API responses arrive as massive continuous text blocks
api_response_string = '{"user": "aziz_t", "role": "data_engineer", "permissions": ["read", "write"]}'

# Transform the raw text payload into a clean, functional Python dictionary
data_dict = json.loads(api_response_string)

print(f"Python Type: {type(data_dict)}")
print(f"Extracted User Role: {data_dict['role']}")


# ---------------------------------------------------------
# 2. PARSING COMPACT JSON FILES (json.load)
# ---------------------------------------------------------
print("\n--- 2. READING STRUCTURAL JSON FILES ---")

# Create mock configuration file
mock_config = {"env": "prod", "db_port": 5432, "debug_mode": False}
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(mock_config, f)

# Read it directly from the local file system
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

print(f"Loaded config parameters: {config}")
print(f"Target Port Connection: {config['db_port']}")


# ---------------------------------------------------------
# 3. PRETTY-PRINTING OUTPUTS (json.dumps)
# ---------------------------------------------------------
print("\n--- 3. SERIALIZING AND PRETTY-PRINTING ---")

complex_data = {
    "status": 200,
    "payload": {
        "metrics": [45, 90, 12],
        "validated": True
    }
}

# 'indent' formats the string with human-readable tabs and clean spacing
formatted_json_string = json.dumps(complex_data, indent=4)
print(formatted_json_string)
