import os, time

while True:
    file = open('/sys/class/thermal/thermal_zone0/temp','r')
    lines = file.readlines()
    temp = float(lines[0])/1000
    file.close()
    print("CPU Temp: {:.1f}*C".format(temp))
    time.sleep(5)
