import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import shorestPath

#Crop image according to histogram
def cropImage(image):
    height, width = image.shape

    x_cord1 = 0
    #Loop over image histogram left to right, if 30% of the pixels are black, this is our edge
    for i in range(10, width-10):
        x1 = np.count_nonzero(image[:, i-10])
        x2 = np.count_nonzero(image[:, i+10])
        if (abs(x2 - x1))>0.3*height:
            print(i)
            x_cord1 = i
            break

    x_cord2 = 0
    # Loop over image histogram right to left, if 30% of the pixels are black, this is our edge
    for i in reversed(range(10, width-10)):
        x1 = np.count_nonzero(image[:, i-10])
        x2 = np.count_nonzero(image[:, i+10])
        if (abs(x2 - x1))>0.3*height:
            print(i)
            x_cord2 = i
            break

    #crop the image with the found coordinates
    result = image[0:height, x_cord1+10:x_cord2-10]
    return result

for i in range(1, 94):
    print(i)
    img = cv2.imread("largest connected scaled/" + str(i) + ".tif", 0)
    cv2.imwrite("Histogram/" + str(i) + ".tif", cropImage(img))


#print(hist)
