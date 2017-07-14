import cv2
import sys
import os.path
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import warnings
import imutils
import json
import cv2
import time

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
def filter_matches(kp1, kp2, filename2, matches, ratio = 0.75):
    mkp1, mkp2 = [], []
    for m in matches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            m = m[0]
            mkp1.append( kp1[m.queryIdx] )
            mkp2.append( kp2[m.trainIdx] )	    
    kp_pairs = zip(mkp1, mkp2)	 
    compareSon = len(kp_pairs)
    print compareSon
    if compareSon > 30:
        
        if filename2 == 'symbols/corrosive.jpg':
	   print "warning: corrosive"
	if filename2 == 'symbols/explosive.jpg':
	   print "warning: explosive"
	if filename2 == 'symbols/dangerouswhenwet.jpg':
	   print "warning: dangerous when wet"
	if filename2 == 'symbols/flammableliquid.jpg':
	   print "warning: flammable liquid"
	if filename2 == 'symbols/flammablesolid.jpg':
	   print "warning: flammable solid"
	if filename2 == 'symbols/infectioussubstance.jpg':
	   print "warning: infectious disease"
	if filename2 == 'symbols/inhalationhazard.jpg':
	   print "warning: inhalation hazard"
	if filename2 == 'symbols/nonflammablegas.jpg':
	   print "warning: nonflammable gas"
	if filename2 == 'symbols/organicperoxide.jpg':
	   print "warning: organic peroxide"
	if filename2 == 'symbols/oxidizer.jpg':
	   print "warning: oxidizer"
	if filename2 == 'symbols/radioactive.jpg':
	   print "warning: radioactive material"
	if filename2 == 'symbols/spontcombustible.jpg':
	   print "warning: spontaneously combustible"
    """
    L.append(compareSon)
    Name = filename2
    L1 = {Name : []}
    L1[Name].append(L)

    
    
    print L1
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
    
    raw_matches = bf.knnMatch(des1, trainDescriptors = des2, k = 2) #2
    kp_pairs = filter_matches(kp1, kp2, filename2, raw_matches)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--conf", required=True,
	help="path to the JSON configuration file")
args = vars(ap.parse_args())
# filter warnings, load the configuration and initialize the Dropbox
# client
warnings.filterwarnings("ignore")
conf = json.load(open(args["conf"]))
client = None

#start camera and save picture to folder
print "take picture with q"
camera = PiCamera()
camera.resolution = tuple(conf["resolution"])
camera.framerate = conf["fps"]
rawCapture = PiRGBArray(camera, size=tuple(conf["resolution"]))
print "[INFO] warming up..."
time.sleep(conf["camera_warmup_time"])
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	frame = f.array
	frame = imutils.resize(frame, width=500)

	if conf["show_video"]:
		# display the security feed
		cv2.imshow("Camera", frame)
		key = cv2.waitKey(1) & 0xFF
		cv2.imwrite('hazmatpic.jpg', frame)
	
                
		# if the `q` key is pressed, break from the lop
		if key == ord("q"):
			break
	rawCapture.truncate(0)



compare('hazmatpic.jpg', 'symbols/corrosive.jpg')
compare('hazmatpic.jpg', 'symbols/explosive.jpg')
compare('hazmatpic.jpg', 'symbols/dangerouswhenwet.jpg')

compare('hazmatpic.jpg', 'symbols/flammableliquid.jpg')
compare('hazmatpic.jpg', 'symbols/flammablesolid.jpg')
compare('hazmatpic.jpg', 'symbols/infectioussubstance.jpg')
compare('hazmatpic.jpg', 'symbols/inhalationhazard.jpg')
compare('hazmatpic.jpg', 'symbols/nonflammablegas.jpg')
compare('hazmatpic.jpg', 'symbols/organicperoxide.jpg')
compare('hazmatpic.jpg', 'symbols/oxidizer.jpg')
compare('hazmatpic.jpg', 'symbols/radioactive.jpg')
compare('hazmatpic.jpg', 'symbols/spontcombustible.jpg')
