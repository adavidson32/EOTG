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

all_settings = variable_setup()
for x,y in all_settings:
    print('Key: {}, Value: {}'.format(x,y))

sensors = sensor_setup(all_settings)
ds, mpu, pump, heater = sensors

while True:
    if current_state == 'background':
        background_return = background(all_settings)
        if background_return == 'waiting':
            current_state = 'waiting'
        elif background_retun == 'brewing':
            current_state = 'brewing'
    if current_state == 'waiting':
        waiting_return = waiting(all_settings)
        if waiting_return == 'background':
            current_state = 'background'
        elif waiting_return == 'brewing':
            current_state = 'brewing'
    if current_state == 'brewing':
        brewing_retun = brewing()
        if brewing_retun == 'waiting':
            current_state = 'waiting'
        elif brewing_return == 'background':
            current_state = 'background'
