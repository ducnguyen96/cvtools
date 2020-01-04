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

def multiple_color_spaces(image):
    RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    LAB = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    cv2.imshow("BGR", image)
    cv2.imshow("RGB", RGB)
    cv2.imshow("HSV", HSV)
    cv2.imshow("LAB", LAB)
    cv2.waitKey(0)
    
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

def color_segment(image, low=(100, 0, 0), high=(255, 255, 255), color_space="RGB", mode=None, show=False):

    transformed = image.copy()

    blured = cv2.medianBlur(transformed, 21)
    mask = cv2.inRange(blured, low, high)
    segmented = cv2.bitwise_and(image, image, mask=mask)
    
    if show == True:
        cv2.imshow("blured", blured)
        cv2.imshow("segmented", segmented)
        cv2.imshow("mask", mask)
        cv2.waitKey(0)

    if mode == "TP":
        cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('mask', 600,600)

        cv2.createTrackbar("space", "mask", 0,3,nothing)

        cv2.createTrackbar("blur", "mask", 10,30,nothing) 
        cv2.createTrackbar("l1", "mask",0,255,nothing)  
        cv2.createTrackbar("l2", "mask",0,255,nothing)      
        cv2.createTrackbar("l3", "mask",0,255,nothing)  
        cv2.createTrackbar("h1", "mask",0,255,nothing)  
        cv2.createTrackbar("h2", "mask",0,255,nothing)      
        cv2.createTrackbar("h3", "mask",0,255,nothing)

        while(1):

            if cv2.waitKey(1) == ord("q"):
                cv2.destroyAllWindows()
            
            space = cv2.getTrackbarPos("space", "mask")

            if space == 1:
                transformed = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            elif space == 2:
                transformed = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            elif space == 3:
                transformed = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

            b=cv2.getTrackbarPos("blur", "mask")
            l1=cv2.getTrackbarPos("l1", "mask")
            l2=cv2.getTrackbarPos("l2", "mask")
            l3=cv2.getTrackbarPos("l3", "mask")
            h1=cv2.getTrackbarPos("h1", "mask")
            h2=cv2.getTrackbarPos("h2", "mask")
            h3=cv2.getTrackbarPos("h3", "mask")

            blured = cv2.medianBlur(transformed, 2*b+1)
            # cv2.imshow("blured", blured)
            mask = cv2.inRange(blured, (l1, l2, l3), (h1, h2, h3))
            cv2.imshow("mask", mask)
            segmented = cv2.bitwise_and(image, image, mask=mask)
            cv2.imshow("segmented", segmented)
    return mask

def padding(image, top=0, left=0, bottom=0, right=0, show=False):
    padded = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT)
    if show == True:
        cv2.imshow("padded", padded)
        cv2.waitKey(0)
    return padded

def draw_houghlines(houghlines, canvas, resize_factor=1):
    if type(houghlines) == type(None):
        return 

    for line in houghlines:
        if len(houghlines.shape) == 3:
            x1,y1,x2,y2 = line[0]
        else:
            x1,y1,x2,y2 = line
        cv2.line(canvas,(x1,y1),(x2,y2),(255,0,0),1)
    canvas = cv2.resize(canvas, (0,0), fx=resize_factor, fy=resize_factor)
    cv2.imshow("houghlines", canvas)
    cv2.waitKey(0)

def detect_houghlines(edges, threshold=70, rho=0.8, minLineLength=400, mode=None, show=False):
    "if you want less lines next to each other : decrease rho"
    "if you want less lines in general : increase threshold"
    houghlines = cv2.HoughLinesP(edges, rho=rho, theta=np.pi/180, threshold=threshold, minLineLength=minLineLength, maxLineGap=10000)
    if show == True:
        canvas = np.zeros_like(edges)
        draw_houghlines(houghlines, canvas)

    if mode == "TP":
        canvas = np.zeros_like(edges)
        cv2.namedWindow("HOUGHLINES", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('HOUGHLINES', 600,600)
        cv2.createTrackbar("threshold", "HOUGHLINES",10,120,nothing)
        cv2.createTrackbar("rho", "HOUGHLINES",1,10,nothing)
        cv2.createTrackbar("minLineLength", "HOUGHLINES",10,500,nothing)

        while(1):
            if cv2.waitKey(1) == ord("q"):
                cv2.destroyAllWindows()

            threshold=cv2.getTrackbarPos("threshold", "HOUGHLINES")
            rho=cv2.getTrackbarPos("rho", "HOUGHLINES")
            minLineLength=cv2.getTrackbarPos("minLineLength", "HOUGHLINES")
            houghlines = cv2.HoughLinesP(edges, rho=rho*0.1, theta=np.pi/180, threshold=threshold, minLineLength=minLineLength, maxLineGap=10000)
            for line in houghlines:
                x1,y1,x2,y2 = line[0]
                cv2.line(canvas,(x1,y1),(x2,y2),(255,0,0),1)
            cv2.imshow("HOUGHLINES", canvas)
            canvas = np.zeros_like(edges)

    return houghlines