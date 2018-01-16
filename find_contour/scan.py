# import the necessary packages
from find_contour.transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils
import os


# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--img", required=True, help = "Path to the image to be scanned")
#args = vars(ap.parse_args())
# load the image and compute the ratio of the old height
# to the new height, clone it, and resize it
print(os.path.dirname(os.getcwd()))
image = cv2.imread(os.path.dirname(os.getcwd())+"/processed/0.tif")
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height=500)

# convert the image to grayscale, blur it, and find edges
# in the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)

# show the original image and the edge detected image
print("STEP 1: Edge Detection")

# find the contours in the edged image, keeping only the
# largest ones, and initialize the screen contour
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True) #[:5]
#_, cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
fill = cv2.drawContours(image, cnts, -1, color=(0, 0, 0))
gray = cv2.cvtColor(fill, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
contours = cv2.findContours(edged.copy(), 1, 2)
cnt = contours[0]
# loop over the contours
for c in cnts:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.09 * peri, True)

    # if our approximated contour has four points, then we
    # can assume that we have found our screen
    if len(approx) == 4:
        screenCnt = approx
        break
peri = cv2.arcLength(cnts[0], True)
approx = cv2.approxPolyDP(cnts[0], 0.09 * peri, True)
# show the contour (outline) of the piece of paper
print("STEP 2: Find contours of paper")
#print(screenCnt[0][0])
#topX = screenCnt[0][0][0]
#topY = screenCnt[0][0][1]
#botX = screenCnt[2][0][0]
#botY = screenCnt[2][0][1]
cv2.drawContours(image, [approx], -1, (0, 255, 0), 1)
#cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
#cv2.rectangle(image, (topX, topY), (botX, botY), (0, 255, 0), 3)
cv2.imshow("Outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
