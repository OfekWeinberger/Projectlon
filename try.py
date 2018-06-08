import cv2
import keyboard
import YanirGetImage
import getDistance
import ArduinoConnect
import time

for i in range(100):
    while (True):
        if keyboard.is_pressed("ENTER"):
            break
    ArduinoConnect.laser_on()
    img = YanirGetImage.get_image()
    cv2.imwrite("fit_experiment4\\" + str(i) + ".jpg", img)
