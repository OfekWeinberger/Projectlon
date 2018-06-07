import cv2
import numpy as np

import ProcessImage as pi


def get_image():
    cap = cv2.VideoCapture(0)
    fgbg = cv2.createBackgroundSubtractorKNN(history=24)
    i = 0
    while (True):
        i += 1
        # Capture frame-by-frame
        ret, frame = cap.read()
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
            contour2 = biggest_contours[-2][1]
            contour1_size = biggest_contours[-1][0]
            contour2_size = biggest_contours[-2][0]
            if (contour1_size > 50 and contour2_size > 50):
                print(contour1_size, contour2_size)
                x, y, w, h = cv2.boundingRect(np.concatenate((contour1, contour2)))
                if (2 < h < 80 and 10 < w < 150 and i > 0):
                    frameArray = np.array(frame)
                    crop_img = frame[y:(int)(y + h), x:x + w]
                    cap.release()
                    cv2.destroyAllWindows()
                    return frame

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
