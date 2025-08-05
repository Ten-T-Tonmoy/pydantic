


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