# -*- coding: utf-8 -*-

import cv2
import numpy as np

#%%
image = cv2.imread(r'C:\Users\Jonas Meier\Development\Taymer-Computer-Vision-Challenge\Input Images\Scratches.bmp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(25,25),0)




# sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)  # x
# sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)  # y
sobelxy = cv2.Sobel(gray,cv2.CV_64F,1,1,ksize=5)  # y
sobelxy = cv2.convertScaleAbs(sobelxy)

ret, th = cv2.threshold(sobelxy, 6, 255, cv2.THRESH_BINARY)
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
kernel = np.ones((4,4),np.uint8)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)


#%% blob

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# # Change thresholds
# params.minThreshold = 200
# params.maxThreshold = 255

# # Filter by Area.
# params.filterByArea = True
# params.minArea = 55


# # Filter by Circularity
# params.filterByCircularity = False
# params.minCircularity = 0.1

# # Filter by Convexity
# params.filterByConvexity = False
# params.minConvexity = 0.87

# # Filter by Inertia
# params.filterByInertia = True
# params.minInertiaRatio = 0.01

detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(closing)
area = []
coordinates = []

for key in keypoints:
    area.append(key.size)
    coordinates.append(key.pt)

 
# im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


# Draw 
# Center coordinates
center_coordinates = (int(coordinates[0][0]), int(coordinates[0][1]))
# Radius of circle
radius = 50
  
# Blue color in BGR
color = (10, 0, 255)
  
# Line thickness of 2 px
thickness = 3
  
# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
image = cv2.circle(image, center_coordinates, radius, color, thickness)

#%%

# Show blobs
cv2.imshow("Keypoints", image)
cv2.waitKey(0)

#%%
