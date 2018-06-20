import cv2
import numpy as np


def skeletize(img):
    #img = cv2.imread("largest connected/67.tif", 0)
    size = np.size(img)
    skel = np.zeros(img.shape, np.uint8)

    ret, img = cv2.threshold(img, 127, 255, 0)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))#3X3 cross kernel
    done = False
    #main loop foe the function, reduces the image untill only the morphologicak skeleton remains
    while(not done):
        eroded = cv2.erode(img, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(img, temp)
        skel = cv2.bitwise_or(skel, temp)
        img = eroded.copy()

        zeros = size - cv2.countNonZero(img)
        if zeros == size:
            done = True

    return skel
for i in range(1, 95):
    img = cv2.imread("largest connected scaled/" + str(i) + ".tif", 0)
    cv2.imshow(str(i),img)
    cv2.imwrite("skeletonized scaled/" + str(i) + ".tif", skeletize(img))

