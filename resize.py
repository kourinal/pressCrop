
# import the necessary packages
import cv2
def resize(image):
    # load the image and show it
    print(image.shape)

    # we need to keep in mind aspect ratio so the image does
    # not look skewed or distorted -- therefore, we calculate
    # the ratio of the new image to the old image
    r = 500.0 / image.shape[1]
    dim = (500, int(image.shape[0] * r))

    # perform the actual resizing of the image and show it
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized

for i in range(1, 95):
    img = cv2.imread("largest connected/" + str(i) + ".tif")
    cv2.imwrite("scaled after largest connected/" + str(i) + ".tif", resize(img))