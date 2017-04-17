import os, glob, time, math
import sqlite3, lcddriver
from ds18b20 import DS18B20
from mpu6050 import mpu6050

def var_setup():
    var_list = (('button',), ('neopixel',), ('wifi',), ('ds18b20',), ('bmp280',), ('mpu6050',))
    conn = sqlite3.connect('eotg.db')
    c = conn.cursor()
    for a in var_list:
        for row in c.execute('SELECT * FROM setup_variables WHERE category=?', var_list[a]):


    #connect to sqlite database (ex. eotg.db)
    #retrieve all values from setting_variables table in eotg.db
    #return tuple of all variable dictionairies ex: ({'t_hold': 1.5, ...}, {'neopixel_pin': 18, ...})
    output_tuple = (button_var, neopixel_var, wifi_var, ds18b20_var, mpu6050_var, bmp280_var, relay_var)
    return output_tuple

def hw_setup(hw_addresses):
    #import: RPi-GPIO, bmp280, ds18b20, mpu6050, 16x2 lcd libraries
    #setup relay GPIO in correct modes
    #setup BMP280, MPU6050 I2C devices (based on saved I2C addresses from variable_setup)
    #setup DS18B20 sensors (identify all, save some variables?)
    return num_ds18b20,
