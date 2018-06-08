import cv2
import keyboard
import YanirGetImage
import getDistance
import ArduinoConnect
import time

ArduinoConnect.laser_on()
img = YanirGetImage.get_image()
cv2.imshow("show", img)
cv2.waitKey(1000)
cv2.imwrite("fit_experiment4\\" + str(15) + ".jpg", img)
