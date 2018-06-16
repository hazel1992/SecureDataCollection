import io
import sqlite3
import serial
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


#open serial port
ser = serial.Serial('/dev/ttyUSB0', 9600)

#directory to the public key
dir = '/client/public_key.pem'

#directory to the database
file_path = '/var/www/html/database/sensordata.db'

#SQL script to create trigger in the database
script = ''' CREATE TRIGGER a
BEFORE INSERT ON sensordata
BEGIN
    SELECT CASE WHEN
        (SELECT COUNT (*) FROM sensordata) >= 3
    THEN
        RAISE(FAIL, "Activated - mytrigger.")
    END;
END;
'''

while True:

    signature = ser.readline().strip()
    print(signature)
    print('connected')
#if data recieved
    if signature:

#initiating secret message
        message = 'Touch'.encode()
#open key file
        key = RSA.importKey(open(dir, 'r').read())
        signer = PKCS1_v1_5.new(key)
        digest = SHA.new(message)

		#if passed verification, open database and store data
        if signer.verify(digest, signature):
            print('Verified')
            conn = sqlite3.connect(file_path)
            curs=conn.cursor()
            curs.execute('''DROP TRIGGER IF EXISTS a''')
            curs.executescript(script)
            curs.execute('''INSERT INTO sensordata VALUES(datetime('now'),(?))''',('pressed',))
            conn.commit()
            conn.close()
        else:
            print(message)
            print(digest)
            print('Error: Message not verified')
