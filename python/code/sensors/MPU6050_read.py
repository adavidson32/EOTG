from mpu6050 import mpu6050
import time

mpu6050 = mpu6050(0x68)
return_type = input("Return Type: (all, accel, gyro, temp, etc.) ")
units = input("Temperature Units (c or f): ")
while not((units=='c') or (units=='f')):
    units = input("Invalid unit type entered. Please type 'c' or 'f' (without '') : ")

def update_accel_gyro(return_type):
    all_data = mpu6050.get_all_data()
    accel = all_data[0]
    gyro = all_data[1]
    temp_c = float('{0:.2f}'.format(all_data[2]))
    temp_f = float('{0:.2f}'.format((all_data[2])*1.800 + 32.000))
    ax = float('{0:.3f}'.format(accel['x']))
    ay = float('{0:.3f}'.format(accel['y']))
    az = float('{0:.3f}'.format(accel['z']))
    gx = float('{0:.3f}'.format(gyro['x']))
    gy = float('{0:.3f}'.format(gyro['y']))
    gz = float('{0:.3f}'.format(gyro['z']))
    if (return_type=='accel' or return_type=='all'):
       print('Accelerometer x({0}), y({1}), z({2))'.format(ax, ay, az))
    if (return_type=='gyro' or return_type=='all'):
        print('Gyrometer (x:{0:.3f}, y:{1:.3f}, z:{2:.3f})'.format(gx, gy, gz))
    if (return_type=='temp' or return_type=='accel' or return_type=='gyro' or return_type=='all'):
        if units=='c':
            print('Temp: {0} Celcius' % temp_c)
        elif units=='f':
            print('Temp: {0} Fahrenheit' % temp_f)
    else:
        print("Invalid input argument, use (all, accel, gyro, temp, temp_c, or temp_f")

print('Starting to run while loop: ')
i = 1
while True:
    print("Running while loop iteration #{0}".format(i))
    update_accel_gyro(return_type)
    time.sleep(10)
    i+=1
