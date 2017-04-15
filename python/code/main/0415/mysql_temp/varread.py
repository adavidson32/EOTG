import sqlite3, time

def get_variables():
    conn = sqlite3.connect('temp.db')
    c = conn.cursor
    c.execute('SELECT * FROM temp_settings')
    select_return = c.fetchone()
    conn.close()
    temp_settings_dict = {'Sensor ID:' select_return[0], 'Sampling Rate': select_return[1], 'Resolution': select_return[2]}
    update_time = time.time()
    return temp_settings_dict, update_time
