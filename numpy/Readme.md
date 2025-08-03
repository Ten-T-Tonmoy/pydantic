✅ Topics covered so far:
There goes:

📐 Array creation (including zeros, ones, full, eye, random)

🧱 Shapes, dimensions, slicing, reshaping, flattening

➕ Math operations: add, dot, mean, sin, max, broadcasting

🧠 Boolean masking & filtering

🔀 Stacking arrays (vstack/hstack)

🎲 Random number generation (Python + NumPy)

🧠 Time comparison with raw Python

📈 Sorting, searching (argsort, where, count_nonzero)

🧮 Linear Algebra (inv, det, eig)

💾 Saving & loading from .npy, .csv




---

# 🧠 NUMPY FUNCTION CHEATLIST

---

## 📏 Array Creation

| Function      | Syntax                                                                       | What it does                                |
| ------------- | ---------------------------------------------------------------------------- | ------------------------------------------- |
| `np.array`    | `np.array(object, dtype=None, copy=True, ndmin=0)`                           | Converts list/tuple into NumPy array        |
| `np.zeros`    | `np.zeros(shape, dtype=float)`                                               | Array of 0s                                 |
| `np.ones`     | `np.ones(shape, dtype=float)`                                                | Array of 1s                                 |
| `np.full`     | `np.full(shape, fill_value, dtype=None)`                                     | Array filled with a constant                |
| `np.eye`      | `np.eye(N, M=None, k=0, dtype=float)`                                        | Identity matrix                             |
| `np.empty`    | `np.empty(shape, dtype=float)`                                               | Uninitialized array (random garbage values) |
| `np.arange`   | `np.arange(start, stop, step, dtype=None)`                                   | Range with step (like Python `range`)       |
| `np.linspace` | `np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)` | `num` evenly spaced points                  |
| `np.logspace` | `np.logspace(start, stop, num=50, base=10.0)`                                | `log` spaced points                         |

---

## 🛠️ Array Manipulation

| Function         | Syntax                                         | What it does                |
| ---------------- | ---------------------------------------------- | --------------------------- |
| `np.reshape`     | `np.reshape(a, newshape)`                      | Reshape array               |
| `np.ravel`       | `np.ravel(a)`                                  | Flattens array              |
| `np.transpose`   | `np.transpose(a, axes=None)`                   | Swaps axes                  |
| `np.concatenate` | `np.concatenate((a1, a2, ...), axis=0)`        | Joins arrays                |
| `np.stack`       | `np.stack(arrays, axis=0)`                     | Stack along new axis        |
| `np.hstack`      | `np.hstack((a1, a2, ...))`                     | Horizontal stack            |
| `np.vstack`      | `np.vstack((a1, a2, ...))`                     | Vertical stack              |
| `np.split`       | `np.split(array, indices_or_sections, axis=0)` | Splits into multiple arrays |

---

## 🧮 Math Operations

| Function      | Syntax                    | What it does                |
| ------------- | ------------------------- | --------------------------- |
| `np.add`      | `np.add(x1, x2)`          | Element-wise addition       |
| `np.subtract` | `np.subtract(x1, x2)`     | Element-wise subtraction    |
| `np.multiply` | `np.multiply(x1, x2)`     | Element-wise multiplication |
| `np.divide`   | `np.divide(x1, x2)`       | Element-wise division       |
| `np.power`    | `np.power(x1, x2)`        | Raise to power              |
| `np.sqrt`     | `np.sqrt(x)`              | Square root                 |
| `np.abs`      | `np.abs(x)`               | Absolute value              |
| `np.round`    | `np.round(x, decimals=0)` | Round to decimals           |

---

## 🔁 Matrix Operations

| Function         | Syntax              | What it does                         |
| ---------------- | ------------------- | ------------------------------------ |
| `np.dot`         | `np.dot(a, b)`      | Matrix multiplication                |
| `np.matmul`      | `np.matmul(a, b)`   | Matrix multiplication (supports >2D) |
| `np.linalg.inv`  | `np.linalg.inv(a)`  | Matrix inverse                       |
| `np.linalg.det`  | `np.linalg.det(a)`  | Determinant                          |
| `np.linalg.eig`  | `np.linalg.eig(a)`  | Eigenvalues and eigenvectors         |
| `np.linalg.norm` | `np.linalg.norm(a)` | Vector/matrix norm                   |

---

## 📊 Stats & Aggregation

| Function    | Syntax                    | What it does       |
| ----------- | ------------------------- | ------------------ |
| `np.mean`   | `np.mean(a, axis=None)`   | Average            |
| `np.median` | `np.median(a, axis=None)` | Median             |
| `np.std`    | `np.std(a, axis=None)`    | Standard deviation |
| `np.var`    | `np.var(a, axis=None)`    | Variance           |
| `np.min`    | `np.min(a, axis=None)`    | Min value          |
| `np.max`    | `np.max(a, axis=None)`    | Max value          |
| `np.sum`    | `np.sum(a, axis=None)`    | Total sum          |
| `np.cumsum` | `np.cumsum(a, axis=None)` | Cumulative sum     |
| `np.argmin` | `np.argmin(a)`            | Index of min       |
| `np.argmax` | `np.argmax(a)`            | Index of max       |

---

## 🎯 Indexing & Conditionals

| Function     | Syntax                      | What it does                             |
| ------------ | --------------------------- | ---------------------------------------- |
| `np.where`   | `np.where(condition, x, y)` | If condition is true, take `x`, else `y` |
| `np.nonzero` | `np.nonzero(a)`             | Indices of non-zero elements             |
| `np.any`     | `np.any(a)`                 | True if any True                         |
| `np.all`     | `np.all(a)`                 | True if all True                         |
| `np.argsort` | `np.argsort(a)`             | Indices to sort array                    |
| `np.sort`    | `np.sort(a)`                | Sorted array                             |

---

## 🎲 Random

| Function            | Syntax                                         | What it does                 |
| ------------------- | ---------------------------------------------- | ---------------------------- |
| `np.random.rand`    | `np.random.rand(d0, d1, ...)`                  | Uniform \[0, 1) floats       |
| `np.random.randn`   | `np.random.randn(d0, d1, ...)`                 | Standard normal distribution |
| `np.random.randint` | `np.random.randint(low, high=None, size=None)` | Random ints                  |
| `np.random.choice`  | `np.random.choice(a, size, replace=True)`      | Random picks                 |
| `np.random.seed`    | `np.random.seed(seed)`                         | Fix random state             |

---

## 🧼 Boolean / Masking

| Function    | Syntax                             | What it does                       |
| ----------- | ---------------------------------- | ---------------------------------- |
| `a[a > 5]`  | Direct filtering                   | Select elements matching condition |
| `np.isin`   | `np.isin(elements, test_elements)` | Element-wise check if in set       |
| `np.unique` | `np.unique(a)`                     | Sorted unique values               |

---

## 📐 Fourier / Signal Ops

| Function      | Syntax                           | What it does           |
| ------------- | -------------------------------- | ---------------------- |
| `np.fft.fft`  | `np.fft.fft(a)`                  | Fast Fourier Transform |
| `np.fft.ifft` | `np.fft.ifft(a)`                 | Inverse FFT            |
| `np.convolve` | `np.convolve(a, v, mode='full')` | Convolution            |

---
