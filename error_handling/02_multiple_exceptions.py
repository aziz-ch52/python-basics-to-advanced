"""
=========================================================
02. TARGETING SPECIFIC EXCEPTIONS
=========================================================
Never use a bare 'except:' block unless necessary.
It hides the actual root cause of the bug. 

You must write different fallback logic for a missing file 
Versus a corrupted data type.
=========================================================
"""

def extract_metric_from_file(filename, metric_index):
    """Simulates opening a file and extracting a specific index."""
    try:
        print(f"[SYSTEM] Attempting to read {filename}...")
        
        # Risk 1: The file might not exist (FileNotFoundError)
        with open(filename, "r") as file:
            data = file.readlines()
            
        # Risk 2: The index might be out of range (IndexError)
        # Risk 3: The data might not be castable to an integer (ValueError)
        target_value = int(data[metric_index].strip())
        print(f"[SUCCESS] Metric extracted: {target_value}")

    # Catching specific errors allows for specific, helpful logging
    except FileNotFoundError:
        print(f"[CRITICAL ERROR] The dataset '{filename}' is missing from the server.")
        
    except IndexError:
        print(f"[ERROR] The requested row index ({metric_index}) does not exist in the dataset.")
        
    except ValueError:
        print(f"[ERROR] The data at index {metric_index} is corrupted and cannot be cast to an integer.")
        
    except Exception as e:
        # A generic catch-all ONLY for unexpected edge cases
        print(f"[FATAL] An unknown error occurred: {e}")

print("--- TESTING SPECIFIC FAILURES ---")
# This will trigger FileNotFoundError because we didn't create the file
extract_metric_from_file("ghost_data.csv", 2)
