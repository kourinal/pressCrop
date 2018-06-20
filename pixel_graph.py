import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("largest connected scaled/8.tif", 0)
height, width = image.shape
arr = []
for i in range(0, width):
    x1 = np.count_nonzero(image[:, i])
    arr.append(x1)
t = range(0, width)
plt.plot(t, arr)
#plt.imshow(original_img)
plt.show()