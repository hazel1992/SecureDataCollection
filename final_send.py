from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto import Random
import sqlite3
import serial
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

#open serial connection
ser = serial.Serial('/dev/ttyUSB0', 9600, write_timeout=10)

#input from the sensor
padPin = 23
GPIO.setup(padPin, GPIO.IN)

alreadyPressed = False

#directory to the database
file_path = '/var/www/html/database/sensordata.db'

message = 'Touch'.encode()
#path to private key
key = RSA.importKey(open('/client/private_key.pem/private_key.pem', 'r').read())

# an SQL script to implement a trigger in the database
script = ''' CREATE TRIGGER mytrigger
BEFORE INSERT ON sensordata
BEGIN
    SELECT CASE WHEN
        (SELECT COUNT (*) FROM sensordata) >= 3
    THEN
        RAISE(IGNORE)
    END;
END;
'''

while True:

    padPressed = GPIO.input(padPin)
    if padPressed and not alreadyPressed:
        print(message)
		#connects to the database and write data
        conn = sqlite3.connect(file_path)
        curs=conn.cursor()
        curs.execute('''DROP TRIGGER IF EXISTS mytrigger''')
        curs.executescript(script)
        curs.execute('''INSERT INTO sensordata VALUES(datetime('now'),(?))''',('pressed',))
        conn.commit()
        

        #count the rows in the database
        curs.execute('''SELECT COUNT (*) FROM sensordata''')
        rowcount = curs.fetchone()[0]
        print(rowcount)
        conn.close()
        if rowcount == 3:
        # close the database and sign the data and send it

            print('closed')
            digest = SHA.new(message)

            print(digest)
            print(message)
            signer = PKCS1_v1_5.new(key)
            sig = signer.sign(digest)
            ser.flushInput()
            ser.write(sig + '\n'.encode())
        #time.sleep(5)
    alreadyPressed = padPressed
    time.sleep(0.1)
