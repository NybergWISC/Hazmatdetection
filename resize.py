import cv2
import numpy as np

img = cv2.imread('download3.png')
img2 = cv2.resize(img, (100, 50))
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()

cv2.imwrite('small.png',img2)
