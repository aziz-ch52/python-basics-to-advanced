
# ⚡ NumPy: High-Performance Numerical Computing

Welcome to the **NumPy** learning directory of the Python Basics to Advanced repository.

NumPy (Numerical Python) is a foundational open-source library for numerical computing, scientific computing, and data analysis in Python.

It provides powerful multidimensional arrays (`ndarray`), mathematical operations, statistical functions, and efficient numerical computation.

NumPy is widely used in Data Analytics, Data Science, Machine Learning, Scientific Computing, and Data Engineering.

This directory contains structured, step-by-step learning materials designed to help students understand NumPy fundamentals, explore its core functionality, and apply numerical computing concepts through practical Python examples.

---

## 📖 History and Origin

| Attribute | Description |
|---|---|
| **Library Name** | NumPy |
| **Full Form** | Numerical Python |
| **Creator** | Travis Oliphant and the early NumPy development community |
| **Initial Release** | 2006 |
| **Programming Languages** | Python and C |
| **Core Data Structure** | `ndarray` |
| **Primary Purpose** | Numerical computing and multidimensional array manipulation |
| **License** | BSD 3-Clause License |

### Motivation

NumPy was developed to unify and improve the Python scientific computing ecosystem.

It combined important capabilities from earlier numerical libraries, particularly **Numeric** and **Numarray**, into a more consistent and efficient framework.

The objective was to provide Python developers with a powerful numerical computing foundation that could handle large datasets and mathematical operations efficiently.

### Ecosystem Impact

NumPy is one of the foundational components of the Python scientific computing ecosystem.

Many popular libraries use NumPy arrays or integrate with NumPy-based numerical workflows.

Examples include:

| Library | Relationship with NumPy |
|---|---|
| **Pandas** | Uses NumPy extensively for numerical data processing and array operations |
| **SciPy** | Builds on NumPy for scientific computing, optimization, and mathematical functions |
| **Scikit-Learn** | Uses NumPy arrays extensively for machine learning data processing |
| **Matplotlib** | Supports NumPy arrays as inputs for visualization |
| **PyTorch** | Supports conversion between NumPy arrays and tensors |
| **TensorFlow** | Supports NumPy-compatible numerical workflows and array interoperability |

> **Important:** These libraries do not all depend on NumPy in exactly the same way. Some use it extensively, while others provide interoperability or support NumPy-compatible operations.

---

## 🛠️ Technical Specifications

| Specification | Details |
|---|---|
| **Library** | NumPy |
| **Primary Language** | Python |
| **Implementation** | Python and optimized compiled code, including C |
| **Core Object** | `ndarray` |
| **Array Dimensions** | One-dimensional, two-dimensional, and higher-dimensional arrays |
| **Data Storage** | Homogeneous numerical data with a defined data type |
| **Supported Operations** | Mathematical, statistical, logical, and array manipulation operations |
| **Performance** | Optimized numerical operations implemented in compiled code |
| **Installation** | `pip install numpy` |
| **Official Documentation** | [numpy.org/doc](https://numpy.org/doc/) |

### Current Version

NumPy 2.0 introduced significant changes to the library, including API updates and improvements to its numerical computing infrastructure.

The exact latest stable release may change over time.

Check the official release information before installing or documenting a specific version:

[NumPy Releases](https://numpy.org/news/)

---

## 🧠 Core Architecture: Why NumPy Matters

Understanding NumPy's architecture helps explain why it is widely used for numerical computing.

### 1. NumPy Arrays (`ndarray`)

The central data structure in NumPy is the `ndarray`, which represents a multidimensional array of elements.

Unlike a standard Python list, a NumPy array generally stores elements using a consistent data type.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)
print(type(arr))
print(arr.dtype)
```

Output:

```text
[10 20 30 40 50]
<class 'numpy.ndarray'>
int64
```

The exact integer data type may vary depending on the platform and how the array is created.

### 2. Memory Efficiency

Standard Python lists store references to Python objects.

NumPy arrays typically store their numerical elements in a more compact, homogeneous memory representation.

This reduces memory overhead for many numerical workloads and makes large-scale numerical operations more efficient.

### 3. Cache Locality

NumPy arrays can store elements in contiguous memory layouts.

This allows processors to access nearby elements efficiently and can improve cache utilization.

However, not every NumPy array is contiguous. Slicing, transposition, and other operations can produce non-contiguous views.

### 4. Vectorization

NumPy allows mathematical operations to be applied to entire arrays without writing explicit Python loops.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

result = arr * 2

print(result)
```

Output:

```text
[20 40 60 80]
```

The operation is performed using NumPy's optimized numerical implementation.

Vectorization often reduces Python-level overhead and improves performance for numerical workloads.

### 5. Broadcasting

Broadcasting allows NumPy to perform operations between compatible arrays of different shapes.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30])

