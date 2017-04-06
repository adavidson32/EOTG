import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(25, GPIO.OUT, initial=GPIO.HIGH)

while TRUE:
  GPIO.output(24, LOW)
  GPIO.output(25, HIGH)
  time.sleep(2)
  GPIO.output(24, HIGH)
  GPIO.output(25, LOW)
  time.sleep(2)
