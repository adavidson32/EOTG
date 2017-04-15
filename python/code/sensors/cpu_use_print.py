import os, time

def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
)))

while True:
    print("CPU Use: ", getCPUuse(), "%")
    time.sleep(1)
    