result = arr + 5

print(result)
```

Output:

```text
[15 25 35]
```

Broadcasting allows the scalar value `5` to participate in the operation without manually creating a separate array of repeated values.

### 6. Mathematical Computation

NumPy provides a wide range of mathematical operations, including:

- Arithmetic operations
- Statistical calculations
- Trigonometric functions
- Aggregation
- Linear algebra
- Random number generation
- Logical operations

These capabilities make NumPy an essential foundation for numerical analysis and scientific computing.

---

## 📚 Repository Learning Sequence

This directory is organized chronologically to guide students from basic NumPy concepts to multidimensional array manipulation and numerical operations.

Each Python file focuses on a specific topic and includes practical coding examples.

| Sequence | Module | Learning Objective |
|---|---|---|
| 01 | `01_NumPy_Introduction.py` | Understand NumPy, its purpose, array fundamentals, and the difference between NumPy arrays and Python lists. |
| 02 | `02_Array_Creation.py` | Create arrays using `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, and `np.linspace()`. |
| 03 | `03_Array_Attributes.py` | Understand array metadata using `ndim`, `shape`, `size`, `dtype`, and `itemsize`. |
| 04 | `04_Array_Indexing.py` | Access individual elements in one-dimensional, two-dimensional, and multidimensional arrays. |
| 05 | `05_Array_Slicing.py` | Extract portions of arrays using slicing and understand how views and copies behave. |
| 06 | `06_Array_Reshaping.py` | Change array dimensions using `reshape()`, `flatten()`, and `ravel()`. |
| 07 | `07_Array_Iteration.py` | Traverse arrays using Python loops and NumPy iteration tools such as `np.nditer()`. |
| 08 | `08_Array_Joining.py` | Combine arrays using `np.concatenate()`, `np.vstack()`, and `np.hstack()`. |
| 09 | `09_Array_Splitting.py` | Divide arrays into smaller arrays using `np.split()`, `np.hsplit()`, and `np.vsplit()`. |
| 10 | `10_Array_Operations.py` | Perform arithmetic operations, understand universal functions (ufuncs), and explore broadcasting fundamentals. |
| 11 | `11_Array_Sorting.py` | Sort array elements using `np.sort()` and `np.argsort()`. |
| 12 | `12_Array_Searching.py` | Locate elements using `np.where()`, `np.argmax()`, and `np.searchsorted()`. |
| 13 | `13_Boolean_Indexing_Filtering.py` | Filter arrays using Boolean conditions and logical operators such as `&`, `|`, and `~`. |

---

## 🔍 Detailed Learning Objectives

### 01. NumPy Introduction

**File:** `01_NumPy_Introduction.py`

Understand the fundamentals of NumPy and why it is important in Python development.

Topics:

- Introduction to NumPy
- Installing and importing NumPy
- Understanding `ndarray`
- Python lists vs. NumPy arrays
- Basic numerical operations
- Introduction to vectorization

### 02. Array Creation

