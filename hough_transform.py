
import cv2
import numpy as np

"""img = cv2.imread('largest connected/1.tif')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(gray,50,150,apertureSize = 3)
height, width, channels = img.shape
minLineLength = height*0.1
maxLineGap = 150
lines = cv2.HoughLinesP(gray,1 , np.pi/90, 100, minLineLength, maxLineGap)
for x1, y1, x2, y2 in lines[0]:
    cv2.line(img, (x1, y1), (x2, y2), (255,0,0), 10)

cv2.imshow('hough', img)
cv2.waitKey(0)"""


img = cv2.imread('largest connected/67.tif')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#edges = cv2.Canny(gray,200,500,apertureSize = 7)
height, width, channels = img.shape
cv2.imshow('edges', gray)

lines = cv2.HoughLines(gray, 1, np.pi/180, 5)
i = 0
for rho,theta in lines[0]:
    print(i)
    i+=1
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('hough', img)
cv2.waitKey(0)