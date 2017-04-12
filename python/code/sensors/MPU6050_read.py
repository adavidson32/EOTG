from mpu6050 import mpu6050
import time

mpu6050 = mpu6050(0x68)
return_type = input("Return Type: (all, accel, gyro, temp, etc.) ")

def update_accel_gyro(return_type):
    all_data = mpu6050.get_all_data()
    accel = all_data[0]
    gyro = all_data[1]
    temp_c = all_data[2]
    temp_f = ((temp_c)*1.800 + 32.000)
    ax = accel['x']
    ay = accel['y']
    az = accel['z']
    gx = gyro['x']
    gy = gyro['y']
    gz = gyro['z']
    if return_type=='all':
        print('Accelerometer (x:{0:.3f}, y:{1:.3f}, z:{2:.3f})'.format(ax, ay, az))
        print('Gyrometer (x:{0:.3f}, y:{1:.3f}, z:{2:.3f})'.format(gx, gy, gz))
        print('Temp(C): {0:.2f},  Temp(F): {1:.2f}'.format(temp_c, temp_f))
    elif return_type=='accel':
        print('Accelerometer (x:{0:.3f}, y:{1:.3f}, z:{2:.3f})'.format(ax, ay, az))
    elif return_type=='gyro':
        print('Gyrometer (x:{0:.3f}, y:{1:.3f}, z:{2:.3f})'.format(gx, gy, gz))
    elif return_type=='temp':
        print('Temp(C): {0:.2f},  Temp(F): {1:.2f}'.format(temp_c, temp_f))
    elif return_type=='temp_c':
        print('Temp(C): {0:.2f}'.format(temp_c))
    elif return_type=='temp_f':
        print('Temp(F): {0:.2f}'.format(temp_f))
    else:
        print("Invalid input argument, use (all, accel, gyro, temp, temp_c, or temp_f")

print('Starting to run while loop: ')
i = 1
while True:
    print("Running while loop iteration #{0}".format(i))
    update_accel_gyro(return_type)
    time.sleep(10)
    i+=1
