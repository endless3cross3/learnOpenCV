# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 11:30:38 2016

@author: Curry
"""

import cv2
import numpy as np
import imutils

imgPath = 'IMAG0070.jpg'
lineLength = 5000

img = cv2.imread(imgPath)

imgO = imutils.resize(img, width=300)  
cv2.imshow("original",imgO)

print(img.shape[:2])

#img = imutils.resize(img, width=1500)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)

gray = cv2.GaussianBlur(gray, (3, 3), 0) # 高斯平滑

gray1 = imutils.resize(gray, width=300)  
cv2.imshow("GaussianBlur",gray1)

edges = cv2.Canny(gray,10,50,apertureSize = 3)

edges1 = imutils.resize(edges, width=300)  
cv2.imshow("Canny",edges1)

lines = cv2.HoughLines(edges,1,np.pi/180,200)
print("Len of lines:",len(lines))
# print lines

rhoList = []
thetaList = []
i = 0
for line in lines:
    rho,theta=line[0]
    print('rho,theta',rho,theta)    
    
#    a = np.cos(theta)
#    b = np.sin(theta)
#    x0 = a*rho
#    y0 = b*rho
#    
#    x1 = int(x0 + lineLength*(-b))
#    y1 = int(y0 + lineLength*(a))
#    x2 = int(x0 - lineLength*(-b))
#    y2 = int(y0 - lineLength*(a))    
    
    degreeThreshold = 1.5
    if theta<np.deg2rad(degreeThreshold) or theta>np.deg2rad(180-degreeThreshold):    
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        
        x1 = int(x0 + lineLength*(-b))
        y1 = int(y0 + lineLength*(a))
        x2 = int(x0 - lineLength*(-b))
        y2 = int(y0 - lineLength*(a))    
            
        print(0,theta)
        rhoList.append(rho)
        thetaList.append(theta)
#        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
#        cv2.putText(img,str(i),(int(x0),int(y0+50*(i+1))), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),1,cv2.LINE_AA)
        i=i+1
    else:
        pass
    
################################################

l1 = []
if len(thetaList) == len(rhoList):
    for i in range(len(thetaList)):
        l1.append((thetaList[i],rhoList[i]))
        
###############

l2 = []
for th, r in l1:
    if th > np.pi/2:
        l2.append((th-np.pi, abs(r)))
    else:
        l2.append((th,r))
        
###################

listSort = sorted(l2 ,key = lambda x: x[1])
lineArray = np.array(listSort)

####################

t = 15
lt = [[]]
lr = [[]]
rho0 = lineArray[0, 1]
j = 0
for theta1, rho1 in lineArray:
#     print('a',i,theta1,rho1)
    if rho1 < rho0 + t:
        lt[j].append(theta1)
        lr[j].append(rho1)
    else: 
        rho0 = rho1
        lt.append([])
        lr.append([])
        j = j+1
        lt[j].append(theta1)
        lr[j].append(rho1)

##################

l3 = []
if len(lt)==len(lr):
    for i in range(len(lt)):
        thetaMean = np.mean(lt[i])
        rhoMean = np.mean(lr[i])
        if thetaMean < 0:
            thetaMean = thetaMean + np.pi
            rhoMean = -rhoMean
        l3.append((thetaMean,rhoMean))        

####################

meanLines=l3

for meanLine in meanLines:
    theta,rho =meanLine
    print(meanLine)
          
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    
    x1 = int(x0 + lineLength*(-b))
    y1 = int(y0 + lineLength*(a))
    x2 = int(x0 - lineLength*(-b))
    y2 = int(y0 - lineLength*(a))  
    
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
   
################################################
    
#rhoArray = np.array(rhoList)    
#thetaArray = np.array(thetaList) 

'''
rhoMean = rhoArray.mean()
thetaMean = thetaArray.mean()
#print(0,rhoMean,thetaMean) 
p1Mean, p2Mean = drawLine(rhoMean, thetaMean, img)
#print(0,p1Mean,p2Mean)
cv2.line(img,p1Mean,p2Mean,(255,0,0),2)
'''

#drawLine(rhoMean, thetaMean, img)

cv2.imwrite('houghlines3.jpg',img)

img = imutils.resize(img, width=300)    
cv2.imshow("houghlines3.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows() 