# -*- coding: utf-8 -*-
import cv2
import numpy as np

img_path = 'lena_noise.jpg'

src = cv2.imread(img_path)
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

aveBlur1 = cv2.blur(src,(3,3))
aveBlur2 = cv2.blur(src,(5,5))
GaussianBlur1 = cv2.GaussianBlur(src, (3, 3), 0)
GaussianBlur2 = cv2.GaussianBlur(src, (5, 5), 0)

cv2.imshow("origin", src)
cv2.imshow("aveBlur_3", aveBlur1)
cv2.imshow("aveBlur_5", aveBlur2)
cv2.imshow("gaussianBlur_3", GaussianBlur1)
cv2.imshow("gaussianBlur_5", GaussianBlur2)

cv2.waitKey(0)
cv2.destroyAllWindows() 