import cv2
import numpy as np

def openIm (img, name):
    #img = cv2.imread('img/2 Copy.tif')
    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    #lower_red = np.array([30, 150, 50])
    #upper_red = np.array([255, 255, 180])

    #mask = cv2.inRange(hsv, lower_red, upper_red)
    #res = cv2.bitwise_and(img, img, mask=mask)
    #mask = np.zeros(img.shape, dtype="uint8")

    kernel = np.ones((250, 1), np.uint8)
    opening = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)

    #cv2.imshow('Original', img)
    #cv2.imshow('Opening', opening)
    return opening
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

for i in range(16):
    print(i)
    img =openIm(cv2.imread('img/' + str(i) + '.tif'), str(i))
    cv2.imshow(str(i),img)
    cv2.waitKey(0)
cv2.destroyAllWindows()

