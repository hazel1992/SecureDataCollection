from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto import Random
import serial
import time
from base64 import b64decode

ser = serial.Serial('/dev/ttyUSB0', 9600, write_timeout=10)


message = 'Touch'.encode()
key = RSA.importKey(open('/client/private_key.pem/private_key.pem', 'r').read())


while True:

    digest = SHA.new(message)

    print(digest)
    print(message)
    signer = PKCS1_v1_5.new(key)
    sig = signer.sign(digest)
    ser.flushInput()
    ser.write(sig + '\n'.encode())
    time.sleep(5)
