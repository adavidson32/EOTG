import os, time

def getCPUtemp():
    file = open('/sys/class/thermal/thermal_zone0/temp','r')
    lines = file.readlines()
    temp_float = float(lines[0])/1000
    temp_str = 'CPU Temp: {.1f}*C'.format(temp_float)
    file.close()
    return temp_float, temp_str


while True:
    temp_f, temp_str = getCPUtemp()
    print(temp_str)
    time.sleep(1)
