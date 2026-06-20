"""
=========================================================
03. FLEXIBLE INPUTS (*args and **kwargs)
=========================================================
In analytics, you often don't know how many columns or 
parameters a dataset will have. *args and **kwargs allow 
your functions to accept an infinite number of inputs.
=========================================================
"""

# ---------------------------------------------------------
# 1. *args (VARIABLE POSITIONAL ARGUMENTS)
# ---------------------------------------------------------
print("--- 1. *args (THE TUPLE PACKER) ---")

# The asterisk (*) takes any number of positional arguments 
# and packs them into a TUPLE.
def sum_all_metrics(pipeline_name, *args):
    print(f"Running aggregation for: {pipeline_name}")
    print(f"Raw args tuple received: {args}")
    return sum(args)

total_revenue = sum_all_metrics("Q1_Revenue", 100, 200, 300, 400, 500)
print(f"Total: {total_revenue}")


# ---------------------------------------------------------
# 2. **kwargs (VARIABLE KEYWORD ARGUMENTS)
# ---------------------------------------------------------
print("\n--- 2. **kwargs (THE DICTIONARY PACKER) ---")

# The double asterisk (**) takes any number of keyword arguments 
# and packs them into a DICTIONARY. This is heavily used for 
# passing dynamic configuration settings.
def configure_database(db_name, **kwargs):
    print(f"Configuring Database: {db_name}")
    print(f"Kwargs dict received: {kwargs}")
    
    # Safely extracting dynamic settings using dictionary methods
    host = kwargs.get("host", "localhost")
    port = kwargs.get("port", 5432)
    
    print(f"Routing to {host}:{port}")

configure_database("Analytics_DB", host="192.168.1.5", port=8080, max_connections=100)

