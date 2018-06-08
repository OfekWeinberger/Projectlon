# Standard imports
import cv2
import numpy as np

# Read image
from old import MathShit as ms


def get_poly7():
    x = []
    y = [i for i in range(5, 16, 1)]
    for i in range(5, 16, 1):
        str = "fit_experiment2\\" + i.__str__() + ".jpg"
        im = cv2.imread(str, cv2.IMREAD_GRAYSCALE)
        im = cv2.bitwise_not(im)
        cv2.imshow("Keypoints", im)
        cv2.waitKey(0)
        # Set up the detector with default parameters.

        # Setup SimpleBlobDetector parameters.
        params = cv2.SimpleBlobDetector_Params()
        params.minThreshold = 0
        params.maxThreshold = 40

        # Area
        params.filterByArea = True
        params.minArea = 30 - (i - 5) * 2

        # Create a detector with the parameters
        ver = (cv2.__version__).split('.')
        if int(ver[0]) < 3:
            detector = cv2.SimpleBlobDetector(params)
        else:
            detector = cv2.SimpleBlobDetector_create(params)

        cutten_im = im[250:340, 250:390]
        keypoints = detector.detect(cutten_im)
        # cv2.imshow("sdv", cutten_im)
        cv2.waitKey(10000)

        print(len(keypoints))
        left_x = keypoints[0].pt[0]
        left_y = keypoints[0].pt[1]
        right_x = 320
        right_y = 240
        dis = (((left_x - right_x) ** 2 + (left_y - right_y) ** 2) ** 0.5)
        x.append(dis)
        print(dis / 640)
        print(ms.distance_from_wall(left_x, left_y, right_x, right_y, fov=0.885))

        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
        im_with_keypoints = cv2.drawKeypoints(cutten_im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Show keypoints
        cv2.imshow("Keypoints", im_with_keypoints)
        cv2.waitKey(0)


get_poly7()
"""
plt.plot(x, y)
plt.show()
str = np.polyfit(x, y, 7)
func = np.poly1d(str)
genx = np.linspace(min(x), max(x), 10000)
geny = func(genx)
plt.plot(genx, geny)
plt.show()
# plt.plot(x,y) -----plt.show()
"""
