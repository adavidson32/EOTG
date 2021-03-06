import sys
from eotg_ws import eotg_ws
import httpUpdateWorker
import time
import threading

class StatusUpdateWorker(httpUpdateWorker.HttpUpdateWorker):

    def __init__(self):
        httpUpdateWorker.HttpUpdateWorker.__init__(self)

    def runUpdate(self):
        while(self.stopped != True):
           try:
               print('running status monitor')
               ws = eotg_ws()
               # Get the brew status from the web server and set the brew status in the database
               ws.getCurrentPreset()
               ws.getAllPresets()
               ws.putDeviceStatus()
               # Get how long we should sleep for, then sleep for that long.
               brewCheckPeriod = super().getTiming()
               #print('sleeping for ' + str(brewCheckPeriod) + ' seconds...')
               if brewCheckPeriod > 0:
                   time.sleep(brewCheckPeriod)
               else:
                   # Default to 10 seconds
                   time.sleep(10)
           except Exception as ex:
               print('Exception updating status: ' + str(ex))
               self.stop()
        self.stop()

    def runStatusMonitor(self):
        t1 = threading.Thread(target=self.runUpdate)
        t1.start()
