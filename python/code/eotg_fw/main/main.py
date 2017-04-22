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
from check_orientation import check_orientation

all_settings = variable_setup()

sensors = sensor_setup(all_settings)
ds, mpu, pump, heater = sensors
current_state = 'background'

while True:
    if current_state == 'background':
        background_return = background(all_settings)
        time.sleep(1)
        if background_return == 'waiting':
            current_state = 'waiting'
        elif background_return == 'brewing':
            mpu_test = check_orientation(mpu)
            if mpu_test == 'level':
                current_state = 'brewing'
            else:
                current_state = 'background'
    elif current_state == 'waiting':
        waiting_return = waiting(all_settings)
        time.sleep(1)
        if waiting_return == 'background':
            current_state = 'background'
        elif waiting_return == 'brewing':
            mpu_test = check_orientation(mpu)
            if mpu_test == 'level':
                current_state = 'brewing'
            else:
                current_state = 'waiting'
    elif current_state == 'brewing':
        brewing_return = brewing(all_settings, sensors)
        time.sleep(1)
        if brewing_return == 'waiting':
            current_state = 'waiting'
        elif brewing_return == 'background':
            current_state = 'background'
