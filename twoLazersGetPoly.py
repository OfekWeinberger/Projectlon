# Standard imports
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Read image
from old import MathShit as ms


def get_poly7():
    x = []
    y = [i / 3.0 for i in range(15, 46, 1)]
    for i in range(1, 32, 1):
        k = i / 3
        str = "fit_experiment4\\img (" + (i).__str__() + ").jpg"
        im = cv2.imread(str, cv2.IMREAD_GRAYSCALE)
        im = cv2.bitwise_not(im)
        cv2.imshow("Keypoints", im)
        cv2.waitKey(0)
        # Set up the detector with default parameters.

        # Setup SimpleBlobDetector parameters.
        params = cv2.SimpleBlobDetector_Params()
        params.minThreshold = 0
        params.maxThreshold = 180

        # Area
        params.filterByArea = True
        for j in range(1, 30, 1):
            params.minArea = 30 - j

            # Create a detector with the parameters
            ver = (cv2.__version__).split('.')
            if int(ver[0]) < 3:
                detector = cv2.SimpleBlobDetector(params)
            else:
                detector = cv2.SimpleBlobDetector_create(params)

            cutten_im = im[250:330 - i, 240:380]
            keypoints = detector.detect(cutten_im)
            if (len(keypoints) >= 2):
                break
            if (j == 29):
                print(29292929299229)
        cv2.imshow("sdv", cutten_im)
        # cv2.waitKey(10000)

        left_x = keypoints[0].pt[0]
        left_y = keypoints[0].pt[1]
        right_x = keypoints[1].pt[0]
        right_y = keypoints[1].pt[1]
        print((left_x + 250 + right_x + 250) / 2)
        print((left_y + 240 + right_y + 240) / 2)

        dis = (((left_x - right_x) ** 2 + (left_y - right_y) ** 2) ** 0.5)
        x.append(dis)

        # Draw detected blobs as red circles.
        # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
        im_with_keypoints = cv2.drawKeypoints(cutten_im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Show keypoints
        cv2.imshow("Keypoints", im_with_keypoints)
        cv2.waitKey()

    str = np.polyfit(x, y, 5)
    np.save("poly2", str)
    func = np.poly1d(str)
    # plt.plot(x, y)
    #plt.show()
    str = np.polyfit(x, y, 7)
    func = np.poly1d(str)
    genx = np.linspace(min(x), max(x), 10000)
    geny = func(genx)
    plt.plot(genx, geny)
    plt.show()
    # plt.plot(x,y) -----plt.show()
    return func


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
