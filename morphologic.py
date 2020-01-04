import cv2
import numpy as np

def nothing():
    pass

def erode(edges, kernel=(1, 1), iters=1, mode=None, show=False):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel)
    erosion = cv2.erode(edges, kernel, iterations=iters)
    # dilation = cv2.dilate(edges, kernel, iterations=iters)

    if show == True:
        cv2.imshow("ersion", erosion)
        cv2.waitKey(0)
    if mode == "TP":
        cv2.namedWindow("EROSION", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('EROSION', 600,600)
        cv2.createTrackbar("kernel-a", "EROSION",1,20,nothing)
        cv2.createTrackbar("kernel-b", "EROSION",1,20,nothing)
        cv2.createTrackbar("iters", "EROSION",1,10,nothing)

        while(1):
            if cv2.waitKey(1) == ord("q"):
                cv2.destroyAllWindows()

            kernel_a=cv2.getTrackbarPos("kernel-a", "EROSION")
            kernel_b=cv2.getTrackbarPos("kernel-b", "EROSION")
            iters=cv2.getTrackbarPos("iters", "EROSION")
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_a, kernel_b))
            erosion = cv2.erode(edges, kernel, iterations=iters)

            cv2.imshow("EROSION", erosion)
    return erosion
