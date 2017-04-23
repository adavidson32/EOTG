import RPi.GPIO as io
from time import sleep, localtime, strftime, time

class relays:
    def __init__(self, pump_settings):
        io.setmode(io.BCM)
        io.setup(pin, io.OUT, initial=io.HIGH)
        self.pin = pump_settings['pin']
        self.pump_freq = pump_settings['pwm_freq']
        self.pump_dutycyc = pump_settings['pwm_dutycyc']

    def on(self):
        io.output(self.pin, io.LOW)

    def off(self):
        io.output(self.pin, io.HIGH)

    def pwm_start(self):
        pwm_var = io.PWM(self.pin, self.pump_freq)
        self.pwm = pwm_var
        pwm_var.start(self.pwm_dutycyc)

    def pwm_stop(self):
        pwm_var = self.pwm
        pwm_var.stop()
