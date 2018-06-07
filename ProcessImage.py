import numpy as np
import cv2


def mask_handle(mask, frame):
    array_mask = np.array(mask)
    array_frame = np.array(frame)
    sub_frame_array = np.array([np.multiply(array_frame[:, :, 0], array_mask).transpose(), np.multiply(array_frame[:, :, 1], array_mask).transpose(),
                                np.multiply(array_frame[:, :, 2], array_mask).transpose()]).transpose()
    return sub_frame_array


def close_holes(mask):
    kernel = np.ones((5, 5), np.uint8)
    dil = cv2.dilate(src=mask, kernel=kernel, iterations=5)
    erd = cv2.erode(src=dil, kernel=kernel, iterations=5)

    return erd


def blob():
    # Read image
    im = cv2.imread("raw_footage\\1.jpeg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Keypoints", im)
    cv2.waitKey(0)
    # Set up the detector with default parameters.
    detector = cv2.SimpleBlobDetector()

    # Detect blobs.
    keypoints = detector.detect(im)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show keypoints
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)


blob()
