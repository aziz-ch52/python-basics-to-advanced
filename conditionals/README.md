# 🚦 Conditionals: Logic & Decision Flow

This directory focuses on the foundational decision-making structures in Python. In data engineering, conditional logic is the primary mechanism for **data validation** and **automated error handling**—ensuring your pipeline only processes valid data.

## 📂 File Directory

* **1️⃣ `basic_if.py`**: Fundamental single-condition logic.
* **2️⃣ `if_else.py`**: Binary decision-making (True vs. False paths).
* **3️⃣ `if_elif_else.py`**: Handling multiple mutually exclusive data states.
* **4️⃣ `nested_if.py`**: Managing hierarchical logic (decisions based on prior decisions).
* **5️⃣ `logical_conditions.py`**: Using Boolean operators (`and`, `or`, `not`) to refine criteria.
* **6️⃣ `ternary_operator.py`**: Compact, high-efficiency, single-line expressions.
* **7️⃣ `real_world_examples.py`**: Practical application—cleaning outliers and invalid entries from a dataset.

---

## 💡 Why This Matters for Data Engineering
In a production-level data pipeline, your code will constantly encounter unexpected values (e.g., `None`, `-99`, `TIMEOUT`). Conditional logic is what allows your scripts to identify these anomalies and either correct them or route them to an error log rather than crashing your entire system.



---

## 🎯 Quick Learning Tip
Don't just read these files. Open `real_world_examples.py` and try to write a piece of logic that filters a list of sales data to remove all negative values. **If you can master the logic flow here, you will have no trouble building complex `pandas` filters later on.**
