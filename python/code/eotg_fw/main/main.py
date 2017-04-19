import time, os, sys
sys.path.append('/home/pi/git/EOTG/python/code/eotg_fw/setup')
sys.path.append('/home/pi/git/EOTG/python/code/eotg_fw/sensors')
sys.path.append('/home/pi/git/EOTG/python/code/eotg_fw/io')
sys.path.append('/home/pi/git/EOTG/python/code/eotg_fw/states')
from setup import variable_setup, sensor_setup

all_settings = variable_setup()
for x,y in all_settings:
    print('Key: {}, Value: {}'.format(x,y))


ds, mpu, pump, heater = sensor_setup(all_settings)

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
