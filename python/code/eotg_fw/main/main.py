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


ds, mpu, pump, heater = sensor_setup(all_settings)

while True:
    if current_state == background:
        background_return = background(all_settings)
        if background_return
    if background_return == 'waiting':
        waiting_return = waiting(all_settings)
    elif background_return == 'off':
        print('shutting down...')
    if waiting_return == 'background':
        continue
    elif waiting_return == 'brewing':
        brewing_return = brewing(all_settings)



print(ds.temp_all)
print(mpu.get_accel_data())
pump.on()
print('pump on')
time.sleep(2)
pump.off()
heater.on()
print('pump off, heater on')
time.sleep(2)
heater.off()
print('heater off')
