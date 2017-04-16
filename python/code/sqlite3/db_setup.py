import sqlite3

conn = sqlite3.connect('temp.db')
c = conn.cursor()
c.execute('''CREATE TABLE temp_values
             (sensor_id INTEGER, temp_c REAL, date_str TEXT, time_str TEXT)''')
conn.commit()
conn.close()

print("Settings successfully updated to: "
print("Sensor #{0}: Samp_Rate({1}sec.), Resolution({2}*C".format(sensor, srate, res))
