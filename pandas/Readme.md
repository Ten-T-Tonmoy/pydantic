
## File Save & Load

---

# 📝 Table 1: Saving Data — `to_*` Methods (CSV, JSON, DB, Excel)

| Argument       | CSV                        | JSON                     | DB (SQL)                    | Excel                  | Description / Notes                                  |
| -------------- | -------------------------- | ------------------------ | --------------------------- | ---------------------- | ---------------------------------------------------- |
| `path_or_buf`  | File path / buffer         | File path / buffer       | SQL connection / engine     | File path / buffer     | Where to save data                                   |
| `sep`          | Yes (default `,`)          | No                       | No                          | No                     | Field separator (CSV only)                           |
| `columns`      | Yes                        | Yes                      | Yes                         | Yes                    | Columns to write                                     |
| `index`        | Yes (default True)         | Yes                      | No (ignored)                | Yes                    | Write index (row labels)                             |
| `header`       | Yes (default True)         | No                       | No                          | Yes                    | Write column names                                   |
| `mode`         | Yes (default 'w')          | No                       | No                          | No                     | Write mode (append/overwrite, CSV only)              |
| `encoding`     | Yes (default None → UTF-8) | Yes                      | No                          | Yes                    | File encoding                                        |
| `compression`  | Yes                        | Yes                      | No                          | Yes                    | Compress output (gzip, bz2, zip, xz)                 |
| `date_format`  | Yes                        | Yes                      | No                          | Yes                    | Format for datetime columns                          |
| `float_format` | Yes                        | No                       | No                          | Yes                    | Format float numbers                                 |
| `json_format`  | N/A                        | `records`, `split`, etc. | N/A                         | N/A                    | JSON output format                                   |
| `orient`       | N/A                        | Yes                      | N/A                         | N/A                    | Controls JSON structure                              |
| `if_exists`    | N/A                        | N/A                      | `fail`, `replace`, `append` | N/A                    | Behavior if table exists (DB only)                   |
| `index_label`  | Yes                        | No                       | No                          | Yes                    | Label for index column                               |
| `sheet_name`   | N/A                        | N/A                      | N/A                         | Yes (default 'Sheet1') | Excel sheet name                                     |
| `engine`       | N/A                        | N/A                      | N/A                         | Yes                    | Excel engine to use (`openpyxl`, `xlsxwriter`, etc.) |
| `chunksize`    | N/A                        | N/A                      | Yes                         | N/A                    | Rows per batch (DB only)                             |

---

# 📝 Table 2: Loading Data — `read_*` Methods (CSV, JSON, DB, Excel)

| Argument             | CSV                      | JSON                     | DB (SQL)                | Excel                | Description / Notes                       |
| -------------------- | ------------------------ | ------------------------ | ----------------------- | -------------------- | ----------------------------------------- |
| `filepath_or_buffer` | File path / URL / buffer | File path / URL / buffer | SQL connection / engine | File path / buffer   | Source location                           |
| `sep`                | Yes (default `,`)        | No                       | No                      | No                   | Field delimiter (CSV only)                |
| `header`             | Yes (int or list)        | No                       | No                      | Yes (int or list)    | Row number(s) to use as column names      |
| `names`              | Yes                      | No                       | No                      | Yes                  | Column names if header not present        |
| `index_col`          | Yes                      | No                       | No                      | Yes                  | Column(s) to use as index                 |
| `usecols`            | Yes                      | No                       | No                      | Yes                  | Columns to parse                          |
| `dtype`              | Yes                      | No                       | No                      | Yes                  | Data types for columns                    |
| `parse_dates`        | Yes                      | No                       | No                      | Yes                  | Columns to parse as dates                 |
| `na_values`          | Yes                      | No                       | No                      | Yes                  | Additional strings to recognize as NA/NaN |
| `skiprows`           | Yes                      | No                       | No                      | Yes                  | Rows to skip at start                     |
| `nrows`              | Yes                      | No                       | No                      | Yes                  | Number of rows to read                    |
| `chunksize`          | Yes                      | No                       | Yes                     | No                   | Read in chunks (generator)                |
| `encoding`           | Yes                      | Yes                      | No                      | Yes                  | File encoding                             |
| `compression`        | Yes                      | Yes                      | No                      | Yes                  | Compression format (gzip, bz2, zip, xz)   |
| `sql`                | N/A                      | N/A                      | Yes                     | N/A                  | SQL query or table name                   |
| `con`                | N/A                      | N/A                      | Yes                     | N/A                  | Database connection / engine              |
| `sheet_name`         | N/A                      | N/A                      | N/A                     | Yes (str, int, list) | Sheet(s) to read (default 0)              |
| `engine`             | N/A                      | N/A                      | N/A                     | Yes                  | Excel engine (`openpyxl`, `xlrd`, etc.)   |

---

### Notes:

* For **DB** saving/loading, pandas uses SQLAlchemy engine or DBAPI connections.
* Some arguments only exist on one format (e.g., `sheet_name` is Excel-only).
* Many arguments overlap in meaning but are only relevant for certain formats.

---


```
# Excel files
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')
df = pd.read_excel('file.xlsx', sheet_name=None)  # All sheets

# JSON
df = pd.read_json('file.json')
df = pd.read_json('file.json', orient='records')

# SQL databases
import sqlite3
conn = sqlite3.connect('database.db')
df = pd.read_sql_query('SELECT * FROM table_name', conn)
```

