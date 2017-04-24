# setup/setup.py

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
    tu_prof = ('prof_num', 'prof_name', 'temp', 'volume', 'color_pattern')
    tu_rly = ('device', 'pin', 'mode', 't_mode_set', 'current_status')
    tu_ac_batt = ('ac_check_pin', 'batt_check_pin')
    tu_wifi = ('network_num', 'ssid', 'password', 'sec_type', 'username', 'IP_addr', 'last_RSSI', 't_last_connect')

    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()

    d_di = c.execute('SELECT * FROM device_info')
    row_di = d_di.fetchone()
    d_bs = c.execute('SELECT * FROM button_settings')
    row_bs = d_bs.fetchone()
    d_be = c.execute('SELECT * FROM button_events')
    row_be = d_be.fetchone()
    d_us = c.execute('SELECT * FROM update_settings')
    row_us = d_us.fetchone()
    d_dss = c.execute('SELECT * FROM ds18b20_settings')
    row_dss = d_dss.fetchone()
    d_dsv = c.execute('SELECT * FROM ds18b20_values')
    row_dsv = d_dsv.fetchone()
    d_mpu = c.execute('SELECT * FROM mpu6050_settings')
    row_mpu = d_mpu.fetchone()
    d_prof = c.execute('SELECT * FROM profile_list')
    rows_profile1 = d_prof.fetchone()
    d_pump = c.execute('SELECT * FROM relay_values WHERE device=?',('pump',))
    row_pump = d_pump.fetchone()
    d_heater = c.execute("SELECT * FROM relay_values WHERE device=?",('heater',))
    row_heater = d_heater.fetchone()
    d_ac_batt = c.execute('SELECT * FROM ac_batt_settings')
    row_ac_batt = d_ac_batt.fetchone()
    d_wifi = c.execute('SELECT * FROM wifi_list')
    row_wifi = d_wifi.fetchone()
    conn.close()

    ret_di, ret_bs, ret_be, ret_us = dict(zip(tu_di, row_di)),  dict(zip(tu_bs, row_bs)),  dict(zip(tu_be, row_be)),  dict(zip(tu_us, row_us))
    ret_dss, ret_dsv, ret_mpu, ret_profile1, ret_pump, ret_heater, ret_ac_batt, ret_wifi = dict(zip(tu_dss, row_dss)),  dict(zip(tu_dsv, row_dsv)),  dict(zip(tu_mpu, row_mpu)), dict(zip(tu_prof, rows_profile1)), dict(zip(tu_rly, row_pump)), dict(zip(tu_rly, row_heater)), dict(zip(tu_ac_batt, row_ac_batt)), dict(zip(tu_wifi, row_wifi))

    all_settings = {'device_info': ret_di, 'button_settings': ret_bs, 'button_events': ret_be, 'update_settings': ret_us, 'ds18b20_settings': ret_dss, 'ds18b20_values': ret_dsv, 'mpu6050_settings': ret_mpu, 'profile1': ret_profile1, 'pump_settings': ret_pump, 'heater_settings': ret_heater, 'ac_batt_settings': ret_ac_batt, 'wifi_settings': ret_wifi}
    return all_settings

def sensor_setup(all_settings):
    ds = DS18B20()
    if all_settings['mpu6050_settings']['i2c_addr'] == 68:
        mpu_addr = 0x68
    mpu = mpu6050(mpu_addr)
    pump = relays(all_settings['pump_settings'])
    heater = relays(all_settings['heater_settings'])
    return ds, mpu, pump, heater
