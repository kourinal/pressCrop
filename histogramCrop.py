import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import shorestPath


def cropImage(image):
    height, width = image.shape

    x_cord1 = 0
    for i in range(10, width-10):
        x1 = np.count_nonzero(image[:, i-10])
        x2 = np.count_nonzero(image[:, i+10])
        if (abs(x2 - x1))>0.5*height:
            print(i)
            x_cord1 = i
            break

    x_cord2 = 0
    for i in reversed(range(10, width-10)):
        x1 = np.count_nonzero(image[:, i-10])
        x2 = np.count_nonzero(image[:, i+10])
        if (abs(x2 - x1))>0.3*height:
            print(i)
            x_cord2 = i
            break
    result = image[0:height, x_cord1+10:x_cord2-10]
    return result

for i in range(1, 94):
    print(i)
    img = cv2.imread("largest connected scaled/" + str(i) + ".tif", 0)
    cv2.imwrite("Histogram/" + str(i) + ".tif", cropImage(img))


#print(hist)
