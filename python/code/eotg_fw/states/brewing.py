from time import time
from state_alert import sqlite_update
import sqlite3

def brewing(all_settings, sensors):
    print('New State: Brewing')
    pump, heater = (sensors[2], sensors[3])
    t_last_button_check = (time()-1,)
    sqlite_update('device_info', 'current_state', 'brewing')
    loop_exit = brewing_loop(all_settings, t_last_connect)
    if ((loop_exit == 'hold_detected') or (loop_exit == '2x_detected')):
        return 'waiting'
    elif loop_exit == time:
        return 'waiting'

def brewing_loop(all_settings, t_last_button_check):
    conn = sqlite3('../main/eotg.db')
    c = conn.cursor()
    c.execute('SELECT * FROM button_events WHERE detect_time>? ORDER BY detect_time DESC', t_last_button_check)
    try:
        last_press = c.fetchone()
        conn.commit()
        conn.close()
        t_last_button_check = time()
        if last_press[0] == 'hold':
            return 'hold_detected'
        elif last_press[0] == '1x':
            return '1x_detected'
        elif last_press[0] == '2x':
            return '2x_detected'
    except:
        time.sleep(0.5)
        brewing_loop(all_settings, t_last_button_check)
