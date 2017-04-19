import os, glob, time, math
import sqlite3
from ds18b20 import DS18B20
from mpu6050 import mpu6050
from relays import relays

def variable_setup():

    tu_di = ('given_id_num', 'current_state', 'battery_level', 'water_level', 'ac_state', 'preset_state', 'remote_brew_start')
    tu_bs = ('pin', 't_1x_min', 't_1x_max', 't_btw_min', 't_btw_max', 't_hold_min', 't_timeout', 'freq_updatecheck')
    tu_be = ('press_type', 'state_during', 'detect_time', 'response')
    tu_us = ('freq_background', 'freq_waiting', 'freq_brewing', 't_last_update')
    tu_dss = ('sensor_id', 'given_name', 'unique_64b_id')
    tu_dsv = ('t_time', 't0', 't1')
    tu_mpu = ('i2c_addr', 'level_deg', 'sr_background', 'sr_waiting', 'sr_brewing')
    tu_rly = ('device', 'pin', 'mode', 't_mode_set', 'current_status')
    tu_wifi = ('network_num', 'ssid', 'password', 'sec_type', 'username', 'IP_addr', 'last_RSSI', 't_last_connect')

    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()

    d_di, d_bs, d_be, d_us = c.execute('SELECT * FROM device_info'), c.execute('SELECT * FROM button_settings'), c.execute('SELECT * FROM button_events'), c.execute('SELECT * FROM update_settings')
    d_dss, d_dsv, d_mpu, d_pump, d_heater, d_wifi = c.execute('SELECT * FROM ds18b20_settings'), c.execute('SELECT * FROM ds18b20_values'), c.execute('SELECT * FROM mpu6050_settings'), c.execute('SELECT * FROM relay_values WHERE device=?',('pump',)), c.execute("SELECT * FROM relay_values WHERE device=?",('heater',)), c.execute('SELECT * FROM wifi_list')

    row_di, row_bs, row_be, row_us = d_di.fetchone(), d_bs.fetchone(), d_be.fetchone(), d_us.fetchone()
    row_dss, row_dsv, row_mpu, row_pump, row_heater, row_wifi = d_dss.fetchall(), d_dsv.fetchall(), d_mpu.fetchone(), d_pump.fetchone(), d_heater.fetchone(), d_wifi.fetchall()

    conn.close()

    ret_di, ret_bs, ret_be, ret_us = dict(zip(tu_di, row_di)),  dict(zip(tu_bs, row_bs)),  dict(zip(tu_be, row_be)),  dict(zip(tu_us, row_us))
    ret_dss, ret_dsv, ret_mpu, ret_pump, ret_heater, ret_wifi = dict(zip(tu_dss, row_dss[0])),  dict(zip(tu_dsv, row_dsv[0])),  dict(zip(tu_mpu, row_mpu)),  dict(zip(tu_rly, row_pump)), dict(zip(tu_rly, row_heater)),  dict(zip(tu_wifi, row_wifi[0])),

    all_settings = {'device_info': ret_di, 'button_settings': ret_bs, 'button_events': ret_be, 'update_settings': ret_us, 'ds18b20_settings': ret_dss, 'ds18b20_values': ret_dsv, 'mpu6050_settings': ret_mpu, 'pump_settings': ret_pump, 'heater_settings': ret_heater, 'wifi_settings': ret_wifi}

    return all_settings

def sensor_setup(all_settings):
    ds = DS18B20()
    mpu = mpu6050(all_settings['mpu6050_settings']['i2c_addr'])
    pump = relays(all_settings['pump_settings']['pin'])
    heater = relays(all_settings['heater_settings']['pin'])
    return ds, mpu, pump, heater
