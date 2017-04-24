import math, sqlite3
import RPi.GPIO as io
from state_alert import sqlite_update

class pb_check:
    def __init__(self, ac_batt_settings):
        self.ac_pin = ac_batt_settings['ac_check_pin']
        self.batt_pin = ac_batt_settings['batt_check_pin']
        io.setmode(io.BCM)
        io.setup(self.ac_pin, io.IN, pull_up_down=io.PUD_DOWN)
        io.setup(self.batt_pin, io.IN, pull_up_down=io.PUD_DOWN)

    def ac_check(self, ac_last):
        ac_state = io.input(self.ac_pin)
        ac_ret = 'connected' if ac_status else 'disconnected'
        print(ac_ret)
        if not(ac_state == ac_last):
            sqlite_update('device_info', 'ac_state', ac_state)
        return ac_ret

    def battery_check(self, batt_last):
        batt_level = io.input(self.ac_pin)
        battery_level = 'HIGH' if batt_level else 'LOW'
        print(battery_level)
        if not(battery_level == batt_last):
            sqlite_update('device_info', 'battery_level', battery_level)
        return battery_level

    def check_orientation(self, mpu):
      accel_data = mpu.get_accel_data()
      ax = float("{0:.3f}".format(accel_data['x']))
      ay = float("{0:.3f}".format(accel_data['y']))
      az = float("{0:.3f}".format(accel_data['z']))
      xz_fraction = math.fabs(ax / az)
      yz_fraction = math.fabs(ay / az)
      xz_angle = math.degrees(math.atan(xz_fraction))
      yz_angle = math.degrees(math.atan(yz_fraction))
      print("xz-angle: {0:.1f} deg.,  yz-angle: {1:.1f} deg.".format(xz_angle, yz_angle))
      if ((xz_angle <= 5) and (yz_angle <= 5)):
        return "level"
      elif ((xz_angle > 5) or (yz_angle  > 5)):
        return "not-level"

    def prebrew_check(self, mpu):
        conn = sqlite3.connect('../main/eotg.db')
        c = conn.cursor()
        d_di = c.execute('SELECT * FROM device_info')
        row_di = d_di.fetchone()
        ac_last, batt_last = row_di[4], row_di[2]
        conn.close()
        current_ac = ac_check(ac_last)
        current_batt = battery_check(batt_last)
        current_orientation = check_orientation(mpu)
        if ((current_ac == 'connected') and (current_orientation == 'level')):
            return 'good'
        else:
            print('ac: {}, batt: {}, mpu: {}'.format(current_ac, current_batt, current_orientation))
            return 'not-good'
