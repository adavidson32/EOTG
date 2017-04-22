import time
from state_alert import sqlite_update
import sqlite3

def background(all_settings):
    print('New State: Background')
    t_last_button_check = time.time()-0.5
    sqlite_update('device_info', 'current_state', 'background')
    background_loop_return = background_loop(all_settings, t_last_button_check)
    loop_exit, t_last_button_check = background_loop_return
    if loop_exit == 'hold_detected':
        return 'waiting'
    elif ((loop_exit == '1x_detected') or (loop_exit == '2x_detected')):
        print('dislay battery....')
        background(all_settings)

def background_loop(all_settings, t_last_button_check):
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    c.execute("SELECT * FROM button_events WHERE detect_time>(?)", (t_last_button_check, ))
    last_press = c.fetchone()
    conn.commit()
    conn.close()
    t_last_button_check = time.time()
    detect_t = ('TOTAL CRAP', )
    if last_press is None:
         time.sleep(0.5)
         return background_loop(all_settings, t_last_button_check)
    elif last_press[0] == 'hold':
        detect_t = ('hold_detected', t_last_button_check)
    elif last_press[0] == '1x':
        detect_t = ('1x_detected', t_last_button_check)
    elif last_press[0] == '2x':
        detect_t = ('2x_detected', t_last_button_check)
    if not(last_press is None):
        return detect_t
