#Import necessary libraries
#---------------------------------------------------------------------
import sqlite3, math
from time import strftime, localtime, time
from gmacser import getMAC, getserial
#---------------------------------------------------------------------

#Define default sqlite3 database tables
#---------------------------------------------------------------------
now = math.floor(time())

#Columns:    | given_id_num | current_state | battery_level | water_level | ac_state | preset_state | remote_brew_start |
device_info = [    -1       , 'background'  ,    'med'      ,    'high'   ,    1     ,      -1      ,        0         )]

#Columns:         | pin | t_1x_min | t_1x_max | t_btw_min | t_btw_max | t_holdout_min | t_timeout | freq_updatecheck |
button_settings = [ 21  ,   0.1    ,   1.0    ,    0.1    ,    1.0    ,      2.0      ,    4.0    ,      60         )]

#Columns:       | press_type | state_during | detect_time | response |
button_events = [(   '1x'    , 'background' ,   now-10    ,  'none'  ),
                 (  'hold'   ,  'waiting'   ,  now-500    , 'handled')]

#Columns:           | pin | brightness |
neopixel_settings = [( 18 ,    50     )]

#Columns:         | freq_background | freq_waiting | freq_brewing | t_last_update |
update_settings = [(      10        ,      3       ,      1       ,   now-1000   )]

#Columns:          | sensor id# |  given_name  | unique_64b_id  |
ds18b20_settings = [(   'ds0'   , 'coffee-temp', '051686663cff'),
                    (   'ds1'   , 'air-temp_1' , '041686a581ff')]

#Columns:          | i2c_addr | level_deg | sr_background | sr_waiting | sr_brewing |
mpu6050_settings = [(   68    ,    5      ,      10       ,    1       ,     0.5   )]

#Columns:         | i2c_addr | resolution | sr_background | sr_waiting | sr_brewing |
bmp280_settings = [(   76    ,     1.0??  ,      10       ,    5       ,     0.5   )]

#Columns:      |  device  | pin |  mode  | t_mode_set | current_status |
relay_values = [(  'pump' ,  5  , 'off'  ,  now-1000  ,        0      ),
                ( 'heater',  6  , 'off'  ,  now-1000  ,        0      )]

#Columns:   | network_num |       ssid       |     password     | sec_type | username |     IP_addr    | last_RSSI | t_last_connect |
wifi_list = [(     1      ,  'notyowifi-2.4' , 'test_password_1',   'WPA'  ,   'none' , '192.168.1.112',     40    ,    now-100    ),
             (     2      , 'notyowifi-guest', 'test_password_2',   'WPA'  ,   'none' , '192.168.1.131',     38    ,    now-1000   )]

#---------------------------------------------------------------------

#---------------------------------------------------------------------
def upd_button_settings():
    conn = sqlite3.connect('eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE button_settings
                (setting text, val REAL)''')
        c.executemany('INSERT INTO button_settings VALUES (?, ?)', button_settings)
        conn.commit()
        print('button settings table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM button_settings')
        c.executemany('INSERT INTO button_settings VALUES (?, ?)', button_settings)
        conn.commit()
        print('button settings table restored to default:')
    print('')
    print('Button Settings:')
    for row in c.execute('SELECT * FROM button_settings'):
        print('Setting: {}, Value: {}'.format(row[0], row[1]))
    print('')
    conn.close()

def upd_relay_values():
    conn = sqlite3.connect('eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE relay_values
                (name text, pin INTEGER, value text)''')
        c.executemany('INSERT INTO relay_values VALUES (?, ?)', relay_values)
        conn.commit()
        print('relayvalue table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM relay_values')
        c.executemany('INSERT INTO relay_values VALUES (?, ?)', relay_values)
        conn.commit()
        print('relay value table restored to default:')
    print('')
    print('Relay Values:')
    for row in c.execute('SELECT * FROM relay_values'):
        print('Function: {0}, State: {2}, Pin: {1}'.format(row[0], row[1]), row[2])
    print('')
    conn.close()

def upd_device_info():
    conn = sqlite3.connect('eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE device_info
                (variable text, val text)''')
        c.executemany('INSERT INTO device_info VALUES (?, ?)', device_info)
        conn.commit()
        print('device info table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM device_info')
        c.executemany('INSERT INTO device_info VALUES (?, ?)', device_info)
        conn.commit()
        print('device info table restored to default:')
    print('')
    print('Device Info:')
    for row in c.execute('SELECT * FROM device_info'):
        print('{}:  {}'.format(row[0], row[1]))
    print('')
    conn.close()

def upd_wifi_settings():
    conn = sqlite3.connect('eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE wifi_settings
                  (add_num INTEGER, ssid TEXT, password TEXT, sec_type TEXT,
                  opt_username TEXT, rssi INTEGER, t_last_connect INTEGER)''')
        c.executemany('INSERT INTO wifi_settings VALUES (?, ?, ?, ?, ?, ?, ?)', wifi_list)
        conn.commit()
        print('wifi settings table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM wifi_settings')
        c.executemany('INSERT INTO wifi_settings VALUES (?, ?, ?, ?, ?, ?, ?)', wifi_list)
        conn.commit()
        print('wifi settings table restored to default:')
    print('')
    print('Configured Wi-Fi Networks: ')
    for row in c.execute('SELECT * FROM wifi_settings'):
        print('(#{}) SSID: {}, Password: {}, Sec. Type: {}, Last RSSI: {}'.format(row[0], row[1], row[2], row[3], row[5]))
    print('')
    conn.close()

def upd_button_events():
    conn = sqlite3.connect('eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE button_events
                (press_type text, event_time REAL)''')
        c.executemany('INSERT INTO button_events VALUES (?, ?)', button_events)
        conn.commit()
        print('button settings table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM button_events')
        c.executemany('INSERT INTO button_events VALUES (?, ?)', button_events)
        conn.commit()
        print('button events table restored to default:')
    print('')
    print('Button Events:')
    for row in c.execute('SELECT * FROM button_events'):
        print('Press Type: {}, Time Detected: {}'.format(row[0], strftime('%X', localtime(row[1]))))
    print('')
    conn.close()

#---------------------------------------------------------------------


#input which variable to update or reset...
#---------------------------------------------------------------------
print('Which settings would you like to reset to default?')
to_update = input('ex: button, device, wifi, ds18b20, all, etc. : ')
if to_update == 'button':
    upd_button_settings()
elif to_update == 'device':
    upd_device_settings()
elif to_update == 'wifi':
    upd_wifi_settings()
elif to_update == 'button_events':
    upd_button_events()
elif to_update == 'relays':
    upd_relay_values()
elif to_update == 'all':
    upd_button_settings()
    upd_button_events()
    upd_device_settings()
    upd_wifi_settings()
#---------------------------------------------------------------------
