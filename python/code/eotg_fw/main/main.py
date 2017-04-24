import time, os, sys
sys.path.append('/home/pi/git/EOTG/python/code/eotg_fw/setup')
sys.path.append('/home/pi/git/EOTG/python/code/eotg_fw/sensors')
sys.path.append('/home/pi/git/EOTG/python/code/eotg_fw/io')
sys.path.append('/home/pi/git/EOTG/python/code/eotg_fw/states')
sys.path.append('/home/pi/git/EOTG/python/code/eotg_fw/web')
from setup import variable_setup, sensor_setup
from background import background
from waiting import waiting
from brewing import brewing
from prebrew_check import pb_check
from state_alert import sqlite_update

all_settings = variable_setup()

sensors = sensor_setup(all_settings)
ds, mpu, pump, heater = sensors
pbc = pb_check(all_settings['ac_batt_settings'])
current_state = 'background'

while True:
    if current_state == 'background':
        sqlite_update('device_info', 'current_state', 'background')
        background_return = background(all_settings)
        time.sleep(0.5)
        if background_return == 'waiting':
            current_state = 'waiting'
        elif background_return == 'brewing':
            pb_test = pbc.prebrew_check(mpu)
            if pb_test == 'good':
                current_state = 'brewing'
            else:
                current_state = 'background'
    elif current_state == 'waiting':
        sqlite_update('device_info', 'current_state', 'waiting')
        waiting_return = waiting(all_settings)
        time.sleep(0.5)
        pump.off()
        print('waiting return = {}'.format(waiting_return))
        if waiting_return == 'background':
            current_state = 'background'
        elif waiting_return == 'brewing':
            pb_test = pbc.prebrew_check(mpu)
            if pb_test == 'good':
                current_state = 'brewing'
            else:
                current_state = 'waiting'
        elif waiting_return == 'waiting':
            current_state = 'waiting'
    elif current_state == 'brewing':
        sqlite_update('device_info', 'current_state', 'brewing')
        brewing_return = brewing(all_settings, sensors)
        time.sleep(0.5)
        if brewing_return == 'waiting':
            current_state = 'waiting'
            pump.off()
        elif brewing_return == 'background':
            current_state = 'background'
            pump.off()
