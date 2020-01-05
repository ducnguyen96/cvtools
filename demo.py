import cv2
import numpy as np

from tools import color_segment, padding, detect_houghlines
from tools import resize_by_size, resize_by_factor, rotate_by_angle, rotate_remain_bound
from tools import perspective_transform
from commons import auto_canny

from morphologic import erode

if __name__ == "__main__":
    image = cv2.imread("images/idcard2.jpg")
    # image = cv2.resize(image, (320, 240))
    # cv2.imshow("image", image)
    # cv2.waitKey(0)

    # resized = resize_by_size(image, mode="TP")
    # resized = resize_by_factor(image, mode="TP")
    # rotated = rotate_by_direction(image, direction="L", show=True)
    # rotated = rotate_by_angle(image, mode="TP")
    # rotated = rotate_remain_bound(image, mode="TP")

    # mask = color_segment(image, show=True)
    mask = color_segment(image)
    padded = padding(mask, 10, 10, 10, 10, show=False)
    edges = auto_canny(padded, show=True)

    detect_houghlines(edges, mode="TP")

    # erode(edges, mode="TP")
    # coords = [422, 127, 584, 180, 408, 204, 579, 271]
    # perspective_transform(image, coords, show=True)
