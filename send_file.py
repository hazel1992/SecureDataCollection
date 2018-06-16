import serial

#enable  comm
ser = serial.Serial('/dev/ttyUSB0',9600,timeout=2)
#ser.port='/dev/ttyUSB0'
#ser.baudrate=9600
#ser.parity = serial.PARITY_NONE
#ser.stopbits=serial.STOPBITS_ONE
#ser.bytesize = serial.EIGHTBITS
#ser.timeout=2

dir = '/client/public_key.pem'
#[line.rstrip('\n') for line in f
while True:
    #serialdata = 'hellos user \r\n'
    with open(dir, 'r') as f:
        mylist = [f]
        readfile = f.read()
        print(readfile)
        #if ser.isOpen():
        ser.write(readfile.encode())
    #print()
        tt = ser.readline().strip().decode('utf-8')
        print(tt)
        print('received data: ' + tt)