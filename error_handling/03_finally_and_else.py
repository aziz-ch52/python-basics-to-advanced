"""
=========================================================
03. CONTROLLING EXECUTION FLOW (ELSE & FINALLY)
=========================================================
try: Run the risky code.
Except: Run if the risky code crashes.
else: Run ONLY if the risky code succeeded without errors.
Finally: Run NO MATTER WHAT (essential for closing connections).
=========================================================
"""

def query_database(query_string):
    """Simulates querying a database with full flow control."""
    print("\n[SYSTEM] Establishing database connection...")
    connection_open = True
    
    try:
        print(f"[SYSTEM] Executing query: {query_string}")
        
        # Simulating a syntax error in the query
        if "DROP" in query_string:
            raise ValueError("Destructive commands are blocked by policy.")
            
        # If no error is raised, we process the mock data
        result = {"status": "success", "rows_returned": 150}
        
    except ValueError as e:
        print(f"[ERROR] Query failed: {e}")
        
    else:
        # This ONLY runs if the 'try' block completes perfectly.
        # It keeps your 'try' block lean and focused on just the risky part.
        print("[SUCCESS] Query executed perfectly. Committing changes to logs.")
        print(f"Data payload: {result}")
        
    finally:
        # This ALWAYS runs. If the script succeeds, this runs. If it crashes, this runs.
        # This is where you release memory and close ports.
        if connection_open:
            print("[SYSTEM] Closing database connection to prevent memory leaks.")
            connection_open = False

print("--- 1. SUCCESSFUL PATH ---")
query_database("SELECT * FROM users;")

print("\n--- 2. FAILURE PATH ---")
query_database("DROP TABLE users;")
