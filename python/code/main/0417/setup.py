import os, glob, time, math
import sqlite3
from ds18b20 import DS18B20
from mpu6050 import mpu6050

def var_setup():
    conn = sqlite3.connect('eotg.db')
    c = conn.cursor()
    device_settings = []
    button_settings = []
    button_events = []
    neopixel_settings = []
    update_settings = []
    ds18b20_settings = []
    mpu6050_settings = []
    bmp280_settings = []
    wifi_list = []
    for row in c.execute('SELECT * FROM device_settings'):
        a_t = (row[1], row[2])
        device_settings.append(a_t)
    for row in c.execute('SELECT * FROM button_settings'):
        b_t = (row[1], row[2])
        button_settings.append(b_t)
    for row in c.execute('SELECT * FROM button_events'):
        c_t = (row[1], row[2])
        button_events.append(c_t)
    for row in c.execute('SELECT * FROM wifi_settings'):
        priority = ('priority', row[0])
        ssid = ('ssid', row[1])
        password = ('password', row[2])
        wifi_settings.append((priority, ssid, password))
        #wifi_settings.append(ssid)
        #wifi_settings.append(password)
    button_settings = dict(button_settings)
    button_events = dict(button_events)
    device_settings = dict(device_settings)
    wifi_settings = dict(wifi_settings)
    #connect to sqlite database (ex. eotg.db)
    #retrieve all values from setting_variables table in eotg.db
    #return tuple of all variable dictionairies ex: ({'t_hold': 1.5, ...}, {'neopixel_pin': 18, ...})
    output_tuple = (device_settings, button_settings, button_events, wifi_settings)
    return output_tuple

def sensor_setup():
    ds = DS18B20()
    mpu = mpu6050(0x76)
    num_ds = ds.device_count()
    return ds, mpu, num_ds
