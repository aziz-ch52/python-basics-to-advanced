"""
=========================================================
02. SET MUTATIONS (UPDATING PIPELINES)
=========================================================
How to safely add and remove data from a Set without 
crashing your script when messy data throws a curveball.
=========================================================
"""

# ---------------------------------------------------------
# 1. ADDING DATA
# ---------------------------------------------------------
print("--- 1. ADDING DATA ---")

active_sessions = {"User_A", "User_B"}

# add(x): Adds a single item. If it already exists, nothing happens.
active_sessions.add("User_C")
active_sessions.add("User_A") # Duplicate ignored silently
print(f"After add: {active_sessions}")

# update(iterable): Merges multiple items (from a list, tuple, or another set)
new_logins = ["User_D", "User_E"]
active_sessions.update(new_logins)
print(f"After update: {active_sessions}")


# ---------------------------------------------------------
# 2. REMOVING DATA (CRITICAL DIFFERENCES)
# ---------------------------------------------------------
print("\n--- 2. REMOVING DATA ---")

flagged_ips = {"192.168.1.1", "10.0.0.5"}

# remove(x): Drops an item, but CRASHES (KeyError) if the item isn't there.
flagged_ips.remove("10.0.0.5")
# flagged_ips.remove("0.0.0.0") # ❌ Would crash the script

# discard(x): Drops an item safely. If it isn't there, it does nothing. No crash.
flagged_ips.discard("192.168.1.1")
flagged_ips.discard("0.0.0.0") # ✅ Safe. Fails silently.

print(f"Remaining flagged IPs: {flagged_ips}")


# pop(): Removes and returns a completely RANDOM element (because sets are unordered).
# Rarely used in analytics, but good to know.
random_pool = {"Task1", "Task2", "Task3"}
completed = random_pool.pop()
print(f"Randomly popped: {completed}")
