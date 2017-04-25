# setup/brewing.py

import time
from eotg_ws import brewStarted
from getProfile import getProfile
import sqlite3

def brewing(all_settings, sensors):
    print('New State: Brewing')
    brewStarted()
    pump, heater = (sensors[2], sensors[3])
    current_profile = getProfile()
    print('Brewing Profile Selected:')
    print('#: {}, name: {}, temp: {}, volume: {}'.format(current_profile[0], current_profile[1], current_profile[2], current_profile[3]))
    heater.on()
    t_brew_start = time.time()
    t_brew_end = t_brew_start + 81.0
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    while time.time() < (t_brew_start + 21.0):
        c.execute("SELECT * FROM button_events WHERE detect_time>?", (t_brew_start,))
        last_press = c.fetchone()
        if last_press is None:
            time.sleep(0.1)
        elif last_press[0] == '2x':
            return 'waiting'
    conn.close()
    pump.pwm_start()
    t_last_button_check = time.time()-0.3
    brewing_loop_return = brewing_loop(all_settings, t_last_button_check, t_brew_end)
    loop_exit, t_last_button_check = brewing_loop_return
    print(loop_exit)
    if (loop_exit == '2x_detected'):
        print('2x detected, cancelling brew, returning to waiting state')
        pump.pwm_stop()
        heater.off()
        return 'waiting'
    elif (loop_exit == 'hold_detected'):
        print('hold_detected, doing nothing')
    elif (loop_exit == '1x_detected'):
        print('1x detected, doing nothing')
    elif loop_exit == 'timeout':
        pump.pwm_stop()
        heater.off()
        return 'waiting'

def brewing_loop(all_settings, t_last_button_check, t_brew_end):
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    c.execute("SELECT * FROM button_events WHERE detect_time>?", (t_last_button_check,))
    last_press = c.fetchone()
    conn.close()
    t_last_button_check = time.time()
    detect_t = ('TOTAL CRAP', )
    if last_press is None:
        time.sleep(0.1)
        if time.time() > t_brew_end:
            return ('timeout', t_last_button_check)
        else:
            return brewing_loop(all_settings, t_last_button_check, t_brew_end)
    elif last_press[0] == 'hold':
        detect_t = ('hold_detected', t_last_button_check)
    elif last_press[0] == '1x':
        detect_t = ('1x_detected', t_last_button_check)
    elif last_press[0] == '2x':
        detect_t = ('2x_detected', t_last_button_check)
    if not(last_press is None):
        if detect_t == ('2x_detected', t_last_button_check):
            return detect_t
        else:
            return brewing_loop(all_settings, t_last_button_check, t_brew_end)
