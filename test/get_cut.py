# -*- coding: utf-8 -*-

import cv2
import numpy as np

#%%
image = cv2.imread(r'C:\Users\Jonas Meier\Development\Taymer-Computer-Vision-Challenge\Input Images\Cut.bmp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)



#%%

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector()
# Detect blobs.
keypoints = detector.detect(gray)
