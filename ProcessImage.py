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
