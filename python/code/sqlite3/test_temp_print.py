import sqlite3
import time, math
from ds18b20 import DS18B20

x = DS18B20()

upload_time = time.time()

while True:
    
    while (time.time() < (upload_time + 5)):
        time.sleep(.1)
        
    upload_time = time.time()
    dt = time.strftime('%x')
    tim = time.strftime('%X')
    
    conn = sqlite3.connect('temp.db')
    c = conn.cursor()
    value_tuple = (1, 0.1*(math.floor(10*x.tempC(0))), dt, tim)
    c.execute('INSERT INTO temp_values VALUES (?,?,?,?)', value_tuple)
    conn.commit()
    conn.close()
    
    print("Just added T={0:.1f}*C to temp.db".format(x.tempC(0)))
