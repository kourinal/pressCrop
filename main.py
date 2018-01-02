import m_transformations as m
import cv2

x = []
for i in range(16):
    print(i)
    m.openIm(cv2.imread('img/' + str(i) + '.tif'), str(i))
cv2.waitKey(0)
cv2.destroyAllWindows()
