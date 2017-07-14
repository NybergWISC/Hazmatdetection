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
    this code takes approximately 40 secs to run
    """
def filter_matches(kp1, kp2, matches, ratio = 0.75, filename2):
    mkp1, mkp2 = [], []
    for m in matches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            m = m[0]
            mkp1.append( kp1[m.queryIdx] )
            mkp2.append( kp2[m.trainIdx] )	    
    kp_pairs = zip(mkp1, mkp2) 
    compare = len(kp_pairs)
    print compare
    #num =
    L.append(compare)
    L1 = {'filename2' : []}
    L1.append(L)
    #L2.append(num)
    
    print L1
    
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
    
    raw_matches = bf.knnMatch(des1, trainDescriptors = des2, k = 2) #2
    kp_pairs = filter_matches(kp1, kp2, raw_matches, filename2)
    
L1 = {}
L = []
compare('symbols/corrosive.jpg', 'symbols/corrosive.jpg')

compare('symbols/corrosive.jpg', 'symbols/explosive.jpg')
compare('symbols/corrosive.jpg', 'symbols/dangerouswhenwet.jpg')
high = max(L1)
#d = {'a': [], 'b': []}
#d['a'].append(L1)
#d['b'].append(L2)
print L1
#print d
print high
"""
compare('symbols/corrosive.jpg', 'symbols/flammableliquid.jpg')
compare('symbols/corrosive.jpg', 'symbols/flammablesolid.jpg')
compare('symbols/corrosive.jpg', 'symbols/infectioussubstance.jpg')
compare('symbols/corrosive.jpg', 'symbols/inhalationhazard.jpg')
compare('symbols/corrosive.jpg', 'symbols/nonflammablegas.jpg')
compare('symbols/corrosive.jpg', 'symbols/organicperoxide.jpg')
compare('symbols/corrosive.jpg', 'symbols/oxidizer.jpg')
compare('symbols/corrosive.jpg', 'symbols/radioactive.jpg')
compare('symbols/corrosive.jpg', 'symbols/spontcombustible.jpg')

"""