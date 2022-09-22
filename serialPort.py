import serial
from time import sleep
import sys

num_of_switch="dgs_1210"
port = "/dev/ttyUSB"+str(sys.argv[1])
user=""
password=""

ser = serial.Serial(
	port = port, \
	baudrate =  9600, \
	stopbits = serial.STOPBITS_ONE, \
	bytesize = serial.EIGHTBITS, \
	timeout = .1)

def auth_ser():
	ser.read_until(b"UserName: ")  
	ser.write(user.encode('ascii') + b"\r\n")
	ser.read_until(b"Password: ")
	ser.write(password.encode('ascii') + b"\r\n")#ascii
	print ("au")
	sleep(0.5)
