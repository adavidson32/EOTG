import varread, os, glob, sys, time, datetime, sqlite3
from ds18b20 import DS18B20

def tarray_calc()
    x = DS18B20()
    count=x.device_count()
    i = 0
    temp_str = ''
    temp_list = []
    while i < count:
        temp_i = x.tempC(i)
        temp_list.append(temp_i)
        i += 1
        temp_str += 'T{0}: {1:.1f}*C'.format(i, temp_i)
        if (i+1) < count:
            temp_str += ', '
    return temp_list, temp_str

def save_temps(temp_list):
    date_str = time.strftime('%x')
    time_str = time.strftime('%X')
    len_temp = len(temp_list)
    upload_time = time.time()
    conn = sqlite3.connect('temp.db')
    c = conn.cursor()
    for i in range(len_temp):
        c.execute("INSERT INTO temp_values VALUES (i, temp_list[i], date_str, time_str)")
    conn.commit()
    conn.close()
    return upload_time
