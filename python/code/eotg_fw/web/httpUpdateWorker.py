import sqlite3

class HttpUpdateWorker(object):

    def __init__(self):
        self.conn = sqlite3.connect('eotg.db')
        self.stopped = False
        self.deviceState = ''
        self.getDeviceState()

    def getDeviceState(self):
        c = self.conn.cursor()
        self.deviceState = 'waiting' #c.execute('select device_state from device_info limit 1;').fetchone()[0]
        c.close()

    # Read timing config item from db
    def getTiming(self):
        try:
            self.getDeviceState()
            timing = -1
            sqlStr = 'select * from update_settings limit 1'
            c = self.conn.cursor()
            timingRow = c.execute(sqlStr).fetchone()
            if self.deviceState == 'background':
                timing = timingRow['freq_background']
            elif self.deviceState == 'brewing':
                timing = timingRow['freq_brewing']
            elif self.deviceState == 'waiting':
                timing = timingRow['freq_waiting']
            #c.close()
            return timing

        except Exception as ex:
            print('Exception occured getting timing setting in http worker thread: ' + str(ex))
            return -1

    # Stop the thread at the next run
    def setShouldStop(self, stop):
        self.stopped = stop

    # Exit the thread cleanly
    def stop(self):
        self.setShouldStop(True)
        self.conn.close()