**File:** `02_Array_Creation.py`

Learn how to create NumPy arrays using different methods.

Topics:

- `np.array()`
- `np.zeros()`
- `np.ones()`
- `np.empty()`
- `np.arange()`
- `np.linspace()`
- Creating one-dimensional arrays
- Creating multidimensional arrays

### 03. Array Attributes

**File:** `03_Array_Attributes.py`

Learn how to inspect the properties and structure of NumPy arrays.

Topics:

- `ndim`
- `shape`
- `size`
- `dtype`
- `itemsize`
- `nbytes`

### 04. Array Indexing

**File:** `04_Array_Indexing.py`

Understand how to access individual array elements.

Topics:

- Zero-based indexing
- Positive indexing
- Negative indexing
- Two-dimensional indexing
- Multidimensional indexing

### 05. Array Slicing

**File:** `05_Array_Slicing.py`

Learn how to extract specific portions of arrays.

Topics:

- Basic slicing
- Start, stop, and step
- Negative slicing
- Two-dimensional slicing
- Selecting rows and columns
- Views vs. copies

### 06. Array Reshaping

**File:** `06_Array_Reshaping.py`

Understand how to change array dimensions without changing the underlying element count.

Topics:

- `reshape()`
- `flatten()`
- `ravel()`
- `transpose()`
- `np.reshape()`
- Changing array dimensions

### 07. Array Iteration

**File:** `07_Array_Iteration.py`

Learn how to traverse array elements.

Topics:

- Iterating through one-dimensional arrays
- Iterating through multidimensional arrays
- Nested loops
- `np.nditer()`
- Iteration order

### 08. Array Joining

**File:** `08_Array_Joining.py`

Learn how to combine multiple arrays.

Topics:

- `np.concatenate()`
- `np.vstack()`
- `np.hstack()`
- Joining arrays along different axes

### 09. Array Splitting

**File:** `09_Array_Splitting.py`

Learn how to divide arrays into smaller arrays.

Topics:

- `np.split()`
- `np.hsplit()`
- `np.vsplit()`
- Splitting arrays along different axes

### 10. Array Operations

**File:** `10_Array_Operations.py`

Understand how NumPy performs mathematical operations on arrays.

Topics:

- Addition
- Subtraction
- Multiplication
- Division
- Modulus
- Exponentiation
- Universal functions (ufuncs)
- Broadcasting fundamentals

### 11. Array Sorting

**File:** `11_Array_Sorting.py`

Learn how to organize array elements.

Topics:

- `np.sort()`
- `np.argsort()`
- Sorting one-dimensional arrays
- Sorting multidimensional arrays
- Sorting along axes
- Understanding sorted indices

### 12. Array Searching

**File:** `12_Array_Searching.py`

Learn how to locate elements within arrays.

Topics:

- `np.where()`
- `np.argmax()`
- `np.argmin()`
- `np.searchsorted()`
- Searching with conditions
- Locating maximum and minimum values

### 13. Boolean Indexing & Filtering

**File:** `13_Boolean_Indexing_Filtering.py`

Learn how to select array elements based on logical conditions.

Topics:

- Boolean arrays
- Conditional filtering
- Comparison operators
- Logical AND (`&`)
- Logical OR (`|`)
- Logical NOT (`~`)
- Combining multiple conditions

---

## 🎯 Quick Learning Tip: Views vs. Copies

One of the most important concepts in NumPy is understanding the difference between a **view** and a **copy**.

### What Is a View?

A view is an array that provides access to data stored in another array's memory.

A view may share the underlying data buffer with its original array.

Modifying a view can therefore modify the original array.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

view = arr[1:4]

view[0] = 999

print(arr)
print(view)
```

Output:

```text
[ 10 999  30  40  50]
[999  30  40]
```

The original array changes because the sliced array shares its data.

### What Is a Copy?

A copy creates an independent array containing its own data.

Modifying the copy does not modify the original array.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

copy_arr = arr[1:4].copy()

copy_arr[0] = 999

print(arr)
print(copy_arr)
```

