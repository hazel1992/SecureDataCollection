import io
import serial
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from base64 import b64decode

ser = serial.Serial('/dev/ttyUSB0', 9600)

dir = '/client/public_key.pem'



while True:

    signature = ser.readline().strip()
    print(signature)

    if signature:

        message = 'Touch'.encode()
        key = RSA.importKey(open(dir, 'r').read())
        signer = PKCS1_v1_5.new(key)
        digest = SHA.new(message)

        if signer.verify(digest, signature):
            print('good')
        else:
            print(message)
            print(digest)
            print('no')
