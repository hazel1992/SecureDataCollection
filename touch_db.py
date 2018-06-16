import serial
import RPi.GPIO as GPIO
import time
import sqlite3
from base64 import b64decode

GPIO.setmode(GPIO.BOARD)
ser = serial.Serial('/dev/ttyUSB0', 9600, write_timeout=10)
file_path = '/var/www/html/database/sensordata.db'
padPin = 23
GPIO.setup(padPin, GPIO.IN)

alreadyPressed = False

message = 'Touch'.encode()
#key = RSA.importKey(open('/client/private_key.pem/private_key.pem', 'r').read())


while True:

    padPressed = GPIO.input(padPin)
    if padPressed and not alreadyPressed:
        print(message)
        conn=sqlite3.connect(file_path)
        curs=conn.cursor()
        curs.execute("""INSERT INTO sensordata VALUES(datetime('now'),(?))""",('pressed',))
        conn.commit()
        conn.close()
    alreadyPressed = padPressed
    time.sleep(0.1)
