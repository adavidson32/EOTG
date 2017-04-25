import sys
from eotg_ws import eotg_ws
import httpUpdateWorker
import time

class BrewUpdateWorker(httpUpdateWorker.HttpUpdateWorker):

    def __init__(self):
        httpUpdateWorker.HttpUpdateWorker.__init__(self)

    def runBrewMonitor(self):
        # Run the brew monitor
        while(self.stopped != True):
            try:
                # Get the brew status from the web server and set the brew status in the database
                #print('Checking if we should brew.')
                eotg_ws.shouldBrew()
                # Get how long we should sleep for, then sleep for that long.
                brewCheckPeriod = 10 #super().getTiming()
                if brewCheckPeriod > 0:
                    time.sleep(brewCheckPeriod)
                else:
                    # Default to 10 seconds
                    time.sleep(10)
            except Exception as ex:
                print('Error getting brew enable: ' + str(ex))
                self.stop()
        self.stop()
