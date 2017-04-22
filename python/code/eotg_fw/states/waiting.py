import sys
sys.path.append('/home/pi/git/EOTG/python/code/eotg_fw/web')
from eotg_ws import shouldBrew
import time
from state_alert import sqlite_update
import sqlite3

def waiting(all_settings):
    print('New State: Waiting')
    t_last_button_check = time.time()-0.3
    sqlite_update('device_info', 'current_state', 'waiting')
    waiting_loop_return = waiting_loop(all_settings, t_last_button_check)
    loop_exit, t_last_button_check = waiting_loop_return
    if loop_exit == 'hold_detected':
        return 'background'
    elif ((loop_exit == '2x_detected') or (loop_exit == 'remote_start_detected')):
        #add to-do to re-set remote_start_detected to 0
        return 'brewing'

def waiting_loop(all_settings, t_last_button_check):
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    c.execute("SELECT * FROM button_events WHERE detect_time>?", (t_last_button_check, ))
    last_press = c.fetchone()
    conn.commit()
    conn.close()
    t_last_button_check = time.time()
    detect_t = ('TOTAL CRAP', )
    if last_press is None:
         time.sleep(0.3)
         # If no buttons are pressed, get the status from the web
         brewing_state = shouldBrew()
         if brewing_state == '1':
             return ('remote_start_detected', 10.0)
         else:
             return waiting_loop(all_settings, t_last_button_check)
    if last_press[0] == 'hold':
        detect_t = ('hold_detected', t_last_button_check)
    elif last_press[0] == '1x':
        print('next profile selected...')
        print('switching device to next profile.....')
        detect_t = ('1x_detected', t_last_button_check)
    elif last_press[0] == '2x':
        detect_t = ('2x_detected', t_last_button_check)
    if not(last_press is None):
        return detect_t
