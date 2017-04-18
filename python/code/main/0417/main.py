import time, os, sys
from setup import var_setup, sensor_setup

def read_settings():
    ret_var = var_setup()
    device_settings, button_settings, button_events, wifi_settings = ret_var
    print('')
    print('Variable Setup Return: ')
    print(device_settings)
    print(button_settings)
    print(button_events)
    print(wifi_settings)

    ret_sensor = sensor_setup()
    print('')
    print('Sensor Return')
    print(ds.getC(0))
    print(mpu.get_accel_data())

read_settings()
print('done with simple main.py....')
