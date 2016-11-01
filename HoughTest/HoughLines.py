#-*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-25 上午11:42
"""

#from IPython import get_ipython
#get_ipython().magic('reset -sf')


import cv2
import numpy as np
import imutils

#def drawLine(rho, theta, img):
#    degreeThreshold = 10
#    if theta<np.deg2rad(degreeThreshold) or theta>np.deg2rad(180-degreeThreshold):
#        print('Threshold',theta)
##    print(theta)
#        a = np.cos(theta) # v
#        b = np.sin(theta) # => 單位向量的概念
#        x0 = a*rho
#        y0 = b*rho
#        x1 = int(x0 + 1000*(-b)) # v
#        y1 = int(y0 + 1000*(a))  # => 用正交向量的概念畫直線的兩端點
#        x2 = int(x0 - 1000*(-b))
#        y2 = int(y0 - 1000*(a))
#        return ((x1,y1),(x2,y2))
#    else:
#        return ((-1,-1),(-1,-1))
    

imgPath = 'IMAG0068.jpg'
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

iList =range(len(rhoList))
rhoAbs = [abs(number) for number in rhoList]
lineArray = np.array([iList,thetaList,rhoList,rhoAbs]).T
lineSort=lineArray[lineArray[:,3].argsort()] #排序

################

t = 15
l1 = [[]]
l2 =[[]]
rho0 = lineSort[0][3]
j=0
for i in iList:
    if lineSort[i][3] < rho0 + t:
#         l1[j].append(lineSort[i][3])
        l2[j].append(lineSort[i][0])
    else:
        j=j+1
#         l1.append([])
        l2.append([])
        rho0 = lineSort[i][3]
#         l1[j].append(lineSort[i][3])
        l2[j].append(lineSort[i][0])
#         print(lineSort[i][3])

# l1
#l2

################

l3=[]
l31 = []
l4=[]
l41=[]
for ll2 in l2:
    for i in ll2:
        l3.append(lineArray[int(i)][2])
        l31.append(lineArray[int(i)][1])
#         l3.append(i)
    l4.append(l3)
    l41.append(l31)
    l3 = None
    l31=None
    l3 =[]
    l31=[]
l4,l41

#####################
                   
l5=[]
l51=[]
for i in l4:
    l5.append(np.mean(i))
for i in l41:
    l51.append(np.mean(i))
l5,l51

####################

meanLines=np.array([l5 ,l51]).T

for meanLine in meanLines:
    rho,theta=meanLine
          
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