include time
include sys
include RPi.GPIO as GPIO

button_pin = 21
relay_pin1 = 6
relay_pin2 = 5
bmp280_addr = 0x76
mpu6050_addr = 0x68
#uncomment below and change address once nano i2c slave is setup
#LCD_16x2_addr = 0x00
#nano_addr = 0x00
neopixel_pin = 18    #pin must support special clock functions required for neopixels. 
neopixel_ring_size = 12     #change to 24 when larger ring arrives and is used

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin1, GPIO.OUT)
GPIO.setup(relay_pin2, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def buttonread(read_time):
  if 
def initial_setup():
  print("Starting program...")
  #connect to server
  #request updates made since last update request...
  
def main_loop():
  button_result 
  
    
