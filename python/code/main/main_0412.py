import time
import sys
import math
import RPi.GPIO as GPIO
from mpu6050 import mpu6050

button_pin = 21
sampling_delay = 0.001
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

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin1, GPIO.OUT)
GPIO.setup(relay_pin2, GPIO.OUT)
GPIO.output(relay_pin1, GPIO.HIGH)
GPIO.output(relay_pin2, GPIO.HIGH)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def run_brew():
  print("Brew Starting Now.....")
  time_start = time.time()
  GPIO.output(relay_pin1, GPIO.LOW)
  GPIO.output(relay_pin2, GPIO.LOW)
  while (time.time() < (time_start + brew_time)):
    time.sleep(.1)
  GPIO.output(relay_pin1, GPIO.HIGH)
  GPIO.output(relay_pin2, GPIO.HIGH)
  return "brew_success"
    

def check_orientation():
  accel_data = mpu6050.get_accel_data()
  ax = float("{0:.3f}".format(accel_data['x']))
  ay = float("{0:.3f}".format(accel_data['y']))
  az = float("{0:.3f}".format(accel_data['z']))
  xz_fraction = math.fabs(ax / az)
  yz_fraction = math.fabs(ay / az)
  xz_angle = math.atan(xz_fraction)
  yz_angle = math.atan(yz_fraction)
  xz_angle = math.degrees(xz_angle)
  yz_angle = math.degrees(yz_angle)
  print("xz-angle: {0:.1f},  yz-angle: {1:.1f}".format(xz_angle, yz_angle))
  if ((xz_angle <= 5) and (yz_angle <= 5)):
    return "level"
  elif ((xz_angle > 5) or (yz_angle  > 5)):
    return "not-level" 
 
def prebrew_check():
  check_level = check_orientation()
  if (ac == 'disconnected'):
    return 'ac_disconnected'
  elif (water_level == 'low'):
    return 'water_low'
  elif (check_level == 'not-level'):
    return 'not-level'
  else:
    return 'pass'

def buttonread():
  b1_time = 0.0001
  button_func = ''
  while b1_time <= debounce_time:
    now = time.time()
    while not(GPIO.input(button_pin)):
      time.sleep(sampling_delay)
    now = time.time()
    while ((GPIO.input(button_pin)) and ((time.time() - now) <= hold_timeout)):
      time.sleep(sampling_delay)
    b1_time = time.time() - now
  if (b1_time >= hold_time):
    button_func = "HOLD"
  elif ((b1_time <= single_max_time) and (b1_time >= debounce_time)):
    now = time.time()
    while (not(GPIO.input(button_pin)) and ((time.time() - now) <= hold_timeout)):
      time.sleep(sampling_delay)
    time_between = time.time() - now
    if time_between <= single_max_time:
      now = time.time()
      while ((GPIO.input(button_pin)) and ((time.time() - now) <= hold_timeout)):
        time.sleep(sampling_delay)
      b2_time = time.time() - now
      if ((b2_time >= debounce_time) and (b2_time <= single_max_time)):
        button_func = "2x Press"
    else:
      button_func = "1x Press"
  return button_func

def advance_profile(current_profile)
  new_profile = (current_profile+1)%(number_profiles+1)
  print("Profile Changed to #{}....".format(new_profile))
  return new_profile

def states_waiting():
  print("Device in waiting state")
  but_func = buttonread()
  while (not(but_func == '2x Press') and not(but_func == '1x Press') and not(but_func == 'HOLD')):
    but_func = buttonread()
  if but_func == 'HOLD':
    print("Device turned off. Hold Button to turn back on....")
    states_background()
  elif but_func == "1x Press":
    profile_num = advance_profile(profile_num)
  elif but_func == "2x Press":
    test_results = prebrew_test()
    if (test_results == 'pass')
      print("Brew Started"):
      result = states_brewing()
      if result == "brew_success":
        print("Brew finished successfully and returned to waiting state")
      else:
        print("Brew finished with error, returned to waiting state")
    else:
      print("Error running brew. Check water level, device level, or AC connection...")
  states_waiting()
         
def states_background():
  While True:
    print("Device in Background State")
    but_func = buttonread()
    while not(but_func == 'HOLD'):
      but_func = buttonread()
    if (but_func == 'HOLD'):
      states_waiting()
  
  #connect to server
  #request updates made since last update request...
  
states_background()
  
    
