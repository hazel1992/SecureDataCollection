import serial
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

padPin = 23
GPIO.setup(padPin, GPIO.IN)


alreadyPressed = False

message = 'Touch'.encode()

ser = serial.Serial('/dev/ttyUSB0', 9600, write_timeout=10)

while True:
    padPressed =  GPIO.input(padPin)

    if padPressed and not alreadyPressed:
        print('pressed')
        ser.write(message + '\n'.encode()
    alreadyPressed = padPressed
    time.sleep(0.1)
