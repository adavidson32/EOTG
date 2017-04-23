import RPi.GPIO as io
from time import sleep, localtime, strftime, time

class relays:
    def __init__(self, pin):
        io.setmode(io.BCM)
        io.setup(pin, io.OUT, initial=io.HIGH)
        self.pin = pin

    def on(self):
        io.output(self.pin, io.LOW)
    def off(self):
        io.output(self.pin, io.HIGH)
