import sqlite3, time, os, glob, sys
import ds18b20 as DS18B20

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
  f = open(device_file, 'r')
  lines = f.readlines()
  f.close()
  return lines

def read_temp():
  lines = read_temp_raw()
  while lines[0].strip()[-3:] != 'YES':
    time.sleep(0.2)
    lines = read_temp_raw()
  equals_pos = lines[1].find('t=')
  if equals_pos != -1:
    temp_string = lines[1][equals_pos+2:]
    temp_c = float(temp_string) / 1000.0
    temp_f = temp_c * 9.0 / 5.0 + 32.0
    return temp_c

upload_time = time.time()

While True:
    while (time.time() < (upload_time + 5)):
        time.sleep(.1)
    upload_time = time.time()
    date_str = time.strftime('%x')
    time_str = time.strftime('%X')
    conn = sqlite3.connect('temp.db')
    c = conn.cursor()
    c.execute("INSERT INTO temp_values VALUES (1, read_temp(), date_str, time_str)")
    conn.commit()
    conn.close()
