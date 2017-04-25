# setup/eotg-db_setup.py

#Import necessary libraries
#---------------------------------------------------------------------
import sqlite3, math
from time import strftime, localtime, time
from gmacser import getMAC, getserial
#---------------------------------------------------------------------

#Define default sqlite3 database tables
#---------------------------------------------------------------------
now = math.floor(time())

#Columns:    | given_id_num | current_state  | battery_level | water_level | ac_state | preset_state | remote_brew_start |
device_info = [(    -1       , 'background'  ,    'LOW'      ,    'HIGH'   ,    0     ,      -1      ,        0         )]

#Columns:    | brew_setting_type_id | brew_setting_value | t_last_update |
brew_settings = [(       0          ,          ''        ,      -1      )]

#Columns:         | pin | t_1x_min | t_1x_max | t_btw_min | t_btw_max | t_holdout_min | t_timeout | freq_updatecheck |
button_settings = [( 21  ,   0.1    ,   1.0    ,    0.1    ,    1.0    ,      2.0      ,    4.0    ,      5         )]

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
#Columns:        | t_time |  t0 |  t1  | ....t#... |
ds18b20_values = [( now-30, 22.1, 23.4),
                  ( now-35, 21.9, 23.5)]

#Columns:          | i2c_addr | level_deg | sr_background | sr_waiting | sr_brewing |
mpu6050_settings = [(   68    ,    5      ,      10       ,    1       ,     0.5   )]

#Columns:         | i2c_addr | resolution | sr_background | sr_waiting | sr_brewing |
#bmp280_settings = [(   76    ,     1.0??  ,      10       ,    5       ,     0.5   )]

#Columns:      | prof_num |  prof_name  | temp | volume |   color_pattern   |
profile_list = [(    1    , 'custom_1'  ,  203 ,   40   , 'y-gn-prp-blu-gn'),
                (   -1    ,  'manual'   ,  196 ,   52   , 'rd-y-gn-blu-pnk')]

#Columns:      |  device  | pin |  mode  | pwm_freq | pwm_dutycyc |
relay_values = [(  'pump' ,  5  , 'off'  ,  0.1     ,    90      ),
                ( 'heater',  6  , 'off'  ,   0.1     ,    .0833      )]

#Colums:           | ac_check_pin | batt_check_pin |
ac_batt_settings = [(      16     ,      20       )]

#Columns:   | network_num |       ssid       |     password     | sec_type | username |     IP_addr    | last_RSSI | t_last_connect |
wifi_list = [(     1      ,  'notyowifi-2.4' , 'test_password_1',   'WPA'  ,   'none' , '192.168.1.112',     40    ,    now-100    ),
             (     2      , 'notyowifi-guest', 'test_password_2',   'WPA'  ,   'none' , '192.168.1.131',     38    ,    now-1000   )]

#---------------------------------------------------------------------

#---------------------------------------------------------------------
def upd_device_info():
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE device_info
                (given_id_num INTEGER, current_state TEXT, battery_level TEXT, water_level TEXT, ac_state INTEGER, preset_state INTEGER, remote_brew_start INTEGER)''')
        c.executemany('INSERT INTO device_info VALUES (?, ?, ?, ?, ?, ?, ?)', device_info)
        conn.commit()
        print('device info table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM device_info')
        c.executemany('INSERT INTO device_info VALUES (?, ?, ?, ?, ?, ?, ?)', device_info)
        conn.commit()
        print('device info table restored to default:')
    for row in c.execute('SELECT * FROM device_info'):
        print(row)
    conn.close()

def upd_button_settings():
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE button_settings
                (pin INTEGER, t_1x_min REAL, t_1x_max REAL, t_btw_min REAL, t_btw_max REAL, t_hold_min REAL, t_timeout REAL, freq_updatecheck INTEGER)''')
        c.executemany('INSERT INTO button_settings VALUES (?, ?, ?, ?, ?, ?, ?, ?)', button_settings)
        conn.commit()
        print('button settings table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM button_settings')
        c.executemany('INSERT INTO button_settings VALUES (?, ?, ?, ?, ?, ?, ?, ?)', button_settings)
        conn.commit()
        print('button settings table restored to default:')
    for row in c.execute('SELECT * FROM button_settings'):
        print(row)
    conn.close()

def upd_button_events():
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE button_events
                (press_type TEXT, state_during TEXT, detect_time REAL, response TEXT)''')
        c.executemany('INSERT INTO button_events VALUES (?, ?, ?, ?)', button_events)
        conn.commit()
        print('button settings table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM button_events')
        c.executemany('INSERT INTO button_events VALUES (?, ?, ?, ?)', button_events)
        conn.commit()
        print('button events table restored to default:')
    for row in c.execute('SELECT * FROM button_events'):
        print(row)
    conn.close()

def upd_update_settings():
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE update_settings
                (freq_background INTEGER, freq_waiting INTEGER, freq_brewing INTEGER, t_last_update INTEGER)''')
        c.executemany('INSERT INTO update_settings VALUES (?, ?, ?, ?)', update_settings)
        conn.commit()
        print('update settings table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM update_settings')
        c.executemany('INSERT INTO update_settings VALUES (?, ?, ?, ?)', update_settings)
        conn.commit()
        print('update settings table restored to default:')
    for row in c.execute('SELECT * FROM update_settings'):
        print(row)
    conn.close()

