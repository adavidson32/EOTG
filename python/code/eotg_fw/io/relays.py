import RPi.GPIO as io
from time import sleep, localtime, strftime, time

class relays:
    def __init__(self, pin):
        io.setmode(GPIO.BCM)
        io.setup(pin, io.OUT, initial=io.HIGH)

    def on(self):
        io.output(pin, io.LOW)
    def off(self):
        io.output(pin, io.HIGH)
