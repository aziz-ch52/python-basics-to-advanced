"""
=========================================================
03. INHERITANCE (DRY PRINCIPLE)
=========================================================
Inheritance allows a "Child" class to inherit all the methods 
and attributes of a "Parent" class. 

If you are building extractors for CSVs, JSON, and SQL, they 
all need basic logging and error handling. Don't write that 3 times.
Write it once in a BaseExtractor, and let the specific extractors 
inherit it.
=========================================================
"""

# ---------------------------------------------------------
# 1. THE PARENT CLASS (BASE BLUEPRINT)
# ---------------------------------------------------------
class BaseExtractor:
    def __init__(self, source_name):
        self.source_name = source_name
        self.status = "Idle"

    def log_activity(self, message):
        """A standardized logger that all child classes will inherit."""
        print(f"[LOG - {self.source_name}] {message}")


# ---------------------------------------------------------
# 2. THE CHILD CLASSES
# ---------------------------------------------------------
# Passing the parent class in parentheses tells Python to inherit from it
class CSVExtractor(BaseExtractor):
    
    def __init__(self, source_name, file_path):
        # super().__init__() calls the Parent's __init__ so we don't have 
        # to rewrite the 'source_name' and 'status' setup logic.
        super().__init__(source_name)
        self.file_path = file_path

    def extract(self):
        # Using the inherited logger!
        self.log_activity(f"Opening CSV at {self.file_path}...")
        self.status = "Extracting"
        return "CSV Data Payload"


class APIExtractor(BaseExtractor):
    
    def __init__(self, source_name, endpoint_url):
        super().__init__(source_name)
        self.endpoint = endpoint_url

    def extract(self):
        self.log_activity(f"Sending GET request to {self.endpoint}...")
        self.status = "Extracting"
        return "JSON API Payload"


# ---------------------------------------------------------
# 3. EXECUTION
# ---------------------------------------------------------
print("--- RUNNING INHERITED EXTRACTORS ---")

csv_job = CSVExtractor("Daily_Sales", "/data/sales.csv")
api_job = APIExtractor("Weather_Data", "https://api.weather.com/v1")

# Both objects can use .log_activity() even though we didn't define 
# it inside CSVExtractor or APIExtractor. They inherited it.
csv_job.extract()
api_job.extract()