def upd_ds18b20_settings():
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE ds18b20_settings
                (sensor_id INTEGER, given_name TEXT, unique_64b_id TEXT)''')
        c.executemany('INSERT INTO ds18b20_settings VALUES (?, ?, ?)', ds18b20_settings)
        conn.commit()
        print('ds18b20 settings table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM ds18b20_settings')
        c.executemany('INSERT INTO ds18b20_settings VALUES (?, ?, ?)', ds18b20_settings)
        conn.commit()
        print('ds18b20 settings table restored to default:')
    for row in c.execute('SELECT * FROM ds18b20_settings'):
        print(row)
    conn.close()

def upd_ds18b20_values():
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE ds18b20_values
                (t_time REAL, t0 REAL, t1 REAL)''')
        c.executemany('INSERT INTO ds18b20_values VALUES (?, ?, ?)', ds18b20_values)
        conn.commit()
        print('ds18b20 values table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM ds18b20_values')
        c.executemany('INSERT INTO ds18b20_values VALUES (?, ?, ?)', ds18b20_values)
        conn.commit()
        print('ds18b20 values table restored to default:')
    for row in c.execute('SELECT * FROM ds18b20_values'):
        print(row)
    conn.close()

def upd_mpu6050_settings():
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE mpu6050_settings
                (i2c_addr INTEGER, level_deg REAL, sr_background INTEGER, sr_waiting REAL, sr_brewing REAL)''')
        c.executemany('INSERT INTO mpu6050_settings VALUES (?, ?, ?, ?, ?)', mpu6050_settings)
        conn.commit()
        print('mpu6050 settings table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM mpu6050_settings')
        c.executemany('INSERT INTO mpu6050_settings VALUES (?, ?, ?, ?, ?)', mpu6050_settings)
        conn.commit()
        print('mpu6050 settings table restored to default:')
    for row in c.execute('SELECT * FROM ds18b20_values'):
        print(row)
    conn.close()

def upd_profiles():
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE profile_list
                (prof_num INTEGER, prof_name TEXT, temp INTEGER, volume INTEGER, color_pattern TEXT)''')
        c.executemany('INSERT INTO profile_list VALUES (?, ?, ?, ?, ?)', profile_list)
        conn.commit()
        print('profile table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM profile_list')
        c.executemany('INSERT INTO profile_list VALUES (?, ?, ?, ?, ?)', profile_list)
        conn.commit()
        print('profile table restored to default:')
    for row in c.execute('SELECT * FROM profile_list'):
        print(row)
    conn.close()

def upd_relays():
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE relay_values
                (device TEXT, pin INTEGER, mode TEXT, pwm_freq REAL, pwm_dutycyc REAL)''')
        c.executemany('INSERT INTO relay_values VALUES (?, ?, ?, ?, ?)', relay_values)
        conn.commit()
        print('relayvalue table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM relay_values')
        c.executemany('INSERT INTO relay_values VALUES (?, ?, ?, ?, ?)', relay_values)
        conn.commit()
        print('relay value table restored to default:')
    for row in c.execute('SELECT * FROM relay_values'):
        print(row)
    conn.close()

def upd_ac_batt():
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE ac_batt_settings
                (ac_check_pin INTEGER, batt_check_pin INTEGER)''')
        c.executemany('INSERT INTO ac_batt_settings VALUES (?, ?)', ac_batt_settings)
        conn.commit()
        print('ac_batt_settings table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM ac_batt_settings')
        c.executemany('INSERT INTO ac_batt_settings VALUES (?, ?)', ac_batt_settings)
        conn.commit()
        print('ac_batt_settings table restored to default:')
    for row in c.execute('SELECT * FROM ac_batt_settings'):
        print(row)
    conn.close()

def upd_wifi_list():
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE wifi_list
                  (add_num INTEGER, ssid TEXT, password TEXT, sec_type TEXT,
                  opt_username TEXT, IP_addr TEXT, rssi INTEGER, t_last_connect INTEGER)''')
        c.executemany('INSERT INTO wifi_list VALUES (?, ?, ?, ?, ?, ?, ?)', wifi_list)
        conn.commit()
        print('wifi list table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE FROM wifi_list')
        c.executemany('INSERT INTO wifi_list VALUES (?, ?, ?, ?, ?, ?, ?, ?)', wifi_list)
        conn.commit()
        print('wifi list table restored to default:')
    print('')
    print('Configured Wi-Fi Networks: ')
    for row in c.execute('SELECT * FROM wifi_list'):
        print('(#{}) SSID: {}, Password: {}, Sec. Type: {}, Last RSSI: {}'.format(row[0], row[1], row[2], row[3], row[5]))
    print('')
    conn.close()
#---------------------------------------------------------------------


#input which variable to update or reset...
#---------------------------------------------------------------------
print('Which settings would you like to reset to default?')
to_update = input('ex: all, button, device, wifi, ds18b20, relays, mpu6050, update: ')
if to_update == 'button':
    upd_button_settings()
    upd_button_events()
elif to_update == 'device':
    upd_device_info()
elif to_update == 'wifi':
    upd_wifi_list()
elif to_update == 'relays':
    upd_relays()
elif to_update == 'mpu6050':
    upd_mpu6050_settings()
elif to_update == 'ds18b20':
    upd_ds18b20_settings()
    upd_ds18b20_values()
elif to_update == 'update':
    upd_update_settings()
elif to_update == 'all':
    upd_device_info()
    upd_button_settings()
    upd_button_events()
    upd_update_settings()
    upd_ds18b20_settings()
    upd_ds18b20_values()
    upd_mpu6050_settings()
    upd_profiles()
    upd_relays()
    upd_ac_batt()
    upd_wifi_list()
#---------------------------------------------------------------------
