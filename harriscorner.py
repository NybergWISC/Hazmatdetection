import cv2
import numpy as np

filename = 'small.png'
img = cv2.imread(filename)

img2 = np.float32(img)
dst = cv2.cornerHarris(img2,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()