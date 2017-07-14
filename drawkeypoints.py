import cv2
import numpy as np

img = cv2.imread('symbols/corrosive.jpg')

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
#kp = sift.detect(img,None)

img2=cv2.drawKeypoints(gray,kp,0,color=(255,0,255),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imwrite('image1.jpg',img2)

