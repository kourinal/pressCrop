
import cv2
import numpy as np

def hough(img):
    #img = cv2.imread('largest connected scaled/2.tif')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200, apertureSize=3)
    height, width, channels = img.shape
    minLineLength = height/2
    maxLineGap = 10
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 15, minLineLength, maxLineGap)
    for x in range(0, len(lines)):
        for x1, y1, x2, y2 in lines[x]:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return img

for i in range(1, 95):
    print(i)
    img = cv2.imread("largest connected/" + str(i) + ".tif")
    cv2.imwrite("hough/" + str(i) + ".tif", hough(img))


