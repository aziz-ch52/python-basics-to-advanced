"""
=========================================================
05. MAGIC METHODS (DUNDER METHODS)
=========================================================
Magic methods are surrounded by double underscores (e.g., __init__).
They allow you to overload standard Python behavior.

For pipelines, overloading __str__ and __repr__ is critical. 
If someone prints your object, you want it to output clean, 
JSON-like metadata, not a useless memory address.
=========================================================
"""

class DataPipeline:
    def __init__(self, pipeline_name, row_count, target_table):
        self.name = pipeline_name
        self.rows = row_count
        self.target = target_table

    # Overloading the built-in print() function behavior
    def __str__(self):
        """Defines what is shown when the object is printed as a string."""
        return f"Pipeline[{self.name}] -> {self.rows} rows mapped to '{self.target}'"

    # Overloading the built-in len() function behavior
    def __len__(self):
        """Allows us to call len() on the object itself to get row counts."""
        return self.rows


print("--- 1. DEFAULT VS OVERLOADED PRINTING ---")

# If we didn't have __str__, printing this would output:
# <__main__.DataPipeline object at 0x7f8b9c...> (Useless garbage)

etl_job = DataPipeline("Nightly_Sync", 50400, "production.users")

# Because we defined __str__, this is highly readable for logging.
print(etl_job)


print("\n--- 2. OVERLOADING BUILT-IN FUNCTIONS ---")

# Because we defined __len__, we can treat our object like a list!
if len(etl_job) > 50000:
    print(f"WARNING: Massive payload detected ({len(etl_job)} rows). Allocating extra memory.")
