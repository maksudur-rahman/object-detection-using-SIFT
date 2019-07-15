import numpy as np
import cv2
from matplotlib import pyplot as plt 

img1 = cv2.imread('ball.jpg',0)          # queryImage
img2 = cv2.imread('main.jpg',0) # trainImage

  # Initiate SIFT detector
sift = cv2.ORB_create()

  # find the keypoints and descriptors with ORB
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

  # create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

 # Match descriptors.
matches = bf.match(des1,des2)

 # Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

 # Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches ,None, flags=2)

plt.imshow(img3),plt.show()
