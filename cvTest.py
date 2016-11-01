import cv2
import numpy as np

image = cv2.imread('colorTest.bmp')

#boundaries = ([0, 0, 1], [0, 0, 255]) # R
#boundaries = ([0, 1, 0], [0, 255, 0]) # G
boundaries = ([1, 0, 0], [255, 0, 0]) # B

lower, upper = boundaries
lower = np.array(lower, dtype = "uint8")
upper = np.array(upper, dtype = "uint8")

mask = cv2.inRange(image, lower, upper)

output = cv2.bitwise_and(image, image, mask = mask)

cv2.imshow('image', np.hstack([image, output]))

cv2.waitKey(0)

cv2.destroyAllWindows() 