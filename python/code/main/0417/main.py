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
    for i in range(num_ds):
        print('ds{0} temp: {1:.1f}'.format(i, ds.tempC(i)))
    mpu_data = mpu.get_all_data()
    print("ax: {0['x']}, ay: {0['y']}, az: {0['z']}".format(mpu_data[0]))
    print("gx: {0[1]['x']}, gy: {0[1]['y']}, gz: {0[1]['z']}".format(mpu_data))
    print('mpu temp: {0[2]:.1f}'.format(mpu_data))
read_settings()
print('done with simple main.py....')
