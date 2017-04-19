import threading
import brewUpdateWorker
import statusUpdateWorker

class HttpWorkerManager(threading.Thread):
    
    def run(self):
        # Run the brew monitor
        brewUpdateWorker = BrewUpdateWorker()
        brewUpdateWorer.start()
        # Run the status uploader/checker
        statusUpdateWorker = StatusUpdateWorker()
        statusUpdateWorker.start()

