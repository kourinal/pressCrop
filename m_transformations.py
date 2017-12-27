import cv2
import numpy as np

img = cv2.imread('img/2 Copy.tif')
hsv = cv2.cvtColor(img, cv2.THRESH_BINARY)

cv2.imshow('binary', hsv)
#lower_red = np.array([30, 150, 50])
#upper_red = np.array([255, 255, 180])

#mask = cv2.inRange(hsv, lower_red, upper_red)
#res = cv2.bitwise_and(img, img, mask=mask)
mask = np.zeros(img.shape, dtype = "uint8")

kernel = np.ones((500, 2))
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

cv2.imshow('Original', img)
cv2.imshow('Opening', opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
