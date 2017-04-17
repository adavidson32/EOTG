import time, os, sys
from setup import var_setup, hw_setup

return_tuple = var_setup()

def var_setup():
    #import: sqlite3,
    #connect to sqlite database (ex. eotg.db)
    #retrieve all values from setting_variables table in eotg.db
    #save variables into dict structures with variable name + value
    #return dictionary variabls for each variable category (ex. button_var, ds18b20_var, wifi_var, etc.)
    return all_var

def hw_setup(hw_addresses):
    #import: RPi-GPIO, bmp280, ds18b20, mpu6050, 16x2 lcd libraries
    #setup relay GPIO in correct modes
    #setup BMP280, MPU6050 I2C devices (based on saved I2C addresses from variable_setup)
    #setup DS18B20 sensors (identify all, save some variables?)
    return num_ds18b20,
