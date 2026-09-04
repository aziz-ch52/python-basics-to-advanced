# ⚡ NumPy: High-Performance Numerical Computing

This directory covers **NumPy (Numerical Python)**, the foundational library for scientific computing, data analytics, and data engineering in Python. NumPy provides fast multidimensional arrays (`ndarray`) and vectorized mathematical routines executed at compiled C speed.

---

## 💡 Why This Matters for Data Engineering & Analytics

Standard Python lists store references to objects scattered across memory, causing significant pointer indirection and memory overhead. NumPy arrays solve this with **homogeneous, contiguous memory storage**, enabling:

* **Cache Locality:** Modern CPUs process contiguous memory blocks far faster than fragmented pointers.
* **Vectorization:** Replaces slow Python `for` loops with compiled C loops, running operations via SIMD (Single Instruction, Multiple Data).
* **Downstream Integration:** Libraries like `pandas`, `scipy`, `scikit-learn`, and `PyTorch` use NumPy array memory layouts internally.

---

## 📂 Curriculum & Theoretical Concepts

### 1. Introduction & Architecture
* **What is NumPy?**: A C-based Python package providing multi-dimensional arrays, mathematical routines, and linear algebra primitives.
* **NumPy vs. Python Lists**: Lists are heterogeneous collections of pointers with high per-element memory overhead. NumPy arrays are statically typed, packed blocks of uniform data.
* **Imports & Aliases**: By standard convention, imported using `import numpy as np`.

### 2. Array Creation Primitives
* **`ndarray`**: The core $N$-dimensional array object.
* **From Collections (`np.array`)**: Converts Python lists/tuples into typed arrays.
* **Zero & One Allocations (`np.zeros`, `np.ones`)**: Allocates and initializes memory to 0 or 1 with a specified shape and `dtype`.
* **Uninitialized Allocation (`np.empty`)**: Allocates memory without wiping previous cache values—fastest for immediate subsequent overwrites.
* **Constant Fills (`np.full`)**: Initializes an array of arbitrary shape with a specified scalar.
* **Sequences (`np.arange`, `np.linspace`)**: `arange` steps by a step-size (half-open $[start, stop)$); `linspace` generates $N$ evenly spaced points over a closed interval $[start, stop]$.
* **Identity Matrices (`np.eye`)**: Generates 2D square matrices with ones along the main diagonal and zeros elsewhere.

### 3. Array Metadata & Properties
* **`ndim`**: Number of axes (dimensions).
* **`shape`**: A tuple of integers showing the size along each axis.
* **`size`**: Total number of elements ($\prod shape_i$).
* **`dtype`**: Concrete data type of array elements (e.g., `int32`, `float64`).
* **`itemsize`**: Memory consumption of a single element in bytes.
* **`nbytes`**: Total memory consumed by array elements (`size * itemsize`).

### 4. Data Types & Memory Casting
* **Core Primitive Types**: Signed/unsigned integers (`int8` through `int64`, `uint8`), floats (`float16` to `float64`), booleans (`bool_`), and complex numbers (`complex128`).
* **Type Inference**: NumPy automatically coerces mixed types to the most flexible type (upcasting).
* **Type Conversion (`astype`)**: Explicitly casts an existing array into a new `dtype` via memory copying.

### 5. 1D Arrays
* Single-axis structures representing mathematical vectors.
* Supports positional indexing, scalar modification, and standard iteration.

### 6. 2D Arrays & Matrices
* Two-axis structures representing tabular grids (Axis 0 = Rows, Axis 1 = Columns).
* Element retrieval via coordinate tuples `[row, column]`.

### 7. Multidimensional Arrays ($N$-D)
* Hyper-dimensional data cubes (e.g., 3D tensors representing channels $\times$ height $\times$ width in image batches).
* **Axes System**: Directional paths through array structures (Axis 0, 1, 2, ..., $N-1$).

### 8. Indexing Systems
* **Zero-based Positive Indexing**: Traversal from the start index ($0$).
* **Negative Indexing**: Backward lookup from the end ($-1, -2$).
* **Coordinate Multi-indexing**: Comma-separated access (`arr[r, c]`), which avoids creating temporary intermediary arrays unlike Python's chained list syntax `list[r][c]`.

### 9. Slicing Mechanics
* Expressed as `arr[start:stop:step]` per axis.
* Slices return **views**, not copies; changes modify the underlying buffer.

### 10. Iteration & Traversal
* Native Python `for` loops iterate over the outer axis (Axis 0).
* **`np.nditer()`**: Optimized iterator object handling flat traversal, order management (C vs. Fortran contiguous), and in-place buffer mutation.

### 11. Shape Manipulation & Transformations
* **`reshape()`**: Changes dimension sizes without altering internal data buffer order (must preserve total element count).
* **`flatten()` vs. `ravel()`**: `flatten()` returns a contiguous copy; `ravel()` returns an uncopied 1D view whenever possible.
* **Transposition (`transpose()`, `.T`)**: Reverses or permutes axis orders.
* **Dimensional Modification (`squeeze()`, `expand_dims()` / `np.newaxis`)**: Strips or inserts unit dimensions ($1$-sized axes).

