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
    print('ax: -{0:.2f}, ay: -{1:.2f}, az: -{2:.2f}'.format(mpu_data[0]['x'], mpu_data[0]['y'], mpu_data[0]['z']))
    print('gx: -{0:.2f}, gy: -{1:.2f}, gz: -{2:.2f}'.format(mpu_data[1]['x'], mpu_data[1]['y'], mpu_data[1]['z']))
    print('mpu temp: {0:.1f}'.format(mpu_data[2]))
read_settings()
print('done with simple main.py....')
