import sqlite3

ex_var = {'Sensor ID': 1, 'Sample Rate': 5, 'Resolution': 0.125}
sensor, srate, res = ex_var['Sensor ID'], ex_var['Sample Rate'], ex_var['Resolution']

conn = sqlite3.connect('temp.db')
conn.execute('''CREATE TABLE temp_settings
                (sensor_id INTEGER, samp_rate REAL, resolution REAL, time INTEGER)''')
conn.execute("insert into temp_settings * values (?, ?, ?, ?)", (sensor, srate, res, time.time()))
conn.commit()

conn.execute('''CREATE TABLE temp_values
                (sensor_id INTEGER, temp_c REAL, date_str TEXT, time_str TEXT)''')
conn.commit()
conn.close()

print("Settings successfully updated to: "
print("Sensor #{0}: Samp_Rate({1}sec.), Resolution({2}*C".format(sensor, srate, res))
