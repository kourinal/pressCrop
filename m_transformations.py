import cv2
import numpy as np
import progressbar


def openIm(img, name):

    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    img2 = cv2.imread('scaled img/2.tif', 0)
    #cv2.imshow('s', img2)
    #cv2.waitKey(0)
    #gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    #kernel = np.ones((5, 5), np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 20))
    erosion = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)
    ret1, thresh21 = cv2.threshold(erosion, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite('eroded/2.tif' ,thresh21)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 20))

    #kernel = np.ones((200, 5), np.uint8)
    opening = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)
    return opening


def transform(path):
    j = 0
    bar = progressbar.ProgressBar(max_value=95)
    for i in path:
        bar.update(j)
        print(i)
        img = openIm(cv2.imread(str(i)), j)
        j += 1
        constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(255, 255, 255))
        cv2.imwrite('processed scaled erosion/' + str(j) + '.tif', constant)

