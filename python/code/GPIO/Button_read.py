import time
import RPi.GPIO as GPIO

button_pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while not(GPIO.input(button_pin)):
  time.sleep(.001)
now = time.time()
while (GPIO.input(button_pin)):
  time.sleep(.001)
b1_time = time.time() - now
print(b1_time)
if ((b1_time <= .2) and (b1_time >= .01)):
  print("button press not long enough to register")
  button_func = "Nothing"
elif (b1_time >= 2):
  print("HOLD Detected")
  button_func = "HOLD"
elif ((b1_time <= 1) and (b1_time >= .2)):
  now = time.time()
  while not(GPIO.input(button_pin)):
    time.sleep(.001)
  time_between = time.time() - now
  if time_between <= 1:
    now = time.time()
    while (GPIO.input(button_pin):
      time.sleep(0.01)
    b2_time = time.time() - now
    if ((b2_time >= 0.2) and (b2_time <= 1)):
      print("2x Press Detected")
      button_func = "2x Press"
  else:
    print("1x Press Detected")
    button_func = "1x Press"
