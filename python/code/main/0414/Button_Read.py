import time
import RPi.GPIO as GPIO

def Button_Read(settings_dict):
	
	button_pin = settings_dict['button_pin']
	time_single_min = settings_dict['time_single_min']
	time_single_max = settings_dict['time_single_max']
	time_hold_min = settings_dict['time_hold_min']
	time_hold_max = settings_dict['time_hold_max']
	
	GPIO.setmode(
	
	
	
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