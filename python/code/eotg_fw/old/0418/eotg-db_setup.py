#Import necessary libraries
#---------------------------------------------------------------------
import sqlite3, math
from time import strftime, localtime, time
from gmacser import getMAC, getserial
#---------------------------------------------------------------------

#Define default sqlite3 database tables
#---------------------------------------------------------------------
now = math.floor(time())
device_settings = [
            # (setting name) , (setting value)
            ('serial_num', getserial()),
            ('mac_addr', getMAC('wlan0')),
            ('given_id_num', 'none'),
            ('current_state', 'off')
            ]
button_settings = [
            # (setting name) , (setting value)
            ('pin', 21),
            ('t_1x_min', 0.1),
            ('t_1x_max', 1.0),
            ('t_btw_min', 0.1),
            ('t_btw_max', 1.0),
            ('t_hold_min', 2.0),
            ('t_timeout', 4.0),
            ('freq_updatecheck', 60)
            ]
button_events = [
            # (press type) , (time of event)
            ('1x', now-500),
            ('2x', now-1000),
            ('hold', now-2000)
            ]
neopixel_settings = [
            ('pin', 18),
            ('brightness', 50)
            ]
update_settings = [
            ('freq_background', 10),
            ('freq_waiting', 3),
            ('freq_brewing', 1),
            ('t_last_update', now-600)
            ]
ds18b20_settings = [
            # 'sensor #' , 'custom name' , 'ds18b20_64bit_ID#'
            ('ds0', 'coffee-temp', '051686663cff'),
            ('ds1', 'air-temp_1', '041686a581ff'),
            ('ds2', 'empty', 'empty')
            ]
mpu6050_settings = [
            ('i2c_addr', 76),
            ('level_deg', 5),
            ('sr_background', 10),
            ('sr_waiting', 1),
            ('sr_brewing', 0.5)
            ]
bmp280_settings = [
            ('i2c_addr', 76),
            ('level_deg', 5),
            ('sr_background', 10),
            ('sr_waiting', 1),
            ('sr_brewing', 0.5)
            ]
relay_values = [
            ('pump', 5, 'OFF'),
            ('heater', 6, 'OFF')
            ]
wifi_list = [
            #(network #) , (ssid) , (password), 'security type' , 'opt: username' , 'Last RSSI(dB)' , 'last connection time'
            (1, 'notyowifi-2.4', 'test_password_1', 'WPA', 'none', 40, now-100),
            (2, 'notyowifi-guest', 'test_password_2', 'WPA', 'none', 38, now-1000),
            (3, 'empty', 'empty', 'empty', 'empty', -1, -1),
            ]
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
        c.execute('DELETE * FROM button_settings')
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
        c.execute('DELETE * FROM relay_values')
        c.executemany('INSERT INTO relay_values VALUES (?, ?)', relay_values)
        conn.commit()
        print('relay value table restored to default:')
    print('')
    print('Relay Values:')
    for row in c.execute('SELECT * FROM relay_values'):
        print('Function: {0}, State: {2}, Pin: {1}'.format(row[0], row[1]), row[2])
    print('')
    conn.close()

def upd_device_settings():
    conn = sqlite3.connect('eotg.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE device_settings
                (variable text, val text)''')
        c.executemany('INSERT INTO device_settings VALUES (?, ?)', device_settings)
        conn.commit()
        print('device settings table created sucessfully:')
    except sqlite3.OperationalError:
        c.execute('DELETE * FROM device_settings')
        c.executemany('INSERT INTO device_settings VALUES (?, ?)', device_settings)
        conn.commit()
        print('device settings table restored to default:')
    print('')
    print('Device Settings:')
    for row in c.execute('SELECT * FROM device_settings'):
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
        c.execute('DELETE * FROM wifi_settings')
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
        c.execute('DELETE * FROM button_events')
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
