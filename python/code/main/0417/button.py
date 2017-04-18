import RPi.GPIO as GPIO
import time, sqlite3

def settings_read():
    conn = sqlite3.connect('eotg.db')
    c = conn.cursor()
    button_settings_list = []
    for row in c.execute('SELECT * FROM button_settings'):
        button_tuple = (row[0], row[1])
        button_settings_list.append(button_tuple)
    return dict(button_settings_list)

def button_interupt_handler(button_pin):
    print('button_press detected, printing button setting info...')
    bsettings = settings_read()
    button_pin = bsettings['pin']
    print('button settings dictionairy: ')
    print(bsettings)
    print('button pin value:')
    print(button_pin)
    print("type of 'button_pin': ")
    print(type(button_pin))

bsettings = settings_read()
button_pin = int(bsettings['pin'])
GPIO.setmode(GPIO.BCM)
GPIO.setup(int(button_pin),GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(int(button_pin),GPIO.RISING, callback=button_interupt_handler, bouncetime=100)
i = 1
while True:
    time.sleep(1)
    print('i = {}'.format(i))
