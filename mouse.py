import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), 2, (0, 0, 255), 2)
        cv2.imshow('image', image)
        coords.append(x)
        coords.append(y)

image = cv2.imread('images/idcard2.jpg')
cv2.imshow("image", image)

coords = []
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)

print(coords)

coordx1, coordy1, coordx2, coordy2, coordx3, coordy3, coordx4, coordy4 = coords

pts1 = np.float32([[coordx1, coordy1], [coordx2, coordy2], [coordx3, coordy3], [coordx4, coordy4]])
pts2 = np.float32([[0, 0], [coordx2-coordx1, 0], [0, coordy3-coordy1], [coordx2-coordx1, coordy3-coordy1]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(image, matrix, (coordx2-coordx1, coordy3-coordy1))

result = cv2.resize(result, (0, 0), fx=2, fy=2)

cv2.imshow("result", result)
cv2.waitKey(0)