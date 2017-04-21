import time
from state_alert import sqlite_update
from eotg_ws import brewStarted
import sqlite3

def brewing(all_settings, sensors):
    print('New State: Brewing')
    pump, heater = (sensors[2], sensors[3])
    brewStarted()
    pump.on()
    heater.on()
    t_brew_start = time.time()
    t_brew_end = t_brew_start + 30.0
    t_last_button_check = time.time()-1.0
    sqlite_update('device_info', 'current_state', 'brewing')
    brewing_loop_return = brewing_loop(all_settings, t_last_button_check)
    loop_exit, t_last_button_check = brewing_loop_return
    if ((loop_exit == 'hold_detected') or (loop_exit == '2x_detected')):
        pump.off()
        heater.off()
        return 'waiting'
    elif loop_exit == 'timeout':
        pump.off()
        heater.off()
        return 'waiting'

def brewing_loop(all_settings, t_last_button_check):
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    c.execute("SELECT * FROM button_events WHERE detect_time>?", (t_last_button_check,))
    last_press = c.fetchone()
    conn.commit()
    conn.close()
    t_last_button_check = time.time()
    detect_t = ('TOTAL CRAP', )
    if last_press is None:
        time.sleep(0.5)
        if time.time() > t_brew_end:
            return 'timeout'
        else:
            return brewing_loop(all_settings, t_last_button_check)
    elif last_press[0] == 'hold':
        detect_t = ('hold_detected', t_last_button_check)
    elif last_press[0] == '1x':
        detect_t = ('1x', t_last_button_check)
    elif last_press[0] == '2x':
        detect_t = ('2x', t_last_button_check)
    if not(last_press is None):
        return detect_t
