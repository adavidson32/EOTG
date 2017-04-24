import RPi.GPIO as io
from time import sleep, localtime, strftime, time

class relays:
    def __init__(self, dev_settings):
        io.setmode(io.BCM)
        self.pin = dev_settings['pin']
        self.pwm_freq = dev_settings['pwm_freq']
        self.pwm_dutycyc = dev_settings['pwm_dutycyc']
        io.setup(self.pin, io.OUT)

    def on(self):
        io.output(self.pin, io.LOW)

    def off(self):
        io.output(self.pin, io.HIGH)

    def pwm_start(self):
        pwm_var = io.PWM(self.pin, self.pwm_freq)
        self.pwm = pwm_var
        pwm_var.start(self.pwm_dutycyc)

    def pwm_stop(self):
        pwm_var = self.pwm
        pwm_var.stop()
