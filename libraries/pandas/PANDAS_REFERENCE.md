# Pandas Core Function Reference

This document serves as a rapid-reference guide for the most critical Pandas methods utilized in daily data analysis and engineering workflows. 

## 1. Input / Output (I/O)
Functions used to ingest and export data from external storage.

| Function | Description | Primary Use Case |
| :--- | :--- | :--- |
| `pd.read_csv()` | Loads a CSV file into a DataFrame. | Ingesting raw, comma-separated flat files. |
| `pd.read_excel()` | Loads an Excel file into a DataFrame. | Reading client or financial reports (.xlsx). |
| `df.to_csv()` | Exports a DataFrame to a CSV file. | Saving cleaned data for database ingestion. Use `index=False`. |
| `df.to_excel()` | Exports a DataFrame to an Excel file. | Generating final reports for non-technical stakeholders. |

## 2. Data Inspection & Profiling
Methods for understanding the shape, structure, and quality of a new dataset.

| Function | Description | Primary Use Case |
| :--- | :--- | :--- |
| `df.head(n)` / `df.tail(n)` | Returns the first/last *n* rows. | Quick visual verification of data structure and column alignment. |
| `df.info()` | Prints summary of columns, null counts, and data types. | Mandatory first step to identify missing data and type mismatches. |
| `df.describe()` | Calculates summary statistics for numeric columns. | Quickly spotting outliers, min/max bounds, and distribution. |
| `df.value_counts()` | Counts unique values in a specific Series. | Finding the frequency distribution of categorical data (e.g., user types). |
| `df.shape` | Returns a tuple of (rows, columns). | Verifying dataset size before and after merges or drops. |

## 3. Data Selection & Filtering
Functions for slicing the dataset and extracting precise data points.

| Function | Description | Primary Use Case |
| :--- | :--- | :--- |
| `df.loc[]` | Selects rows/columns by explicit label. | Extracting specific named rows or specific column headers. |
| `df.iloc[]` | Selects rows/columns by integer position (0-indexed). | Extracting rows based purely on their numeric order. |
| `df.query()` | Filters rows using a boolean string expression. | Writing clean, readable multi-condition filters without bracket clutter. |
| `Series.isin()` | Filters based on a list of target values. | Replacing long "OR" logic chains. Equivalent to SQL `IN`. |

## 4. Data Cleaning
Methods for handling missing, corrupt, or unnecessary data.

| Function | Description | Primary Use Case |
| :--- | :--- | :--- |
| `df.isna()` | Returns a boolean mask of missing values. | Used with `.sum()` to map exactly where the dataset is broken. |
| `df.dropna()` | Removes rows or columns containing missing values. | Purging completely corrupt rows where imputation is impossible. |
| `df.fillna()` | Replaces missing values with a specified value. | Replacing NaNs with mathematical means or logical defaults. |
| `df.drop()` | Removes specified rows or columns. | Stripping out useless features (columns) to save memory. |
| `df.rename()` | Alters column headers or row indices. | Standardizing inconsistent headers (e.g., removing spaces/capitalizing) before database loading. |

## 5. Data Transformation
Functions applied to modify existing data or create new calculated fields.

| Function | Description | Primary Use Case |
| :--- | :--- | :--- |
| `df.apply()` | Executes a custom function along an axis. | Applying complex if/else logic or string parsing to every row. |
| `df.astype()` | Casts a Pandas object to a specified data type. | Fixing incorrect types (e.g., converting a string '100' to an integer 100). |
| `pd.to_datetime()`| Converts strings to Pandas datetime objects. | Enabling time-series analysis on date columns. |

## 6. Grouping & Aggregation
Methods for summarizing data across categories.

| Function | Description | Primary Use Case |
| :--- | :--- | :--- |
| `df.groupby()` | Splits data into groups based on some criteria. | The equivalent of SQL `GROUP BY`. Precursor to any mathematical aggregation. |
| `df.agg()` | Applies one or multiple math functions across columns. | Generating complex summaries (e.g., Sum of Revenue AND Average of Units simultaneously). |

## 7. Merging & Reshaping
Functions for combining multiple datasets and altering dimensional structure.

| Function | Description | Primary Use Case |
| :--- | :--- | :--- |
| `pd.merge()` | Joins two DataFrames on a common key. | Relational joining (Inner, Left, Outer). Equivalent to SQL `JOIN`. |
| `pd.concat()` | Stacks DataFrames vertically or horizontally. | Appending new rows of identical data to an existing table (SQL `UNION`). |
| `pd.pivot_table()`| Creates a spreadsheet-style pivot table. | Multidimensional summarization for financial or reporting dashboards. |
| `pd.melt()` | Unpivots a DataFrame from wide to long format. | Normalizing wide, messy report data into strict columnar formats required by BI tools (like Power BI). |
