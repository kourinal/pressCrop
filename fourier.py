import cv2
import numpy as np
import pylab

def filterOne(width,height):
    x = np.zeros((width, height))

    for i in range(height):
        for j in range(30):
            x[i, int(height/2) + j] = 255
            x[i, int(height / 2) - j] = 255
    cv2.imshow("1", x)
    cv2.waitKey(0)
    return x

def filterTwo(width, height):
    x = np.ones((width, height))

    for i in range(width):
        for j in range(240):
            x[i, int(height/2) + j] = 0
            x[i, int(height / 2) - j] = 0
    cv2.imshow("1", x)
    cv2.waitKey(0)
    return x

def filterThree(width,height):
    x = np.ones((width, height))
    for i in range(height):
        for j in range(150):
            print((height / 2))
            x[int(height / 2) + j, i] = 0
            x[int(height / 2) - j, i] = 0
    cv2.imshow("1", x)
    cv2.waitKey(0)
    return x

image = cv2.imread("fourier/10.tif", 0)
#image = cv2.bitwise_not(image)
'''ftimage = np.fft.fft2(image)
ftimage = np.fft.fftshift(ftimage)
kernel = filterTwo(image.shape[0], image.shape[1])
ftimagep = ftimage * kernel
imagep = np.fft.ifft2(ftimagep)
cv2.imwrite("fourier/test1_150px.tif", np.abs(imagep))

pylab.imshow(np.abs(imagep), cmap='Greys')
pylab.show()'''
j = 8;
for i in range(4):
    print(j)
    image = cv2.imread('fourier/' + str(j) + '.tif', 0)
    ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    '''img2 = cv2.imread('scaled img/' + str(j) + '.tif', 0)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 2))
    erosion = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)
    ret1, thresh21 = cv2.threshold(erosion, 127, 255, cv2.THRESH_BINARY_INV)'''

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (200, 2))
    opening = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)
    cv2.imwrite("fourier/" + str(j) + "_opening.tif", opening)
    cv2.imshow("open", opening)
    cv2.waitKey(0)
    j = j + 1
    opening = cv2.imread("fourier/" + str(j) + "_opening.tif")
    opening = cv2.bitwise_not(opening)
    cv2.imshow('open inverted', opening)
    cv2.waitKey(0)
    ret, thresh = cv2.threshold(opening, 127, 255, 0)
    contours, hierarchy, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    cnt = contours[0]

    '''M = cv2.moments(cnt)
    x, y, w, h = cv2.boundingRect(cnt)'''
    epsilon = 0.1 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    print(approx)
    '''cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("rec",image)'''
    cv2.waitKey(0)