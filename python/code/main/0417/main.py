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
    ds, mpu, num_ds = ret_sensor
    print('')
    print('Sensor Return')
    print('Number DS18B20: {}'.format(num_ds))
    print('ds1 temp: {:.1f}'.format(ds.getC(0)))
    print("x: {0['x']}, x: {0['y']}, x: {0['z']}".format(mpu.get_accel_data()))

read_settings()
print('done with simple main.py....')
