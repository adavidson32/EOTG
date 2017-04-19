from time import time
from state_alert import sqlite_update
import sqlite3

def background(all_settings):
    print('New State: Background')
    t_last_button_check = (time()-1,)
    sqlite_update('device_info', 'current_state', 'background')
    loop_exit, t_last_button_check = background_loop(all_settings, t_last_button_check)
    if loop_exit == 'hold_detected':
        return 'waiting'
    elif ((loop_exit == '1x_detected') or (loop_exit == '2x_detected')):
        print('dislay battery....')
        background(all_settings)

def background_loop(all_settings, t_last_button_check):
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    c.execute('SELECT * FROM button_events WHERE detect_time>? ORDER BY detect_time DESC', t_last_button_check)
    try:
        last_press = c.fetchone()
        conn.commit()
        conn.close()
        t_last_button_check = time()
        if last_press[0] == 'hold':
            return 'hold_detected', t_last_button_check
        elif last_press[0] == '1x':
            return '1x_detected', t_last_button_check
        elif last_press[0] == '2x':
            return '2x_detected', t_last_button_check
    except:
        t_last_button_check = time()
        time.sleep(1)
        background_loop(all_settings, t_last_button_check)
