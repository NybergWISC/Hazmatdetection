import cv2
import sys
import os.path
import numpy as np
 
def drawMatches(img1, kp1, img2, kp2, matches):
    """
    https://www.codementor.io/tips/5193438072/module-object-has-no-attribute-drawmatches-opencv-python
    My own implementation of cv2.drawMatches as OpenCV 2.4.9
    does not have this function available but it's supported in
    OpenCV 3.0.0
 
    This function takes in two images with their associated 
    keypoints, as well as a list of DMatch data structure (matches) 
    that contains which keypoints matched in which images.
 
    An image will be produced where a montage is shown with
    the first image followed by the second image beside it.
 
    Keypoints are delineated with circles, while lines are connected
    between matching keypoints.
 
    img1,img2 - Grayscale images
    kp1,kp2 - Detected list of keypoints through any of the OpenCV keypoint 
              detection algorithms
    matches - A list of matches of corresponding keypoints through any
              OpenCV keypoint matching algorithm
    """
 
    
 
def compare(filename1, filename2):
    img1 = cv2.imread(filename1,0)          # queryImage
    img2 = cv2.imread(filename2,0)          # trainImage
 
    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SIFT_create()
 
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
 
    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.match(des1,des2)
    matches = sorted(matches, key=lambda val: val.distance)
    print matches
    
 
compare('symbols/corrosive.jpg', 'symbols/corrosive.jpg')
compare('symbols/corrosive.jpg', 'symbols/explosive.jpg')
compare('symbols/corrosive.jpg', 'symbols/dangerouswhenwet.jpg')
compare('symbols/corrosive.jpg', 'symbols/flammableliquid.jpg')
compare('symbols/corrosive.jpg', 'symbols/flammablesolid.jpg')
compare('symbols/corrosive.jpg', 'symbols/infectioussubstance.jpg')
compare('symbols/corrosive.jpg', 'symbols/inhalationhazard.jpg')
compare('symbols/corrosive.jpg', 'symbols/nonflammablegas.jpg')
compare('symbols/corrosive.jpg', 'symbols/organicperoxide.jpg')
compare('symbols/corrosive.jpg', 'symbols/oxidizer.jpg')
compare('symbols/corrosive.jpg', 'symbols/radioactive.jpg')
compare('symbols/corrosive.jpg', 'symbols/spontcombustible.jpg')