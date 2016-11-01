# -*- coding: utf-8 -*-

# USAGE
# python center_of_shape.py --image shapes_and_colors.png

# import the necessary packages
import cv2

# load the image, convert it to grayscale, blur it slightly,
# and threshold it

imgPath = 'shapes_and_colors.png'

image = cv2.imread(imgPath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 轉灰階
blurred = cv2.GaussianBlur(gray, (5, 5), 0) # 高斯平滑

#cv2.imshow("blurred", blurred)
#cv2.waitKey(0)
#cv2.destroyAllWindows() 

thresh = cv2.threshold(src=blurred, thresh=60, maxval=255, type=cv2.THRESH_BINARY)[1] # 二值化

# find contours in the thresholded image
cntsTuple = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 找輪廓
cnts = cntsTuple[1]

# loop over the contours
for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c) # 計算重心
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])

	# draw the contour and center of the shape on the image
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2) # 畫輪廓
	cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1) # 畫重心
	cv2.putText(image, "center", (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

	# show the image
	cv2.imshow("Image", image)
	cv2.waitKey(0)
 
cv2.destroyAllWindows() 