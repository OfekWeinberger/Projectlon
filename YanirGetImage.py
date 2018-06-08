import cv2
import numpy as np

import ProcessImage as pi


def get_image():
    cap = cv2.VideoCapture(0)
    fgbg = cv2.createBackgroundSubtractorKNN(history=24)
    i = 0
    for i in range(10):
        ret, frame2 = cap.read()
    while (True):
        i += 1
        # Capture frame-by-frame
        ret, frame2 = cap.read()
        frame = frame2[250:340, :]
        # Our operations on the frame come here
        fgmask = fgbg.apply(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        im = pi.mask_handle(fgmask, frame)
        # Display the resulting frame
        im2, contours, hier = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
        biggest_contours = sorted(contour_sizes, key=lambda x: x[0])
        if (len(biggest_contours) > 1):
            contour1 = biggest_contours[-1][1]
            contour1_size = biggest_contours[-1][0]
            if (contour1_size > 40):
                x, y, w, h = cv2.boundingRect(np.concatenate((contour1)))
                if (True):
                    frameArray = np.array(frame)
                    crop_img = frame[y:(int)(y + h), :]
                    cap.release()
                    cv2.destroyAllWindows()
                    return pi.mask_handle(fgmask, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
