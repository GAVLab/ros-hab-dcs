#RPi Pinouts

#I2C Pins 
#GPIO2 -> SDA
#GPIO3 -> SCL

#Import the Library Requreid 
import smbus2 as smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
#Slave Address 1
address = 0x04
data = []
str1 = ""

while True:
	#Receives the data from the User
    raw_data = bus.read_byte_data(address,0x00,1)
    if raw_data > 32:
        data.append(chr(raw_data))
    if (raw_data == 2 or raw_data == 3) and len(data)>1:
        print(str1.join(data))
        data = []

