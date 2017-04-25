import sqlite3

def getProfile():
    conn = sqlite3.connect('../main/eotg.db')
    c = conn.cursor()
    c.execute("SELECT preset_state FROM device_info")
    current_profile_num = c.fetchone()[0]
    c.execute("SELECT * FROM profile_list WHERE prof_num=?", (current_profile_num,))
    current_profile = c.fetchone()
    conn.commit()
    conn.close
    tu_prof = ('prof_num', 'prof_name', 'temp', 'volume', 'color_pattern')
    current_profile_dict = dict(zip(tu_prof, current_profile))
    return current_profile_dict
