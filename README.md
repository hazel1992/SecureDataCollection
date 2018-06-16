# SecureDataCollection
This project secures data transmission through authentication

# Set Up
sudo apt-get install pycrypto

sudo apt-get install sqlite

# Code descriptions

Sender 				Description				Receiver 			Description
Ser_mes_send.py-	Send string via XBee	Ser_mes_receive.py	Receive string via XBee
Touch_sensor.py		Test connection 
					of sensor to the Pi		-					-
Send_touch.py		Sensor is touched 		Receive_touch.py	Data is received via XBee
					and data is sent 
					via XBee					
RSA.py				Generate key pairs 		Receive_rsa.py		Receive public key and save it in  a specified folder location
					and save it to 
					designated folder				
Send_file.py		Send text from a specified folder location	Receive_file.py	Received data and save it in a specified folder location
Sign.py				Sign string and send via XBee	Verify.py	Verify signature from received data
Touch_db.py			Sensor is pressed and data is saved in the database	Touch_db.py	Sensor is pressed and data is saved in the database to test database from the receiver side
Trigger.py			Test the limit implemented to the database and raise an error.	-	-
Final_send.py		Save data, once database trigger is met, sign data and send.	Final_rec.py	Verify signature and save data in the database, raise an error when database limit is reached.
