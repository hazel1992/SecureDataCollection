import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0)

while True:
    data=ser.readline()
    if data:
        print(data)
        f = open('/client/public_key.pem','a')
        data=str(data)
        f.write(data)
        f.close()
        time.sleep(1)