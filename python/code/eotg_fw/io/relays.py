import RPi.GPIO as io
from time import sleep, localtime, strftime, time

class relays:
    def __init__(self, pin):
        io.setmode(io.BCM)
        io.setup(pin, io.OUT, initial=io.HIGH)
        self.off(self,pin)

    def on(self, pin):
        io.output(pin, io.LOW)
    def off(self, pin):
        io.output(pin, io.HIGH)
