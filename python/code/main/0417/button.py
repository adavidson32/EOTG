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
    ret = GPIO.wait_for_edge(button_pin, GPIO.FALLING, timeout=3000)
    t_1x_end = time.time()
    t_1x = t_1x_end - t_1x_start
    if ret is None:
        print('hold detected')
        GPIO.remove_event_detect(button_pin)
        GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
        return 'hold'
    else:
        if (t_1x > 1.5):
            print('hold detected')
            GPIO.remove_event_detect(button_pin)
            GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
            return 'hold'
        elif (t_1x < 0.1):
            print('too quick')
            GPIO.remove_event_detect(button_pin)
            GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
            return 'nothing'
        elif (t_1x > 1):
            print('too long')
            GPIO.remove_event_detect(button_pin)
            GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
            return 'nothing'
        else:
            GPIO.remove_event_detect(button_pin)
            ret1 = GPIO.wait_for_edge(button_pin, GPIO.RISING, timeout=1000)
            if ret1 is None:
                print('1x press detected')
                GPIO.remove_event_detect(button_pin)
                GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
                return '1x_press'
            elif ((time.time() - t_1x_end) > 0.1):
                GPIO.remove_event_detect(button_pin)
                ret2 = GPIO.wait_for_edge(button_pin, GPIO.FALLING, timeout=1000)
                if ret2 is None:
                    print('2nd press too long')
                    GPIO.remove_event_detect(button_pin)
                    GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
                    return 'nothing'
                else:
                    print('2x press detected')
                    GPIO.remove_event_detect(button_pin)
                    GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
                    return '2x_press'

bsettings = settings_read()
button_pin = int(bsettings['pin'])
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
a = GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
i = 1
while True:
    time.sleep(5)
    print(a)
