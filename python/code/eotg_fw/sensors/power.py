

def ac_connected_check(ac_status_last):
    ac_status = read_powerboost_5Vin()
    if not(ac_status == ac_status_last):

    return ac_status

def battery_level_check(batt_level_last):
    batt_level = read_powerboost_Vbatt()
    return batt_level

def db_status_update(power_stat, value):
    power_stat_t = (power_stat,)
    conn = sqlite3.connect('eotg.db')
    c = conn.cursor()
    c.execute('UPDATE device_status SET va ')
