import sqlite3

def sqlite_update(table, setting, new_value):
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    sqlCommand = 'UPDATE {} SET {} = {}'.format(table, setting, new_value)
    c.execute(sqlCommand)
    conn.commit()
    conn.close()
