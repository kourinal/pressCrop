
from imutils import contours
from skimage import measure
import numpy as np
import imutils
import cv2


def connected(image):
    #image = cv2.imread("processed/2.tif")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    # threshold the image to reveal light regions in the
    # blurred image
    #thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
    # perform a series of erosions and dilations to remove
    # any small blobs of noise from the thresholded image
    #thresh = cv2.erode(thresh, None, iterations=2)

    #thresh = cv2.dilate(thresh, None, iterations=5)
    # perform a connected component analysis on the thresholded
    # image, then initialize a mask to store only the "large"
    # components
    labels = measure.label(gray, neighbors=8, background=0)
    mask = np.zeros(gray.shape, dtype="uint8")
    height, width, channels = image.shape
    # loop over the unique components
    for label in np.unique(labels):
        # if this is the background label, ignore it
        if label == 0:
            continue

        # otherwise, construct the label mask and count the
        # number of pixels
        labelMask = np.zeros(gray.shape, dtype="uint8")
        labelMask[labels == label] = 255
        numPixels = cv2.countNonZero(labelMask)

        # if the number of pixels in the component is sufficiently
        # large, then add it to our mask of "large blobs"

        if numPixels > 200:
            mask = cv2.add(mask, labelMask)

    # find the contours in the mask, then sort them from left to
    # right
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cnts = contours.sort_contours(cnts)[0]

    # loop over the contours
    for (i, c) in enumerate(cnts):
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(img, [box], 0, (0, 0, 255), 20)

        # draw the bright spot on the image
        (x, y, w, h) = cv2.boundingRect(c)
        #cv2.imshow("rec", img)
        #cv2.waitKey(0)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        ((cX, cY), radius) = cv2.minEnclosingCircle(c)
        if height/2 > radius >= height*0.25:
            cv2.circle(image, (int(cX), int(cY)), int(radius),
                       (0, 0, 255), 3)
            cv2.putText(image, "#{}".format(i + 1), (x, y - 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            cv2.line(image, (int(cX), 0), (int(cX), height), (255, 0, 0), 5)

    # return the output image
    cv2.imshow("stuff",image)
    cv2.waitKey(0)
    return image


#for i in range(1, 96):
#    img = cv2.imread("processed/" + str(i) + ".tif")
#    cv2.imwrite("connected/" + str(i) + ".tif", connected(img))
#img = cv2.imread("processed/1.tif")
img = cv2.imread("largest connected/67.tif")
connected(img)