Output:

```text
[10 20 30 40 50]
[999  30  40]
```

The original array remains unchanged.

### Understanding `arr.base`

The `base` attribute can help investigate whether an array shares its data with another array.

```python
import numpy as np

arr = np.array([10, 20, 30, 40])

view = arr[1:3]

copy_arr = arr[1:3].copy()

print(arr.base)
print(view.base)
print(copy_arr.base)
```

For these examples:

- `arr.base` is `None` because `arr` owns its data.
- `view.base` references the underlying array.
- `copy_arr.base` is `None` because the copied array owns its data.

**Important:** `arr.base` is useful for inspecting memory relationships, but it is not a complete or universal test for whether two arrays share memory.

For a more direct check, use:

```python
np.shares_memory(arr, view)
```

This checks whether the arrays share memory.

---

## 🛠️ Installation

Before executing the Python scripts, make sure NumPy is installed in your Python environment.

### Install NumPy

```bash
pip install numpy
```

### Verify Installation

```python
import numpy as np

print(np.__version__)
```

This displays the installed NumPy version.

### Run a Python Script

Navigate to the NumPy directory:

```bash
cd NumPy
```

Execute the first learning file:

```bash
python 01_NumPy_Introduction.py
```

Continue with the remaining files in chronological order.

---

## 📂 Directory Structure

```text
NumPy/
│
├── README.md
├── LEARNING_GUIDE.md
├── PRACTICE_QUESTIONS.md
│
├── 01_NumPy_Introduction.py
├── 02_Array_Creation.py
├── 03_Array_Attributes.py
├── 04_Array_Indexing.py
├── 05_Array_Slicing.py
├── 06_Array_Reshaping.py
├── 07_Array_Iteration.py
├── 08_Array_Joining.py
├── 09_Array_Splitting.py
├── 10_Array_Operations.py
├── 11_Array_Sorting.py
├── 12_Array_Searching.py
└── 13_Boolean_Indexing_Filtering.py
```

---

## 📌 Learning Guidelines

To develop a strong understanding of NumPy:

1. Follow the learning sequence in chronological order.
2. Read the explanations before executing the examples.
3. Write the code yourself instead of only copying it.
4. Modify array values and experiment with different dimensions.
5. Understand the output of every operation.
6. Practice indexing, slicing, and filtering independently.
7. Learn how to interpret Python and NumPy errors.
8. Complete the practice questions after studying the topics.
9. Apply the concepts to real-world numerical datasets.

---

## 📚 Official Documentation

Use the official NumPy documentation whenever you need additional explanations, function parameters, or advanced examples.

- [NumPy Official Documentation](https://numpy.org/doc/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [NumPy Reference](https://numpy.org/doc/stable/reference/)
- [NumPy Installation Guide](https://numpy.org/install/)

---

## 🚀 What's Next?

After completing the NumPy fundamentals, continue with:

| Next Step | Learning Objective |
|---|---|
| **Pandas** | Learn data manipulation, cleaning, filtering, and analysis |
| **Matplotlib** | Learn to create data visualizations |
| **Seaborn** | Learn statistical visualization and exploratory analysis |
| **Scikit-Learn** | Learn machine learning fundamentals |

NumPy provides the numerical foundation for many of these tools.

Developing a strong understanding of NumPy will make it easier to work with structured datasets, perform calculations, and understand data analysis workflows.

---

## 🎓 Final Learning Advice

Do not focus on memorizing every NumPy function.

Focus on understanding:

- How arrays work
- How data is organized
- How to select and manipulate elements
- How numerical operations are performed
- How to interpret results
- How to apply NumPy to practical problems

**Learn the concepts. Practice the code. Understand the output. Build real solutions.**

---

**Happy Coding! 🐍**
<br>
**- Aziz Chharchhoda**
