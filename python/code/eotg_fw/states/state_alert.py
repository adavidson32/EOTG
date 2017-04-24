# states/state_alert.py

import sqlite3

def sqlite_update(table, setting, new_value):
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    sqlCommand = ("UPDATE {0} SET {1} = '{2}'".format(table, setting, new_value))
'''    print(sqlCommand)
    print(type(sqlCommand))
    print(len(sqlCommand)) '''
    c.execute(sqlCommand)
    conn.commit()
    conn.close()
