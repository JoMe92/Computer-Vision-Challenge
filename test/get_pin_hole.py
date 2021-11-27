import sys
import cv2 as cv
import numpy as np


# src  = cv.imread(r'C:\Users\Jonas Meier\Development\Taymer-Computer-Vision-Challenge\Input Images\Cut.bmp') 

# src  = cv.imread(r'C:\Users\Jonas Meier\Development\Taymer-Computer-Vision-Challenge\Input Images\Scratches.bmp') 
# src  = cv.imread(r'C:\Users\Jonas Meier\Development\Taymer-Computer-Vision-Challenge\Input Images\Pin-Hole and cut.bmp') 
src  = cv.imread(r'C:\Users\Jonas Meier\Development\Taymer-Computer-Vision-Challenge\Input Images\Pin-Hole.bmp') 


# Check if image is loaded fine

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 9)
# ret,thresh1 = cv.threshold(gray,200,255,cv.THRESH_BINARY)

rows = gray.shape[0]


# dp = 1
# minDist = rows / 8
# param1 = 250 #the higher threshold of the two passed to the Canny edge detector 
# param2 = 10 # it is the accumulator threshold for the circle centers at the detection stage. The smaller it is, the more false circles may be detected. 
# minRadius = 5
# maxRadius = 50

# circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, dp, minDist, param1, param2, minRadius, maxRadius)
 


# circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
#                             param1=255, param2 = 15,minRadius=5, maxRadius=10)


gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 9)
rows = gray.shape[0] 
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                            param1=255, param2 = 10,minRadius=5, maxRadius=10)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv.circle(src, center, 1, (0, 100, 100), 3)
        # circle outline
        radius = i[2]
        cv.circle(src, center, radius, (255, 0, 255), 3)


    
cv.imshow("detected circles", src)
cv.waitKey(0)
    


