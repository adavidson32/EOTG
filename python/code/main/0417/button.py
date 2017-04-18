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
    GPIO.remove_event_detect(button_pin)
    t_1x_start = time.time()
    ret = GPIO.wait_for_edge(button_pin, GPIO.FALLING, timeout=5000)
    t_1x_end = time.time()
    t_1x = t_1x_end - t_1x_start
    if ret is None:
        return 'too_long'
    else:
        if (t_1x > 2):
            return 'hold'
        elif (t_1x < 0.1):
            return 'nothing'
        elif (t_1x > 1):
            return 'nothing'
        else:
            ret = GPIO.wait_for_edge(bottom_pin, GPIO.RISING, timeout=1000)
            if ret is None:
                return '1x_press'
            else:
                ret = GPIO.wait_for_edge(bottom_pin, GPIO.FALLING, timeout=1000)
                if ret is None:
                    return 'nothing'
                else:
                    return '2x_press'
    GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
bsettings = settings_read()
button_pin = int(bsettings['pin'])
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
i = 1
while True:
    time.sleep(1)
