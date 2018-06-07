# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread("raw_footage\\3.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Keypoints", im)
cv2.waitKey(0)
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector()

# Detect blobs.
is_v2 = cv2.__version__.startswith("2.")
if is_v2:
    detector = cv2.SimpleBlobDetector()
else:
    detector = cv2.SimpleBlobDetector_create()

keypoints = detector.detect(im)
print(keypoints)
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
