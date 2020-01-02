import cv2
import numpy as np

from commons import rotate

if __name__ == "__main__":
    image = cv2.imread("images/idcard.png")
    cv2.imshow("image", image)
    cv2.waitKey(0)

    # resized = resize_by_size(image, (300, 300), show=True)
    # resized = resize_by_factor(image, 0.5, 0.5, show=True)
    # resized = resize_by_factor(image, 0.5, 0.5, mode="TP")
    rotated = rotate(image, direction="L", show=True)