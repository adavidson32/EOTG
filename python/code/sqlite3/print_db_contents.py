import sqlite3

conn = sqlite3.connect('temp.db')

c = conn.cursor()

for row in c.execute('SELECT * FROM temp_values'):
    print(row)
