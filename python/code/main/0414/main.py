import time, sys, math
import RPi.GPIO as GPIO
from mpu6050 import mpu6050
import os, glob
import main_background, main_waiting, 

settings_all = main_settings_read()


button_pin = settings_all[1]['pin']
debounce_time = .1
hold_time = 1.5
single_max_time = 1
hold_timeout = 1.7

number_profiles = 5
profile_num = 1
brew_time = 30
water_level = "full"
battery_level = "full"
ac = "connected"
relay_pin1 = 6
relay_pin2 = 5
bmp280_addr = 0x76
mpu6050_addr = 0x68
mpu6050 = mpu6050(mpu6050_addr)
#uncomment below and change address once nano i2c slave is setup
#LCD_16x2_addr = 0x00
#nano_addr = 0x00
neopixel_pin = 18    #pin must support special clock functions required for neopixels. 
neopixel_ring_size = 12     #change to 24 when larger ring arrives and is used
device_state = 'background'

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin1, GPIO.OUT)
GPIO.setup(relay_pin2, GPIO.OUT)
GPIO.output(relay_pin1, GPIO.HIGH)
GPIO.output(relay_pin2, GPIO.HIGH)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  
states_background()
