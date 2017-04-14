import os, time

while True:
    file = open('/sys/class/thermal/thermal_zone0/temp','r')
    lines = file.readlines()
    temp += ';' + str(float(lines[0])/1000)
    file.close()
    print(temp)
    time.sleep(5)
