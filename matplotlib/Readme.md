✅ Topics covered so far:

📈 Line plots with styles, color, labels, title, grid, and legend
📐 Data generation using arange, linspace for smooth curves
➕ Multiple functions in one plot (sin, cos together)
🪟 Subplots using plt.subplots() (vertical and horizontal layout)
🧱 Axes customization (figsize, set_title, set_ylabel)
💾 Saving plots as PNG with savefig() (with DPI, transparency)
🔵 Scatter plots for point-wise data visualization
📊 Bar charts using categories and values
📉 Histogram with custom bin size and grid



1. **Colors**
2. **Line Styles**
3. **Markers**
4. **Format string (`fmt`) shortcuts**

---

### 🎨 COLORS

| Code  | Color   | Long Name   |
| ----- | ------- | ----------- |
| `'b'` | Blue    | `'blue'`    |
| `'g'` | Green   | `'green'`   |
| `'r'` | Red     | `'red'`     |
| `'c'` | Cyan    | `'cyan'`    |
| `'m'` | Magenta | `'magenta'` |
| `'y'` | Yellow  | `'yellow'`  |
| `'k'` | Black   | `'black'`   |
| `'w'` | White   | `'white'`   |

You can also use hex codes like `'#ff5733'` or RGB tuples like `(0.1, 0.2, 0.5)`

---

### ➖ LINE STYLES

| Code             | Description | Full Arg (`linestyle`) |
| ---------------- | ----------- | ---------------------- |
| `'-'`            | Solid       | `'solid'`              |
| `'--'`           | Dashed      | `'dashed'`             |
| `'-.'`           | Dash-dot    | `'dashdot'`            |
| `':'`            | Dotted      | `'dotted'`             |
| `''` or `'None'` | No line     | `'none'`               |

---

### 🔵 MARKERS

