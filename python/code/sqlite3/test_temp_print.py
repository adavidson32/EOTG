import sqlite3, time, os, glob, sys
import ds18b20 as DS18B20

x = DS18B20()

upload_time = time.time()

While True:
    while (time.time() < (upload_time + 5)):
        time.sleep(.1)
    upload_time = time.time()
    date_str = time.strftime('%x')
    time_str = time.strftime('%X')
    conn = sqlite3.connect('temp.db')
    c = conn.cursor()
    c.execute("INSERT INTO temp_values VALUES (1, x.tempC(0), date_str, time_str)")
    conn.commit()
    conn.close()
