import time
import RPi.GPIO as GPIO

button_pin = 21
sampling_delay = 0.001
debounce_time = .1
hold_time = 1.5
single_max_time = 1
hold_timeout = 1.7

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

b1_time = 0.0001
while b1_time <= debounce_time:
  now = time.time()
  while not(GPIO.input(button_pin)):
    time.sleep(sampling_delay)
  now = time.time()
  while ((GPIO.input(button_pin)) and ((time.time() - now) <= hold_timeout)):
    time.sleep(sampling_delay)
  b1_time = time.time() - now
print("Button 1 Held for : ", b1_time, " seconds")
if (b1_time >= hold_time):
  print("HOLD Detected")
  button_func = "HOLD"
elif ((b1_time <= single_max_time) and (b1_time >= debounce_time)):
  now = time.time()
  while (not(GPIO.input(button_pin)) and ((time.time() - now) <= hold_timeout)):
    time.sleep(sampling_delay)
  time_between = time.time() - now
  print("Time between presses : ", time_between, " seconds")
  if time_between <= single_max_time:
    now = time.time()
    while ((GPIO.input(button_pin)) and ((time.time() - now) <= hold_timeout)):
      time.sleep(sampling_delay)
    b2_time = time.time() - now
    print("Button 2 Held for : ", b2_time, " seconds")
    if ((b2_time >= debounce_time) and (b2_time <= single_max_time)):
      print("2x Press Detected")
      button_func = "2x Press"
  else:
    print("1x Press Detected")
    button_func = "1x Press"
