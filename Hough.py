# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:34:10 2016

@author: UNO
"""

import cv2
import numpy as np

def main():
    imgPath = 'houghline_1.jpg'
    image = cv2.imread(imgPath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 轉灰階
    lines = calcLines(img)
    pass

def calcLines(img):
    contours = cv2.Canny(img,50,150,apertureSize = 3)
    lines = cv2.HoughLines(contours,1,np.pi/180,50)
    # cv2.HoughLines(image, rho, theta, threshold[, lines[, srn[, stn]]]) → lines
    return lines
    
    
    
    
def drawLines(img):
    pass