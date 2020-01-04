import cv2
import numpy as np

from commons import color_segment

def nothing():
    pass

if __name__ == "__main__":
    image = cv2.imread("images/idcard.png")
    image = cv2.resize(image, (640, 480))
    # cv2.imshow("image", image)
    # cv2.waitKey(0)

    # resized = resize_by_size(image, (300, 300), show=True)
    # resized = resize_by_factor(image, 0.5, 0.5, show=True)
    # resized = resize_by_factor(image, 0.5, 0.5, mode="TP")
    # rotated = rotate_by_direction(image, direction="L", show=True)
    # rotated = rotate_by_angle(image, 3, mode="TP")
    # rotated = rotate_remain_bound(image, -3, mode="TP")

    color_segment(image, mode="TP")