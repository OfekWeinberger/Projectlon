# Standard imports
import cv2
import numpy as np

# Read image
str = np.load("poly2.npy")
func = np.poly1d(str)
TWO_LAZER_POLY = func
str = np.load("poly1.npy")
func = np.poly1d(str)
ONE_LAZER_POLY = func


def get_distance(img):
    img = cv2.bitwise_not(img)
    # Set up the detector with default parameters.

    # Setup SimgpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()
    params.minThreshold = 0
    params.maxThreshold = 40
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
        cutten_img = img[:-50, 250:360]
        cv2.imshow("m", cutten_img)
        cv2.waitKey(1000)
        print(cutten_img.shape)
        keypoints = detector.detect(cutten_img)
        if (len(keypoints) >= 2):
            break

    # cv2.imshow("sdv", cutten_img)
    if (len(keypoints) == 1):
        print("used one point")
        # cutten_img = img[250:290, 250:310]
        # keypoints = detector.detect(cutten_img)
        my_poly = TWO_LAZER_POLY
        left_x = keypoints[0].pt[0] + 250
        left_y = keypoints[0].pt[1] + 250
        right_x = 309
        right_y = 265
        dis = 2 * (((left_x - right_x) ** 2) + ((left_y - right_y) ** 2)) ** 0.5

    elif len(keypoints) >= 2:
        print("used two points")
        my_poly = TWO_LAZER_POLY
        left_x = keypoints[0].pt[0]
        left_y = keypoints[0].pt[1]
        right_x = keypoints[1].pt[0]
        right_y = keypoints[1].pt[1]
        dis = (((left_x - right_x) ** 2) + ((left_y - right_y) ** 2)) ** 0.5
    else:
        print("didn't find points")
    return my_poly(dis)


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
