import RPi.GPIO as GPIO
import sys
import time 

GPIO.setmode(GPIO.BCM)
if len(sys.argv) == 4:
  GPIO_pin = int(sys.argv[1])
  read_mode = sys.argv[2]
  up_down = sys.argv[3]
else:
  print("len(argv)!=4... Please manually enter GPIO_pin, read_mode, and pullup mode:
  GPIO_pin = int(input("Which pin to control? : "))
  read_mode = input("Read mode to use? (once, continuous, time): ")  
  up_down = input("Pull up mode to use? (Enter UP or DOWN) : ")  

GPIO.setwarnings(False)
if up_down == "UP":
  GPIO.setup(GPIO_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
elif up_down == "DOWN":
  GPIO.setup(GPIO_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
if (read_mode == "once"):
  if GPIO.input(GPIO_pin):
    print("GPIO#{0} is currently HIGH...")
  else:
    print("GPIO#{0} is currently LOW...")

elif (read_mode == "continuous"):
  print_freq = input("How many seconds between readings? (0:1000) : ")
  while 1:
    if GPIO.input(GPIO_pin):
      print("GPIO#{0} is currently HIGH...")
    else:
      print("GPIO#{0} is currently LOW...")
    delay(print_freq)

elif (read_mode == "time"):
  run_time = input("How many seconds should script run? : ")
  print_freq = input("How many seconds between readings? (0:1000) : ")
  start_time = int(time.time())
  finish_time = start_time + run_time
  while (int(time.time()) < finish_time):
    if GPIO.input(GPIO_pin):
      print("GPIO#{0} is currently HIGH...")
    else:
      print("GPIO#{0} is currently LOW...")
    delay(print_freq)
