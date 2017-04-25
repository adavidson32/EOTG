import RPi.GPIO as GPIO
import time, sqlite3, math

class button:
    def __init__(self):
        self.bsettings = self.settings_read()
        self.button_pin = int(self.bsettings['pin'])
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.button_pin, GPIO.RISING, callback=self.button_interupt_handler)

    def button_manager(self):
        while(self.stopped != True):
           try:
               time.sleep(self.bsettings['freq_updatecheck'])
               new_bsettings = self.settings_read()
               if not(self.bsettings['pin'] == new_bsettings['pin']):
                   GPIO.remove_event_detect(self.button_pin)
                   self.bsettings = new_bsettings
                   self.button_pin = int(self.bsettings['pin'])
                   GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                   GPIO.add_event_detect(self.button_pin, GPIO.RISING, callback=self.button_interupt_handler)
               elif not(self.bsettings == new_bsettings):
                   self.bsettings = new_bsettings
           except Exception as ex:
               print('Exception while reading button: ' + str(ex))
               self.stop()
        self.stop()

    def settings_read(self):
        conn = sqlite3.connect('../main/eotg.db')
        c = conn.cursor()
        tu_bs = ('pin', 't_1x_min', 't_1x_max', 't_btw_min', 't_btw_max', 't_hold_min', 't_timeout', 'freq_updatecheck')
        d_bs = c.execute('SELECT * FROM button_settings')
        row_bs = d_bs.fetchone()
        conn.close()
        button_settings = dict(zip(tu_bs, row_bs))
        return button_settings

    def store_press(self, press_type):
        conn = sqlite3.connect('../main/eotg.db')
        c = conn.cursor()
        insert_str = [(press_type, 'background', time.time(), 'none')]
        c.executemany('INSERT INTO button_events VALUES (?, ?, ?, ?)', insert_str)
        conn.commit()
        conn.close()
        #print('Added to eotg.db:  {:>4} detected at {:<.2f}'.format(press_type, time.time()))

    def button_interupt_handler(self, button_pin):
        GPIO.remove_event_detect(button_pin)
        t_1x_start = time.time()
        ret = GPIO.wait_for_edge(button_pin, GPIO.FALLING, timeout=int(1000*self.bsettings['t_timeout']))
        t_1x_end = time.time()
        t_1x = t_1x_end - t_1x_start
        if ret is None:
            print('hold detected')
            GPIO.remove_event_detect(button_pin)
            GPIO.add_event_detect(button_pin,GPIO.RISING,callback=self.button_interupt_handler)
            self.store_press('hold')
        else:
            if (t_1x > self.bsettings['t_hold_min']):
                print('hold detected')
                GPIO.remove_event_detect(button_pin)
                GPIO.add_event_detect(button_pin,GPIO.RISING,callback=self.button_interupt_handler)
                self.store_press('hold')
            elif (t_1x < self.bsettings['t_1x_min']):
                print('too quick')
                GPIO.remove_event_detect(button_pin)
                GPIO.add_event_detect(button_pin,GPIO.RISING,callback=self.button_interupt_handler)
                return
            elif (t_1x > self.bsettings['t_1x_max']):
                print('too long but not hold (1s < t < 2s)')
                GPIO.remove_event_detect(button_pin)
                GPIO.add_event_detect(button_pin,GPIO.RISING,callback=self.button_interupt_handler)
                return
            else:
                GPIO.remove_event_detect(button_pin)
                ret1 = GPIO.wait_for_edge(button_pin, GPIO.RISING, timeout=int(1000*self.bsettings['t_btw_max']))
                if ret1 is None:
                    print('1x press detected')
                    GPIO.remove_event_detect(button_pin)
                    GPIO.add_event_detect(button_pin,GPIO.RISING,callback=self.button_interupt_handler)
                    self.store_press('1x')
                elif ((time.time() - t_1x_end) > self.bsettings['t_btw_min']):
                    GPIO.remove_event_detect(button_pin)
                    ret2 = GPIO.wait_for_edge(button_pin, GPIO.FALLING, timeout=int(1000*self.bsettings['t_1x_max']))
                    if ret2 is None:
                        print('2nd press too long')
                        GPIO.remove_event_detect(button_pin)
                        GPIO.add_event_detect(button_pin,GPIO.RISING,callback=self.button_interupt_handler)
                        return
                    else:
                        print('2x press detected')
                        GPIO.remove_event_detect(button_pin)
                        GPIO.add_event_detect(button_pin,GPIO.RISING,callback=self.button_interupt_handler)
                        self.store_press('2x')
