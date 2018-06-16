from Crypto.PublicKey import RSA
from Crypto import Random
import os

#generate random number
random_generator = Random.new().read

new_key = RSA.generate(1024, random_generator)

#export keys as PEM files
public_key = new_key.publickey().exportKey("PEM")
private_key = new_key.exportKey("PEM")

#save private key in directory
print(private_key)
fd = open("/client/private_key.pem/private_key.pem", "wb")
fd.write(private_key)
fd.close()

#save public key in directory
print(public_key)
fd = open("/client/public_key.pem", "wb")
fd.write(public_key)
fd.close()
