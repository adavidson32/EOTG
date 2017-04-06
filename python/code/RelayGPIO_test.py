import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(24, GPIO.OUT, initial=GPIO.HIGH)
#NOTE: GPIO.HIGH == Relay-OFF   GPIO.LOW == Relay-OFF
time.sleep(3)

while 1:
  GPIO.output(23, GPIO.HIGH)
  GPIO.output(24, GPIO.LOW)
  time.sleep(1)
  GPIO.output(23, GPIO.LOW)
  GPIO.output(24, GPIO.HIGH)
  time.sleep(1)
  GPIO.output(23, GPIO.LOW)
  GPIO.output(24, GPIO.LOW)
  time.sleep(1)
  GPIO.output(23, GPIO.HIGH)
  GPIO.output(24, GPIO.HIGH)
  time.sleep(1)
