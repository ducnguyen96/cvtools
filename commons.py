import cv2
import numpy as np

def nothing():
    pass

def resize_by_size(image, size, mode=None, show=False):
    # size is a tuple, (300, 300) for example.
    resized = cv2.resize(image, size)
    if show == True:
        cv2.imshow("resize_by_size", resized)
        cv2.waitKey(0)
    if mode == "TP":
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

def resize_by_factor(image, fx, fy, mode=None, show=False):
    # fx and fy can be float.
    # because trackbar have to be int number so I have to set fx,fy equal to 1/100 of their original value in TP mode.
    resized = cv2.resize(image, (0, 0), fx=fx, fy=fy)
    if show == True:
        cv2.imshow("resize_by_factor", resized)
        cv2.waitKey(0)
    if mode == "TP":
        cv2.namedWindow("FACTOR", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('FACTOR', 400,0)
        cv2.createTrackbar("FX", "FACTOR",100,200,nothing)
        cv2.createTrackbar("FY", "FACTOR",100,200,nothing)

        while(1):
            if cv2.waitKey(1) == ord("q"):
                cv2.destroyAllWindows()

            fx=cv2.getTrackbarPos("FX", "FACTOR")
            fy=cv2.getTrackbarPos("FY", "FACTOR")

            resized = cv2.resize(image, (0, 0), fx=fx*0.01, fy=fy*0.01)
            cv2.imshow("resize_by_factor", resized)
    return resized

def rotate_by_direction(image, direction, show=False):
    # Rotate to the right 90.
    if direction == "R":
        rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    # Rotate to the left 90.
    if direction == "L":
        rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # Rotate upside down.
    if direction == "UD":
        rotated = cv2.rotate(image, cv2.ROTATE_180)
        
    if show == True:
        cv2.imshow("rotate", rotated)
        cv2.waitKey(0)
    return rotated

def rotate_remain_bound(image, angle, mode=None, show=False):
    # grab the dimensions of the image and then determine the center
    (h, w) = image.shape[:2]
    (cX, cY) = (w / 2, h / 2)

    # grab the rotation matrix (applying the negative of the angle to rotate clockwise), then grab the sine and cosine
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    rotated = cv2.warpAffine(image, M, (nW, nH))

    if show == True:
        cv2.imshow("rotate_remain_bound", rotated)
        cv2.waitKey(0)

    if mode == "TP":
        cv2.namedWindow("ANGLE", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('ANGLE', 400,0)
        cv2.createTrackbar("angle", "ANGLE",0,360,nothing)

        while(1):
            if cv2.waitKey(1) == ord("q"):
                cv2.destroyAllWindows()

            angle=cv2.getTrackbarPos("angle", "ANGLE")
            M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
            cos = np.abs(M[0, 0])
            sin = np.abs(M[0, 1])
            nW = int((h * sin) + (w * cos))
            nH = int((h * cos) + (w * sin))
            M[0, 2] += (nW / 2) - cX
            M[1, 2] += (nH / 2) - cY

            # perform the actual rotation and return the image
            rotated = cv2.warpAffine(image, M, (nW, nH))
            cv2.imshow("rotate_remain_bound", rotated)

    return rotated

def rotate_by_angle(image, angle, mode=None, show=False):
    # grab the dimensions of the image
    (h, w) = image.shape[:2]

    center = (w // 2, h // 2)

    # perform the rotation
    M = cv2.getRotationMatrix2D(center, -angle, 1)
    rotated = cv2.warpAffine(image, M, (w, h))

    if show == True:
        cv2.imshow("rotate_by_angle", rotated)
        cv2.waitKey(0)
    
    if mode == "TP":
        cv2.namedWindow("ANGLE", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('ANGLE', 400,0)
        cv2.createTrackbar("angle", "ANGLE",0,360,nothing)

        while(1):
            if cv2.waitKey(1) == ord("q"):
                cv2.destroyAllWindows()

            angle=cv2.getTrackbarPos("angle", "ANGLE")
            M = cv2.getRotationMatrix2D(center, -angle, 1)
            rotated = cv2.warpAffine(image, M, (w, h))

            cv2.imshow("rotate_by_angle", rotated)

    return rotated