"""
=========================================================
02. INSTANCE VS. CLASS VARIABLES
=========================================================
Instance Variables (using 'self'): Belong to ONE specific object.
Class Variables: Belong to the blueprint itself and are SHARED 
                 across all objects created from that blueprint.

Use Case: You want each database connection to track its own queries (Instance),
But you want the system to track the TOTAL active connections across the entire 
server to prevent overloading (Class).
=========================================================
"""

class DatabaseConnection:
    
    # 1. CLASS VARIABLE: Shared across every instance.
    # Defined outside of __init__, without 'self'.
    total_active_connections = 0
    
    def __init__(self, db_name):
        # 2. INSTANCE VARIABLES: Unique to this specific connection.
        self.db_name = db_name
        self.queries_run = 0
        
        # When a new connection is created, update the GLOBAL class variable
        DatabaseConnection.total_active_connections += 1
        print(f"[SYSTEM] Connected to {self.db_name}. Total server connections: {DatabaseConnection.total_active_connections}")

    def execute_query(self, query):
        # Updates the INSTANCE variable (only affects this specific DB)
        self.queries_run += 1
        print(f"[{self.db_name}] Executing: {query}")

    def close_connection(self):
        # Decrement the GLOBAL class variable when a connection closes
        DatabaseConnection.total_active_connections -= 1
        print(f"[SYSTEM] Closed {self.db_name}. Total server connections: {DatabaseConnection.total_active_connections}")


print("--- 1. SPAWNING INSTANCES ---")
# Watch the class variable increment across all instances
db1 = DatabaseConnection("Sales_DB")
db2 = DatabaseConnection("HR_DB")
db3 = DatabaseConnection("Analytics_DB")

print("\n--- 2. UPDATING INSTANCE VARIABLES ---")
db1.execute_query("SELECT * FROM q1_sales;")
db1.execute_query("SELECT * FROM q2_sales;")
db2.execute_query("SELECT * FROM employees;")

# Prove they are isolated
print(f"Sales DB Queries Run: {db1.queries_run}")
print(f"HR DB Queries Run: {db2.queries_run}")

print("\n--- 3. VERIFYING CLASS VARIABLE SHARED STATE ---")
db1.close_connection()
# Accessing the class variable directly from the class, not the instance
print(f"Final Active Connections: {DatabaseConnection.total_active_connections}")
