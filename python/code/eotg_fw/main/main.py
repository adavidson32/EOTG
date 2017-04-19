import time, os, sys
from setup import variable_setup, sensor_setup

all_settings = variable_setup()

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
