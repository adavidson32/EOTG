import os, glob, time, math
import sqlite3
from ds18b20 import DS18B20
from mpu6050 import mpu6050

def var_setup():
    conn = sqlite3.connect('eotg.db')
    c = conn.cursor()
    button_var_list = []
    neopixel_var_list = []
    wifi_var_list = []
    for row in c.execute('SELECT * FROM setup_variables WHERE category=?', ('button',)):
        var_tuple = (row[1], row[2])
        button_var_list.append(var_tuple)
    for row in c.execute('SELECT * FROM setup_variables WHERE category=?', ('neopixel',)):
        neopixel_tuple = (row[1], row[2])
        neopixel_var_list.append(neopixel_tuple)
    for row in c.execute('SELECT * FROM wifi_variables'):
        priority = ('priority', row[0])
        ssid = ('ssid', row[1])
        password = ('password', row[2])
        wifi_var_list.append(priority)
        wifi_var_list.append(ssid)
        wifi_var_list.append(password)
    button_var = dict(button_var_list)
    neopixel_var = dict(neopixel_var_list)
    wifi_var = dict(wifi_var_list)
    #connect to sqlite database (ex. eotg.db)
    #retrieve all values from setting_variables table in eotg.db
    #return tuple of all variable dictionairies ex: ({'t_hold': 1.5, ...}, {'neopixel_pin': 18, ...})
    output_tuple = (button_var, neopixel_var, wifi_var)
    return output_tuple

def hw_setup():
    ds = DS18B20()
    mpu = mpu6050(0x76)
    num_ds = ds.device_count()
    return ds, mpu, num_ds
