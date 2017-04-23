# setup/brewing.py

import time
from eotg_ws import brewStarted
import sqlite3
from math import fmod

def brewing(all_settings, sensors):
    print('New State: Brewing')
    pump, heater = (sensors[2], sensors[3])
    brewStarted()
    pump.on()
    heater.on()
    pump_on_time = 1.0
    pump_off_time = 5.0
    t_brew_start = time.time()
    t_brew_end = t_brew_start + 30.0
    t_last_button_check = time.time()-0.3
    brewing_loop_return = brewing_loop(all_settings, pump, t_last_button_check, pump_on_time, pump_off_time, t_brew_start, t_brew_end)
    loop_exit, t_last_button_check = brewing_loop_return
    print(loop_exit)
    if ((loop_exit == 'hold_detected') or (loop_exit == '2x_detected')):
        pump.off()
        heater.off()
        return 'waiting'
    elif loop_exit == 'timeout':
        #pump.off(all_settings['pump_settings']['pin'])
        #heater.off(all_settings['heater_settings']['pin'])
        pump.off()
        heater.off()
        return 'waiting'

def brewing_loop(all_settings, pump, t_last_button_check, pump_on_time, pump_off_time, t_brew_start, t_brew_end):
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    c.execute("SELECT * FROM button_events WHERE detect_time>?", (t_last_button_check,))
    last_press = c.fetchone()
    conn.commit()
    conn.close()
    t_last_button_check = time.time()
    detect_t = ('TOTAL CRAP', )
    if last_press is None:
        time.sleep(0.1)
        if fmod((time.time()-t_brew_start), (pump_on_time + pump_off_time)) > pump_on_time:
            pump.off()
        elif fmod((time.time()-t_brew_start), (pump_on_time + pump_off_time)) < pump_on_time:
            pump.on()
        if time.time() > t_brew_end:
            return ('timeout', t_last_button_check)
        else:
            return brewing_loop(all_settings, pump, t_last_button_check, pump_on_time, pump_off_time, t_brew_start, t_brew_end)
    elif last_press[0] == 'hold':
        detect_t = ('hold_detected', t_last_button_check)
    elif last_press[0] == '1x':
        detect_t = ('1x_detected', t_last_button_check)
    elif last_press[0] == '2x':
        detect_t = ('2x_detected', t_last_button_check)
    if not(last_press is None):
        return detect_t