### 12. Splitting & Concatenation
* **Joining**: `np.concatenate` merges existing axes; `np.stack` creates and aligns along a brand-new axis. `vstack` stacks vertically (row-wise), `hstack` horizontally (column-wise).
* **Partitioning**: `np.split`, `hsplit`, `vsplit` divide arrays into equal or index-delineated sub-arrays.

### 13. Searching & Locating Elements
* **`where(condition, [x, y])`**: Vectorized ternary operator returning indices or selected values based on a boolean mask.
* **`argwhere`**: Locates array indices matching conditions in coordinate tuples.
* **`searchsorted`**: Binary search returning indices where elements should be inserted to maintain sort order.
* **`argmax` / `argmin`**: Returns the index position of extreme values along a target axis.

### 14. Boolean Masking & Conditional Filtering
* Element-wise comparison operations return boolean arrays (`arr > 5`).
* Bitwise operators (`&` AND, `|` OR, `~` NOT) are required instead of Python keywords (`and`, `or`, `not`) to evaluate element-by-element masks.
* Applying masks via `arr[mask]` extracts flat subsets meeting logical criteria.

### 15. Fancy Indexing
* Passing integer arrays/lists as indices (`arr[[1, 3, 4]]`) to select elements out of order.
* Unlike standard slices, fancy indexing **always produces a copy**, never a view.

### 16. Element-wise Arithmetic
* Standard arithmetic operators (`+`, `-`, `*`, `/`, `**`, `%`) operate element-by-element across identical shapes without explicit loops.

### 17. Universal Functions (ufuncs)
* Compiled C functions performing fast, element-by-element mathematical operations (`np.sqrt`, `np.abs`, `np.exp`, `np.log`, `np.floor`, `np.ceil`).

### 18. Vectorization Mechanics
* Replacing explicit application-level loops with array expressions.
* **`np.vectorize`**: Convenience wrapper for applying standard Python functions across arrays (note: provides cleaner syntax, but does not provide compiled C speed).

### 19. Broadcasting Paradigm
Broadcasting allows arithmetic operations between arrays of different shapes without copying data.
* **Trailing Dimensions Rule**: Starting from the trailing (rightmost) dimension, two shapes are compatible if:
  1. The dimensions are equal, or
  2. One of the dimensions is $1$.

### 20 & 21. Mathematical & Aggregation Functions
* Fast reductions across the entire array or targeted axes: `sum()`, `prod()`, `min()`, `max()`, `mean()`, `median()`, `std()`, `var()`.
* **Peak-to-Peak (`ptp()`)**: Evaluates the statistical range ($\max - \min$).

### 22. Axis Operations Deep Dive
* **`axis=0`**: Collapses rows; operation runs downwards through columns.
* **`axis=1`**: Collapses columns; operation runs across rows.

### 23. Statistical Computations
* Advanced population calculations: `percentile()`, `quantile()`, covariance (`cov()`), and correlation coefficient matrices (`corrcoef()`).

### 24. Pseudorandom Number Generation
* Generating numbers via `np.random` and modern `np.random.default_rng()`.
* Uniform distributions, standard normals, discrete random choices, and setting seed states for pipeline reproducibility.

### 25. Sorting Algorithms
* **`np.sort()`**: Returns an independently sorted array.
* **`np.argsort()`**: Returns the integer array of indices that would order the data (essential for sorting companion datasets based on a reference column).

### 26. Set Operations
* Fast unique element extractions and set logic: `np.unique()`, `union1d()`, `intersect1d()`, `setdiff1d()`, and `setxor1d()`.

### 27. Special Value Handling (Data Quality)
* Identification and handling of IEEE 754 floating-point anomalies: `np.nan` (Not a Number) and `np.inf` (Infinity).
* Validation checks using `np.isnan()`, `np.isinf()`, `np.isfinite()`.
* NaN-safe aggregations: `np.nansum()`, `np.nanmean()`, `np.nanstd()`.

### 28. Memory Management: Views vs. Deep Copies
* **View**: A shallow memory reference sharing the original base data buffer. Created via slices and transformations (`reshape`, `ravel`).
* **Copy**: Complete allocation of independent heap memory. Created via `np.copy()` or fancy indexing.
* Modifying views accidentally mutates the source array.

### 29. Performance & Storage Optimization
* Downcasting high-overhead types (`int64` $\to$ `int16`/`int8`) to reduce pipeline memory footprints.
* Benchmarking loop runtime costs against vectorized calls.

### 30. File I/O Operations
* Binary Serialization: `np.save()` and `np.load()` using fast, zero-parsing `.npy` and compressed `.npz` formats.
* Text Parsing: Loading structured tabular text via `np.loadtxt()` or the missing-value-tolerant `np.genfromtxt()`.

### 31. Linear Algebra Primitives
* Vector dot products and 2D matrix multiplication using `np.dot()` and the `@` operator.
* Matrix inversions (`np.linalg.inv`), determinants (`np.linalg.det`), and eigenvalue calculations.

### 32. Python Interoperability
* Bidirectional conversions between native lists, generator outputs, and array buffers.

### 33 & 34. Practical Problems & Real-World Projects
* Applying NumPy to data cleaning, normalizations ($z$-score scaling, min-max scaling), outlier detection masks, and tabular record aggregations.

---

## 🎯 Quick Learning Tip
When working through array operations, check whether an operation produces a **view** or a **copy** by checking `arr.base`. If `arr.base is None`, the array owns its memory; otherwise, it is viewing another array's buffer.
