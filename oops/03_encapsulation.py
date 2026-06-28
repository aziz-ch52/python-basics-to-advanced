"""
=========================================================
04. ENCAPSULATION (DATA HIDING)
=========================================================
You don't want junior developers accidentally overwriting 
critical variables (like database passwords or internal states).

By prefixing variables with double underscores (__), you make 
them "private". They cannot be accessed directly from outside 
the class. You must provide safe "getter" methods instead.
=========================================================
"""

class SecureDatabaseConnector:
    def __init__(self, host, username, password):
        self.host = host          # Public: Anyone can read/write this
        self.username = username  # Public
        self.__password = password # PRIVATE: Hidden from the outside
        self.__is_authenticated = False # PRIVATE: Hidden state

    def authenticate(self, input_password):
        """A controlled method to verify credentials without exposing the password."""
        print(f"Attempting authentication for {self.username}...")
        if input_password == self.__password:
            self.__is_authenticated = True
            print("SUCCESS: Authenticated.")
        else:
            print("ERROR: Invalid credentials.")

    def run_query(self, query):
        """A controlled method that checks the private state before executing."""
        if not self.__is_authenticated:
            print("ACCESS DENIED: Please authenticate first.")
            return
        print(f"Executing: {query}")


print("--- 1. SECURING THE PIPELINE ---")
db = SecureDatabaseConnector("10.0.0.99", "admin", "super_secret_123")

print(f"Public Host accessible: {db.host}")

print("\n--- 2. THE ENCAPSULATION SHIELD ---")
# ❌ The below line would crash the script with an AttributeError.
# print(db.__password)  

# ❌ The below line would also crash. You cannot check the state directly.
# print(db.__is_authenticated)

print("\n--- 3. CONTROLLED ACCESS ---")
# We must use the public methods to interact with the private data
db.run_query("DROP TABLE users;") # Fails, not authenticated
db.authenticate("wrong_password")
db.authenticate("super_secret_123")
db.run_query("SELECT * FROM secure_vault;") 

# Succeeds!
