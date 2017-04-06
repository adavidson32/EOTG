import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

while TRUE:
  GPIO.output(24, FALSE)
  GPIO.output(25, TRUE)
  time.sleep(2)
  GPIO.output(24, TRUE)
  GPIO.output(25, FALSE)
  time.sleep(2)