| Code  | Shape            | Full Name          |           |
| ----- | ---------------- | ------------------ | --------- |
| `'.'` | Point marker     | `'point'`          |           |
| `','` | Pixel marker     | `'pixel'`          |           |
| `'o'` | Circle           | `'circle'`         |           |
| `'v'` | Triangle down    | `'triangle_down'`  |           |
| `'^'` | Triangle up      | `'triangle_up'`    |           |
| `'<'` | Triangle left    | `'triangle_left'`  |           |
| `'>'` | Triangle right   | `'triangle_right'` |           |
| `'1'` | Tri-down (thin)  | `'tri_down'`       |           |
| `'2'` | Tri-up (thin)    | `'tri_up'`         |           |
| `'3'` | Tri-left (thin)  | `'tri_left'`       |           |
| `'4'` | Tri-right (thin) | `'tri_right'`      |           |
| `'s'` | Square           | `'square'`         |           |
| `'p'` | Pentagon         | `'pentagon'`       |           |
| `'*'` | Star             | `'star'`           |           |
| `'h'` | Hexagon 1        | `'hexagon1'`       |           |
| `'H'` | Hexagon 2        | `'hexagon2'`       |           |
| `'+'` | Plus             | `'plus'`           |           |
| `'x'` | Cross            | `'x'`              |           |
| `'D'` | Diamond          | `'diamond'`        |           |
| `'d'` | Thin diamond     | `'thin_diamond'`   |           |
| \`'   | '\`              | Vertical line      | `'vline'` |
| `'_'` | Horizontal line  | `'hline'`          |           |

---

### 🧪 FORMAT STRING (`fmt`)

Format strings are a **combo of**:

```
color + marker + line style
```

| `fmt`    | Meaning                          |
| -------- | -------------------------------- |
| `'ro-'`  | red, circle marker, solid line   |
| `'g--'`  | green, dashed line               |
| `'bs:'`  | blue, square marker, dotted      |
| `'k^'`   | black, triangle-up marker, solid |
| `'m*--'` | magenta, star marker, dashed     |

💡 **Order doesn't matter**, `'--ro'`, `'or--'`, and `'--or'` are all valid.


---

# 🎨 MATPLOTLIB.PYPLOT FUNCTION CHEATLIST

---

## 📈 Basic Line Plot

| Function       | Syntax                                         | What it does               |
| -------------- | ---------------------------------------------- | -------------------------- |
| `plt.plot`     | `plt.plot(x, y, fmt='', **kwargs)`             | Line plot of y vs x        |
| `plt.show()`   | `plt.show()`                                   | Render the figure          |
| `plt.figure()` | `plt.figure(num=None, figsize=None, dpi=None)` | Create a new figure window |
| `plt.clf()`    | `plt.clf()`                                    | Clear current figure       |
| `plt.close()`  | `plt.close()`                                  | Close a figure             |

---

## 🏷️ Labels & Titles

| Function       | Syntax                                                          | What it does              |
| -------------- | --------------------------------------------------------------- | ------------------------- |
| `plt.title`    | `plt.title('Your Title', fontsize=12)`                          | Set plot title            |
| `plt.xlabel`   | `plt.xlabel('X label')`                                         | X-axis label              |
| `plt.ylabel`   | `plt.ylabel('Y label')`                                         | Y-axis label              |
| `plt.legend`   | `plt.legend(loc='best')`                                        | Show legend               |
| `plt.grid`     | `plt.grid(True)`                                                | Toggle grid lines         |
| `plt.axis`     | `plt.axis([xmin, xmax, ymin, ymax])`                            | Set axis range            |
| `plt.xticks`   | `plt.xticks(ticks, labels=None)`                                | Set custom X ticks        |
| `plt.yticks`   | `plt.yticks(ticks, labels=None)`                                | Set custom Y ticks        |
| `plt.text`     | `plt.text(x, y, 'text')`                                        | Draw text inside plot     |
| `plt.annotate` | `plt.annotate('text', xy=(x,y), xytext=(x2,y2), arrowprops={})` | Add annotation with arrow |

---

## 🧱 Multiple Plots & Subplots

| Function             | Syntax                               | What it does                    |
| -------------------- | ------------------------------------ | ------------------------------- |
| `plt.subplot`        | `plt.subplot(nrows, ncols, index)`   | Create grid and select one cell |
| `plt.subplots`       | `fig, ax = plt.subplots(rows, cols)` | Returns fig and array of axes   |
| `plt.tight_layout()` | `plt.tight_layout()`                 | Auto-layout to prevent overlap  |
| `plt.suptitle()`     | `plt.suptitle('Title')`              | Title for whole figure          |

---

## 🖍️ Line Format Options

| Param                      | Values                               | Description            |
| -------------------------- | ------------------------------------ | ---------------------- |
| `color` or `c`             | `'r'`, `'blue'`, `'#00ff00'`, etc.   | Line color             |
| `linestyle` or `ls`        | `'-'`, `'--'`, `':'`, `'-.', 'None'` | Line type              |
| `linewidth` or `lw`        | Float (e.g. `2.5`)                   | Line thickness         |
| `marker`                   | `'o'`, `'^'`, `'s'`, `'x'`, etc.     | Marker style           |
| `markersize` or `ms`       | Float                                | Marker size            |
| `markerfacecolor` or `mfc` | Color                                | Fill color of marker   |
| `markeredgecolor` or `mec` | Color                                | Border color of marker |
| `label`                    | `'My Line'`                          | Label for legend       |

can combine `color`, `linestyle`, and `marker` using format strings like `'ro--'`.

---

## 📊 Other Plot Types

| Type             | Function                         | Syntax                       |
| ---------------- | -------------------------------- | ---------------------------- |
| **Scatter**      | `plt.scatter(x, y, s=20, c='r')` | Dot plot                     |
| **Bar**          | `plt.bar(x, height)`             | Vertical bars                |
| **Barh**         | `plt.barh(y, width)`             | Horizontal bars              |
| **Histogram**    | `plt.hist(data, bins=10)`        | Distribution                 |
| **Boxplot**      | `plt.boxplot(data)`              | Box-and-whisker plot         |
| **Pie**          | `plt.pie(sizes, labels=...)`     | Pie chart                    |
| **Stem**         | `plt.stem(x, y)`                 | Discrete signal plot         |
| **Error Bars**   | `plt.errorbar(x, y, yerr=...)`   | Plot with error margins      |
| **Fill Between** | `plt.fill_between(x, y1, y2)`    | Shaded region between curves |

---

## 💾 Saving Plots

| Function        | Syntax                                 | What it does         |
| --------------- | -------------------------------------- | -------------------- |
| `plt.savefig()` | `plt.savefig("filename.png", dpi=300)` | Save to file         |
| `dpi`           | `plt.savefig(..., dpi=300)`            | Set image resolution |
| `transparent`   | `plt.savefig(..., transparent=True)`   | No background        |

---

## 🔁 Axes / Figure Control

| Function     | Syntax               | What it does       |
| ------------ | -------------------- | ------------------ |
| `plt.xlim()` | `plt.xlim(min, max)` | Set X-axis limits  |
| `plt.ylim()` | `plt.ylim(min, max)` | Set Y-axis limits  |
| `plt.gca()`  | `ax = plt.gca()`     | Get current axes   |
| `plt.gcf()`  | `fig = plt.gcf()`    | Get current figure |

---

## 🔍 Zooming/Styling Tips

| Feature               | How                                               |
| --------------------- | ------------------------------------------------- |
| Zoom in a section     | Use `plt.xlim()`, `plt.ylim()`                    |
| Add multiple lines    | Multiple `plt.plot()` calls                       |
| Customize per-subplot | Use `fig, ax = plt.subplots()` and access `ax[i]` |
| Use LaTeX             | Wrap labels like `r"$\sin(x)$"` for math style    |

---

## 📌 Common Use Pattern

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8,4))
plt.plot(x, y, label='sin(x)', color='red', linestyle='--', marker='o')
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("sine.png", dpi=300)
plt.show()
```

---
