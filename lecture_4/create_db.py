import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

with open('queries.sql', 'r', encoding='utf-8', errors='ignore') as f:
    sql_script = f.read()
cursor.executescript(sql_script)
conn.commit()
conn.close()

print("school.db created successfully")