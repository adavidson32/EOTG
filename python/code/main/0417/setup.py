import os, glob, time, math
import sqlite3
#from ds18b20 import DS18B20
#from mpu6050 import mpu6050

def var_setup():
    var_list = (('button',), ('neopixel',), ('wifi',), ('ds18b20',), ('bmp280',), ('mpu6050',))
    conn = sqlite3.connect('eotg.db')
    c = conn.cursor()
    button_var_list = neopixel_var_list = wifi_var_list = []
    for row in c.execute('SELECT * FROM setup_variables WHERE category=?', ('button',)):
        var_tuple = (row[1], row[2])
        button_var_list.append(var_tuple)
    for row in c.execute('SELECT * FROM setup_variables WHERE category=?', ('neopixel',)):
        neopixel_tuple = (row[1], row[2])
        neopixel_var_list.append(neopixel_tuple)
    for row in c.execute('SELECT * FROM wifi_variables'):
        var_list = (('priority', row[0]), ('ssid', row[1]), ('password', row[2]))
        wifi_var_list.append(var_list)
    print(button_var_list)
    print(neopixel_var_list)
    print(wifi_var_list)
    button_var = dict(button_var_list)
    neopixel_var = dict(neopixel_var_list)
    wifi_var = dict(wifi_var_list)
    #connect to sqlite database (ex. eotg.db)
    #retrieve all values from setting_variables table in eotg.db
    #return tuple of all variable dictionairies ex: ({'t_hold': 1.5, ...}, {'neopixel_pin': 18, ...})
    output_tuple = (button_var, neopixel_var, wifi_var)
    return output_tuple

#def hw_setup(hw_addresses):
    #import: RPi-GPIO, bmp280, ds18b20, mpu6050, 16x2 lcd libraries
    #setup relay GPIO in correct modes
    #setup BMP280, MPU6050 I2C devices (based on saved I2C addresses from variable_setup)
    #setup DS18B20 sensors (identify all, save some variables?)
    #return num_ds18b20,

button_var, neopixel_var, wifi_var = var_setup()
print('Button Variables: ')
print(button_var)
print('Neopixel Variables: ')
print(neopixel_var)
print('Wifi Variables: ')
print(wifi_var)
