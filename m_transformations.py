import cv2
import numpy as np
import progressbar


def openIm(img, name):

    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 100))
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
        cv2.imwrite('processed/' + str(j) + '.tif', img)

