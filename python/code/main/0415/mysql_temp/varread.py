import sqlite3
import time, os

def get_variables():
    con = sqlite3.connect('eotg.db')
    c = con.cursor()
    c.execute('select * from temp_vals')
    r = c.fetchone()
    
