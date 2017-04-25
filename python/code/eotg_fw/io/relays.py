import RPi.GPIO as io

class relays:
    def __init__(self, dev_settings):
        io.setmode(io.BCM)
        io.setwarnings(False)
        self.pin = dev_settings['pin']
        self.pwm_freq = dev_settings['pwm_freq']
        self.pwm_dutycyc = dev_settings['pwm_dutycyc']
        print('pin: {}, pwm_frequency: {}, pwm_duty_cycle: {}'.format(self.pin, self.pwm_freq, self.pwm_dutycyc))
        io.setup(self.pin, io.OUT, initial=io.HIGH)
        self.pwm = io.PWM(self.pin, self.pwm_freq)

    def on(self):
        io.output(self.pin, io.LOW)

    def off(self):
        io.output(self.pin, io.HIGH)

    def pwm_start(self):
        self.pwm.start(self.pwm_dutycyc)

    def pwm_stop(self):
        self.pwm.stop()
        
    def cleanup(self):
        io.cleanup()
