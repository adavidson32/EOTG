import RPi.GPIO as GPIO
import time, sqlite3, math

def settings_read():
    conn = sqlite3.connect('eotg.db')
    c = conn.cursor()
    button_settings_list = []
    for row in c.execute('SELECT * FROM button_settings'):
        button_tuple = (row[0], row[1])
        button_settings_list.append(button_tuple)
    return dict(button_settings_list)

def store_press(press_type):
    conn = sqlite3.connect('eotg.db')
    c = conn.cursor()
    insert_str = [(press_type, time.time())]
    c.executemany('INSERT INTO button_events VALUES (?, ?)', insert_str)
    conn.commit()
    conn.close()
    print('Added to eotg.db:  {:>4} detected at {:<.2f}'.format(press_type, time.time()))

def button_interupt_handler(button_pin):
    GPIO.remove_event_detect(button_pin)
    t_1x_start = time.time()
    ret = GPIO.wait_for_edge(button_pin, GPIO.FALLING, timeout=int(1000*bsettings['t_timeout']))
    t_1x_end = time.time()
    t_1x = t_1x_end - t_1x_start
    if ret is None:
        print('hold detected')
        GPIO.remove_event_detect(button_pin)
        GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
        store_press('hold')
    else:
        if (t_1x > bsettings['t_hold_min']):
            print('hold detected')
            GPIO.remove_event_detect(button_pin)
            GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
            store_press('hold')
        elif (t_1x < bsettings['t_1x_min']):
            print('too quick')
            GPIO.remove_event_detect(button_pin)
            GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
            return
        elif (t_1x > bsettings['t_1x_max']):
            print('too long but not hold (1s < t < 2s)')
            GPIO.remove_event_detect(button_pin)
            GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
            return
        else:
            GPIO.remove_event_detect(button_pin)
            ret1 = GPIO.wait_for_edge(button_pin, GPIO.RISING, timeout=int(1000*bsettings['t_btw_max']))
            if ret1 is None:
                print('1x press detected')
                GPIO.remove_event_detect(button_pin)
                GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
                store_press('1x')
            elif ((time.time() - t_1x_end) > bsettings['t_btw_min']):
                GPIO.remove_event_detect(button_pin)
                ret2 = GPIO.wait_for_edge(button_pin, GPIO.FALLING, timeout=int(1000*bsettings['t_1x_max']))
                if ret2 is None:
                    print('2nd press too long')
                    GPIO.remove_event_detect(button_pin)
                    GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
                    return
                else:
                    print('2x press detected')
                    GPIO.remove_event_detect(button_pin)
                    GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
                    store_press('2x')

bsettings = settings_read()
button_pin = int(bsettings['pin'])
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)

while True:
    time.sleep(bsettings['freq_updatecheck'])
    new_bsettings = settings_read()
    if not(bsettings['pin'] == new_bsettings['pin']):
        GPIO.remove_event_detect(button_pin)
        bsettings = new_bsettings
        button_pin = int(bsettings['pin'])
        GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_interupt_handler)
    if not(bsettings == new_bsettings):
        bsettings = new_bsettings
