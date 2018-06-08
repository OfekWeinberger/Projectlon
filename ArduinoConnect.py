import serial
import time



def laser_on():
    ser = serial.Serial("COM7", 9600)
    time.sleep(1.5)
    ser.write(b"1")

