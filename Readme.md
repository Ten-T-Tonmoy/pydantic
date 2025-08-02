# Numpy basics with JupyterNotebook 

## setup

- set up virtual environment python
```
    python -m venv venv

    venv\Scripts\activate
```

- dependencies
    ```
        pip install ipykernel jupyter
    ```



---

## 🧭 Modes to Know

* **Edit Mode** → You're typing inside a cell (`green bar`)
* **Command Mode** → You're controlling cells (`blue bar`)

Toggle between them:

| Action             | Shortcut |
| ------------------ | -------- |
| Enter Edit Mode    | `Enter`  |
| Enter Command Mode | `Esc`    |

---

## ✍️ Edit Mode Shortcuts (inside a cell)

| Action                 | Shortcut        |
| ---------------------- | --------------- |
| Run cell               | `Shift + Enter` |
| Run cell, stay in cell | `Ctrl + Enter`  |
| Run cell, insert below | `Alt + Enter`   |
| Autocomplete           | `Tab`           |
| Indent                 | `Tab`           |
| Dedent (un-indent)     | `Shift + Tab`   |
| Multicursor (VSCode)   | `Alt + Click`   |

---

## ⚙️ Command Mode Shortcuts (cell-level actions)

| Action                                   | Shortcut         |
| ---------------------------------------- | ---------------- |
| Run cell                                 | `Shift + Enter`  |
| Add cell below                           | `B`              |
| Add cell above                           | `A`              |
| Delete cell                              | `D D` (double D) |
| Cut cell                                 | `X`              |
| Copy cell                                | `C`              |
| Paste cell below                         | `V`              |
| Undo cell deletion                       | `Z`              |
| Merge cell below                         | `Shift + M`      |
| Change to code cell                      | `Y`              |
| Change to markdown cell                  | `M`              |
| Save notebook                            | `Ctrl + S`       |
| Select multiple cells (like shift+click) | `Shift + ↑ / ↓`  |

---

## 🧽 Markdown Helpers (in markdown cells)

| Action        | Syntax                          |
| ------------- | ------------------------------- |
| Heading       | `#`, `##`, etc.                 |
| Bold          | `**bold**`                      |
| Italic        | `*italic*`                      |
| Code          | `` `code` ``                    |
| Code block    | <pre>`python<br>code<br>`</pre> |
| Bullet list   | `- item`                        |
| Numbered list | `1. item`                       |

---

## 🧠 Bonus Tips

* `Ctrl + Shift + P` → VSCode command palette (type `jupyter` to explore extensions/settings)
* `Ctrl + /` → Toggle comment in a code cell
* `Ctrl + K Ctrl + S` → See **all shortcuts** in VSCode

