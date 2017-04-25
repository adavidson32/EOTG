import serial

def sendSerialMsg(msg, serial_port, baud_rate, to):

    ser = serial.Serial(
        port = serial_port,
        baudrate = baud_rate,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = to
    )
    print('writing ' + msg + ' to port ' + str(serial_port))
    ser.write(msg)
