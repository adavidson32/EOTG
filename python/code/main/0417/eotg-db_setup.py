#Import necessary libraries
#---------------------------------------------------------------------
import sqlite3
#---------------------------------------------------------------------


#Define variable list
#---------------------------------------------------------------------
var_list = [
        ('update', 'update_freq', 5.0),
        ('button', 'pin', 21),
        ('button', 't_1x_min', 0.1),
        ('button', 't_1x_max', 1.2),
        ('button', 't_btw_max', 1.0),
        ('button', 't_hold_min', 2.0),
        ('button', 't_hold_max', 4.0),
        ('button', 't_timeout', 10.0),
        ('button', 't_samplerate', 0.01),
        ('neopixel', 'pin', 18)
        ]

#Import variable list
conn = sqlite3.connect('eotg.db')
c = conn.cursor()
try:
    c.execute('''CREATE TABLE setup_variables
                (category text, variable text, value REAL)''')
    c.executemany('INSERT INTO setup_variables VALUES (?, ?, ?)', var_list)
    conn.commit()
    print('variables saved/updated sucessfully')
except sqlite3.OperationalError:
    print('Variable Table Already Exists')
    #Change so values will be updated or deleted then updated...
conn.close()
#---------------------------------------------------------------------


#---------------------------------------------------------------------
#Define wifi list
wifi_list = [
        (1, 'notyowifi-2.4', 'test_password_1'),
        (2, 'notyowifi-guest', 'test_password_2'),
        (3, 'empty', 'empty')
        ]

#Save wifi list
conn = sqlite3.connect('eotg.db')
c = conn.cursor()
try:
    c.execute('''CREATE TABLE wifi_variables
              (priority INTEGER, ssid TEXT, password TEXT)''')
    c.executemany('INSERT INTO wifi_variables VALUES (?, ?, ?)', wifi_list)
    conn.commit()
    print('wifi data saved/updated sucessfully')
except sqlite3.OperationalError:
    print('Wifi Table Already Exists')
    #Change so values will be updated or deleted then updated...
conn.close()
#---------------------------------------------------------------------


#---------------------------------------------------------------------
#print all contents of each to test:
conn = sqlite3.connect('eotg.db')
c = conn.cursor()
print('')
print('Variable Setup printout: ')
for row in c.execute('SELECT * FROM setup_variables'):
    print('Category: {}, Variable: {}, Value: {}'.format(row[0], row[1], row[2]))
print('')
print('WiFi Setup printout: ')
for row in c.execute('SELECT * FROM wifi_variables'):
    print('Priority: {}, SSID: {}, Password: {}'.format(row[0], row[1], row[2]))
conn.close()
#---------------------------------------------------------------------
