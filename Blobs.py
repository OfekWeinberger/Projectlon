# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread("raw_footage\\4.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Keypoints", im)
cv2.waitKey(0)
# Set up the detector with default parameters.

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Filter by threshold
params.minThreshold = 200
params.maxThreshold = 255

# Filter by Area.
params.filterByArea = True
params.minArea = 0.01

# Filter by color.
params.filterByColor = True
params.blobColor = 255

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)


keypoints = detector.detect(im)
print(keypoints[0].pt)
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
