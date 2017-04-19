import sqlite3

def sqlite_update_di(table, setting, new_value):
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    c.execute('UPDATE device_info SET ?=?', (setting, new_value))
    conn.commit()
    conn.close()
