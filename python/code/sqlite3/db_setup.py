import sqlite3, time

conn = sqlite3.connect('temp.db')
c = conn.cursor()
c.execute('''CREATE TABLE temp_values
             (sensor_id INTEGER, temp_c REAL, date_str TEXT, time_str TEXT)''')
c.exectute("INSERT INTO temp_values VALUES (0, 1.00, time.strftime("%x"), time.strftime("%X"))")
# insert initial "fake" values for some senser #0: Temp = 1.00*C, time = now....
conn.commit()
conn.close()

