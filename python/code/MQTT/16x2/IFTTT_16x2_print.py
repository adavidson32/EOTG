import os, glob, time, sys, lcddriver
from Adafruit_IO import MQTTClient

ADAFRUIT_IO_KEY      = '7c61b801bf874426902ba2f78d5c2102'
ADAFRUIT_IO_USERNAME = 'eotg'
SUB_FEED = 'ifttt'
PUB_FEED = 'coffee_temp'

sample_rate = 30.0

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
device_folder = glob.glob('/sys/bus/w1/devices/28*')
device_file = device_folder[0] + '/w1_slave'
def read_temp_raw():
    f_1 = open(device_file, 'r')
    lines_1 = f_1.readlines()
    f_1.close()
    return lines_1
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    temp = float(lines[1][equals_pos+2:])/1000
    return temp

def connected(client):
    print("Connected to Adafruit IO!  Listening for {0} changes".format(SUB_FEED))
    lcd.lcd_display_string("Conn:adafruit.io", 1)
    lcd.lcd_display_string("Receiving: IFTTT", 2)
    client.subscribe(SUB_FEED)
def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)
def message(client, feed_id, payload):
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    if len(payload > 16):
        payload = payload[0:16]
    lcd.lcd_display_string("  MSG on IFTTT  ", 1)
    lcd.lcd_display_string("{}".format(payload), 2)

lcd = lcddriver.lcd()

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.connect()

last = 0
print('Publishing a new message every 30 seconds (press Ctrl-C to quit)...')
while True:
   client.loop()
   if (time.time() - last) >= sample_rate:
       coffee_temp = read_temp()
       print('Publishing {0:.2f} to cofee_temp feed.'.format(coffee_temp))
       client.publish(PUB_FEED, coffee_temp)
       last = time.time()
