import serial

def sendSerialMsg(msg, serial_port, baud_rate, to):

    ser = serial.Serial(
        port = '/dev/ttyAMA0',
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = 1
    )
    print('writing ' + msg + ' to port ' + str(serial_port))
    ser.write(msg)
