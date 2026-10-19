# Pandas: Data Analysis and Manipulation

Pandas is a foundational open-source library for Python, designed specifically for data manipulation and analysis. It provides high-performance data structures and analytical tools for handling numerical tables and time-series data.

## History and Origin

* **Creator:** Wes McKinney.
* **Year of Inception:** 2008.
* **Origin Location:** AQR Capital Management, a financial firm.
* **Motivation:** McKinney recognized a significant gap in how people were handling data in Python; he needed a tool to make working with structured financial data faster and more efficient.
* **Etymology:** The name is a playful nod to "Panel Data," an econometrics term referring to multidimensional structured datasets collected over time.
* **Open Source Release:** Released to the public in 2009.

## Technical Specifications

* **Primary Language:** Python. (It uses C and Cython under the hood for performance-critical operations.)
* **Current Stable Version:** 3.0.6 (Released September 17, 2026).
* **Compatibility:** Pandas 3.0.6 supports Python 3.11 and higher, including full compatibility with Python 3.15.

## Core Architecture

Pandas bridges the gap between the programmatic power of Python and the structured querying logic found in SQL and enterprise spreadsheet software. It operates primarily on two data structures:

1. **Series:** A one-dimensional labeled array capable of holding any data type.
2. **DataFrame:** A two-dimensional, size-mutable tabular data structure with labeled axes (rows and columns).

## Repository Learning Sequence

This directory is structured chronologically to mirror an authentic data analysis workflow. Moving from initial data ingestion to advanced restructuring, this sequence builds foundational logic before abstracting into complex data engineering operations.

| Sequence | Module | Objective |
| --- | --- | --- |
| **01** | `01_series_and_dataframes.py` | Constructing core data structures from lists, dictionaries, and arrays. |
| **02** | `02_reading_and_writing_data.py` | Executing I/O operations for CSV, Excel, and JSON formats. |
| **03** | `03_inspecting_and_summarizing.py` | Profiling new datasets using `.head()`, `.info()`, and `.describe()`. |
| **04** | `04_selection_and_indexing.py` | Precision data extraction utilizing `.loc[]` and `.iloc[]`. |
| **05** | `05_filtering_and_boolean_indexing.py` | Conditional row filtering, mirroring SQL `WHERE` logic. |
| **06** | `06_handling_missing_data.py` | Identifying and standardizing dirty data (`.dropna()`, `.fillna()`). |
| **07** | `07_data_transformation.py` | Column manipulation, renaming, and functional mapping via `.apply()`. |
| **08** | `08_grouping_and_aggregation.py` | Aggregating metrics by category, mirroring SQL `GROUP BY` statements. |
| **09** | `09_merging_and_joining.py` | Combining diverse datasets via relational logic (`INNER JOIN`, `LEFT JOIN`). |
| **10** | `10_pivot_tables_and_reshaping.py` | Dimensional reshaping of tabular data using `pivot_table()` and `melt()`. |

## Installation

To ensure environment consistency with the scripts in this directory, install the modern 3.0.x series of Pandas:

```bash
pip install pandas==3.0*

```
