import time, os, sys
from setup import var_setup, sensor_setup

def read_settings():
    ret_var = var_setup()
    print('')
    print('Variable Setup Return: ')
    print(return_var)

    ret_sensor = sensor_setup()
    print('')
    print('Sensor Return')
    print(sensor_hw)

read_settings()
