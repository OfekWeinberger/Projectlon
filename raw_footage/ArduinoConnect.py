import serial


def laser_on():
    ser = serial.Serial('/dev/tty.usbserial', 9600)
    ser.write(b"1")


laser_on()
