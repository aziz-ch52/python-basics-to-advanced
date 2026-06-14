"""
=========================================================
03. NESTED DICTIONARIES (JSON PARSING)
=========================================================
Real-world data is almost never flat. When you hit a REST API,
you will receive nested structures: dictionaries inside of 
lists inside of dictionaries. You must know how to drill down.
=========================================================
"""

# Simulated JSON payload from a weather API
api_response = {
    "status": "success",
    "metadata": {
        "timestamp": "2026-06-14T08:55:00Z",
        "source": "sensor_array_alpha"
    },
    "data": [
        {"location": "New York", "metrics": {"temp": 75, "humidity": 60}},
        {"location": "London", "metrics": {"temp": 62, "humidity": 80}},
        {"location": "Tokyo", "metrics": {"temp": 80, "humidity": 70}}
    ]
}

print("--- DRILLING DOWN INTO NESTED DATA ---")

# 1. Extract the timestamp (Dict -> Dict -> Value)
timestamp = api_response["metadata"]["timestamp"]
print(f"Data pulled at: {timestamp}")

# 2. Extract Tokyo's temperature (Dict -> List -> Dict -> Dict -> Value)
# Step-by-step: Go into 'data', grab the 3rd item (index 2), go into 'metrics', grab 'temp'.
tokyo_temp = api_response["data"][2]["metrics"]["temp"]
print(f"Tokyo Temperature: {tokyo_temp}°F")

# 3. Iterate through the nested list to extract all temperatures
print("\n--- BATCH EXTRACTION ---")
for record in api_response["data"]:
    city = record["location"]
    temp = record["metrics"]["temp"]
    print(f"Extracted -> {city}: {temp}°F")

