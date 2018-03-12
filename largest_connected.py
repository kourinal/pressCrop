import cv2
import numpy as np


def undesired_objects(image):
    image = image.astype('uint8')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(gray, connectivity=4)
    sizes = stats[:, -1]

    max_label = 1
    max_size = sizes[1]
    for i in range(2, nb_components):
        if sizes[i] > max_size:
            max_label = i
            max_size = sizes[i]

    img2 = np.zeros(output.shape)
    img2[output == max_label] = 255
    return img2


for i in range(1, 95):
    img = cv2.imread("processed scaled/" + str(i) + ".tif")
    cv2.imwrite("largest connected scaled/" + str(i) + ".tif", undesired_objects(img))

