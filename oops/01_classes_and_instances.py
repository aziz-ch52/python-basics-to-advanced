"""
=========================================================
01. CLASSES AND INSTANCES (THE BLUEPRINT)
=========================================================
A 'Class' is a blueprint for creating objects.
An 'Instance' is a specific object built from that blueprint.

In Data Engineering, we don't use OOP to model "Dogs" or "Cars". 
We use it to build robust, repeatable wrappers for data pipelines, 
database connections, and API clients.
=========================================================
"""

# ---------------------------------------------------------
# 1. DEFINING THE BLUEPRINT (THE CLASS)
# ---------------------------------------------------------
print("--- 1. DEFINING THE BLUEPRINT ---")

class DataConnector:
    """
    A standardized blueprint for connecting to various data sources.
    """
    
    # The __init__ method is the "constructor". It runs automatically 
    # the exact moment you create a new instance of this class.
    # 'self' refers to the specific object being created in memory.
    def __init__(self, source_name, host_ip, port):
        # These are "Instance Attributes". They belong ONLY to this specific object.
        self.source_name = source_name
        self.host = host_ip
        self.port = port
        self.is_connected = False  # Default state upon creation
        
        print(f"[SYSTEM] Initialized blueprint for {self.source_name} at {self.host}:{self.port}")

    # This is an "Instance Method". It is a function that belongs to the object.
    def connect(self):
        print(f"\n[{self.source_name}] Attempting connection to {self.host}...")
        # Simulating a successful connection
        self.is_connected = True
        print(f"[{self.source_name}] SUCCESS: Connection established on port {self.port}.")

    def extract_data(self, query):
        if not self.is_connected:
            print(f"[{self.source_name}] ERROR: Cannot extract data. Not connected.")
            return None
        
        print(f"[{self.source_name}] Executing query: '{query}'")
        return [f"Row 1 from {self.source_name}", f"Row 2 from {self.source_name}"]


# ---------------------------------------------------------
# 2. CREATING INSTANCES (THE OBJECTS)
# ---------------------------------------------------------
print("\n--- 2. CREATING ISOLATED INSTANCES ---")

# We use the exact same blueprint to create two completely separate objects.
postgres_db = DataConnector("PostgreSQL_Prod", "192.168.1.50", 5432)
mongo_db = DataConnector("MongoDB_Analytics", "10.0.0.12", 27017)

# Proving they are isolated in memory:
print(f"\nPostgres IP: {postgres_db.host}")
print(f"Mongo IP: {mongo_db.host}")


# ---------------------------------------------------------
# 3. EXECUTING INSTANCE METHODS
# ---------------------------------------------------------
print("\n--- 3. EXECUTING PIPELINE LOGIC ---")

# We connect Postgres, but intentionally leave Mongo disconnected to prove 
# their internal states (self.is_connected) do not affect each other.
postgres_db.connect()

print("\n--- Attempting Data Extraction ---")
# This succeeds because self.is_connected is True for postgres_db
pg_data = postgres_db.extract_data("SELECT * FROM users;")

# This fails because self.is_connected is False for mongo_db
mongo_data = mongo_db.extract_data("db.sales.find({})")

