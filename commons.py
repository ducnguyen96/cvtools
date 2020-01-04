import cv2
import numpy as np

def auto_canny(img, sigma=0.33, show=False):
    # compute the median of the single channel pixel intensities
    v = np.median(img)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(img, lower, upper)
    if show == True:
        cv2.imshow("edged", edged)
        cv2.waitKey(0)
    return edged

def convert_to_scan(img):
    # Gray Image
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Scan Image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(9, 9))
    close = cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel)
    div = np.float32(gray)/(close+0.0001)
    res = np.uint8(cv2.normalize(div,div,0,255,cv2.NORM_MINMAX))
    scanned = cv2.cvtColor(res,cv2.COLOR_GRAY2BGR)
    return scanned