import RPi.GPIO as io
from time import sleep, localtime, strftime, time

class relays:
    def __init__(self, pump_pin, heat_pin):
        io.setmode(GPIO.BCM)
        io.setup(pump_pin, GPIO.OUT, initial=GPIO.HIGH)
        io.setup(heat_pin, GPIO.OUT, initial=GPIO.HIGH)

    def pump_on(self):
        io.output(pump_pin, GPIO.LOW)
    def pump_off(self):
        io.output(pump_pin, GPIO.HIGH)
    def heat_on(self):
        io.output(heat_pin, GPIO.LOW)
    def heat_off(self):
        io.output(heat_pin, GPIO.HIGH)
    def pump_on_for(self, sec_on):
        now = time()
    def heat_on_for(self, sec_on):
        now = time()
