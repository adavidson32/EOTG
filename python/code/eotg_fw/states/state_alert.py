import sqlite3

def sqlite_update(table, setting, new_value):
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    c.execute('UPDATE %s SET %s=%s',(table, setting, new_value))
    conn.commit()
    conn.close()
