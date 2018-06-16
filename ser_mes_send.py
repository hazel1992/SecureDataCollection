import serial

#enable  comm
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=.5)

while True:
    #serialdata = 'hellos user \r\n'
    ser.write('hello user \r\n'.encode())
    #print()
    tt = ser.readline().strip().decode()
    print(tt)
    print('received data: ' + tt)