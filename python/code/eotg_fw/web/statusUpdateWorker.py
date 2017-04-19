import eotg-ws as ws
import httpUpdateWorker
import time

class StatusUpdateWorker(httpUpdateWorker.HttpUpdateWorker):

    def run(self):
        # Run the brew monitor
        while(!self.stopped):
           try: 
               # Get the brew status from the web server and set the brew status in the database
               ws.getCurrentPreset()
               ws.getAllPresets()
               ws.getBrewSettings()
               ws.putDeviceStatus()
               # Get how long we should sleep for, then sleep for that long.
               brewCheckPeriod = self.getTiming()
               if brewCheckPeriod > 0:
                   time.sleep(brewCheckPeriod * 1000)
               else:
                   # Default to 10 seconds
                   time.sleep(10000)
           except Exception as ex:
               print('Exception updating status: + ' str(ex))
        
        self.stop()

