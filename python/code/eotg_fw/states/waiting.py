import sys
sys.path.append('/home/pi/git/EOTG/python/code/eotg_fw/web')
from eotg_ws import shouldBrew
from time import time
from state_alert import sqlite_update
import sqlite3

def waiting(all_settings):
    print('New State: Waiting')
    t_last_button_check = (time.time()-1,)
    sqlite_update('device_info', 'current_state', 'waiting')
    loop_exit = waiting_loop(all_settings, t_last_connect)
    if loop_exit == 'hold_detected':
        return 'background'
    elif loop_exit == '2x_detected':
        return 'brewing'

def waiting_loop(all_settings, t_last_button_check):
    conn = sqlite3('../main/eotg.db')
    c = conn.cursor()
    c.execute('SELECT * FROM button_events WHERE detect_time>? ORDER BY detect_time DESC', t_last_button_check)
    try:
        last_press = c.fetchone()
        conn.commit()
        conn.close()
        t_last_button_check = time.time()
        if last_press[0] == 'hold':
            return 'hold_detected'
        elif last_press[0] == '1x':
            return '1x_detected'
        elif last_press[0] == '2x':
            return '2x_detected'
        else:
            # If no buttons are pressed, get the status from the web
            shouldBrew = shouldBrew()
            if shouldBrew == 1:
                return 'remote_start_detected'
    except:
        time.sleep(1)
        waiting_loop(all_settings, t_last_button_check)
