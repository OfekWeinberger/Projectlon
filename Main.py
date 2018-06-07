import cv2
import keyboard
import YanirGetImage
import getDistance

while (True):
    if keyboard.is_pressed("ENTER"):
        break
img = YanirGetImage.get_image()  # get grey image
grey_img = cv2.colorChange(cv2.COLOR_RGB2GRAY, img)  # convert to grey
cv2.imshow(grey_img)

dis = getDistance.get_distance(grey_img)
print(dis)
