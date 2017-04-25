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
               print('NPM NPM 0')
               ws = eotg_ws()
               print('NPM NPM 1')
               # Get the brew status from the web server and set the brew status in the database
               ws.getCurrentPreset()
               print('NPM NPM 2')
               ws.getAllPresets()
               print('NPM NPM 3')
               ws.putDeviceStatus()
               print('NPM NPM 4')
               # Get how long we should sleep for, then sleep for that long.
               brewCheckPeriod = 10 #super().getTiming()
               print('NPM NPM 5')
               #print('sleeping for ' + str(brewCheckPeriod) + ' seconds...')
               if brewCheckPeriod > 0:
                   print('NPM NPM 5.5')
                   time.sleep(brewCheckPeriod)
                   print('NPM NPM 5.6')
               else:
                   # Default to 10 seconds
                   print('NPM NPM 6')
                   time.sleep(10)
           except Exception as ex:
               print('Exception updating status: ' + str(ex))
               self.stop()
        self.stop()

    def runStatusMonitor(self):
        t1 = threading.Thread(target=self.runUpdate)
        t1.start()
        #t1.join()
