# Standard imports
import cv2
import numpy as np;

# Read image
import MathShit as ms

im = cv2.imread("fit_experiment\\15.jpg", cv2.IMREAD_GRAYSCALE)
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
params.minArea = 10

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)

cutten_im = im[150:400, 150:600]
keypoints = detector.detect(cutten_im)
cv2.waitKey(10000)

print(len(keypoints))
left_x = keypoints[0].pt[0]
left_y = keypoints[0].pt[1]
right_x = keypoints[1].pt[0]
right_y = keypoints[1].pt[1]

print((((left_x - right_x) ** 2 + (left_y - right_y) ** 2) ** 0.5) / 640)
print(ms.distance_from_wall(left_x, left_y, right_x, right_y, fov=0.904))

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(cutten_im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
