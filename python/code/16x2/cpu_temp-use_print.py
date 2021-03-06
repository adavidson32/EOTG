import lcddriver
import time, os

def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
)))

def getCPUtemp():
    file = open('/sys/class/thermal/thermal_zone0/temp','r')
    lines = file.readlines()
    temp_float = float(lines[0])/1000
    temp_str = 'CPU Temp: {:.1f}*C'.format(temp_float)
    file.close()
    return temp_float, temp_str

lcd = lcddriver.lcd()


while True:
    temp_f, temp_str = getCPUtemp()
    use_p = getCPUuse()
    print("CPU Use: ", use_p, " %") 
    print("CPU Temp: ", temp_str)
    str1 = 'CPU Use: ' + use_p + '%  '
    str2 = temp_str
    lcd.lcd_display_string(str1, 1)
    lcd.lcd_display_string(str2, 2)
    time.sleep(0.25)
