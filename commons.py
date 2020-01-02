import cv2
import numpy as np

def nothing():
    pass

def resize_by_size(image, size, mode=None, show=False):
    resized = cv2.resize(image, size)
    if show == True:
        cv2.imshow("resize_by_size", resized)
        cv2.waitKey(0)
    if mode=="TP":
        cv2.namedWindow("SIZE", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('SIZE', 400,0)
        cv2.createTrackbar("VERT_SIZE", "SIZE",10,1280,nothing)
        cv2.createTrackbar("HORIZ_SIZE", "SIZE",10,1280,nothing)

        while(1):
            if cv2.waitKey(1) == ord("q"):
                cv2.destroyAllWindows()

            vert_size=cv2.getTrackbarPos("VERT_SIZE", "SIZE")
            horiz_size=cv2.getTrackbarPos("HORIZ_SIZE", "SIZE")

            resized = cv2.resize(image, (horiz_size, vert_size))
            cv2.imshow("resize_by_size", resized)
    return resized