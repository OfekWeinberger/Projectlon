import cv2
import keyboard
import YanirGetImage
import getDistance
import ArduinoConnect

while (True):
    if keyboard.is_pressed("ENTER"):
        break
ArduinoConnect.laser_on()
img = YanirGetImage.get_image()  # get grey image
grey_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # convert to grey
dis = getDistance.get_distance(grey_img)
print(dis)
