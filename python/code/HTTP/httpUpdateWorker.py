import eotg-ws as ws
import sqlite3
import threading

class HttpUpdateWorker(threading.Thread):
    
    stopped = false
    deviceState = ''
    conn 

    def __init__(self):
        self.conn = sqlite3.connect('eotg.db')
        getDeviceState()

    def run(self):
        return
    
    # Get the device state TODO - how to share this among threads?
    def getDeviceState():
        c = self.conn.cursor()
        self.deviceState = c.execute('select device_state from device_info limit 1;').fetchone()[0]
        c.close()

    # Read timing config item from db
    def getTiming():
        try:
            getDeviceState()
            timing = -1
            sqlStr = 'select * from update_settings limit 1'
            c = self.conn.cursor()
            timingRow = c.execute(sqlStr).fetchone()
            if deviceState == 'background':
                timing = timingRow['freq_background']
            elif deviceState == 'brewing': 
                timing = timingRow['freq_brewing']
            elif deviceState == 'waiting': 
                timing = timingRow['freq_waiting']
            c.close()
            return timing
            
        except Exception as ex:
            print('Exception occured getting timing setting in http worker thread: ' + str(ex))
            return -1

    # Stop the thread at the next run
    def setShouldStop(stop):
        self.stopped = stop
    
    # Exit the thread cleanly
    def stopThread():
        self.conn.close()
