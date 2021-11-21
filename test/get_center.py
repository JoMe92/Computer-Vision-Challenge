import cv2
import numpy as np



image = cv2.imread(r'C:\Users\Jonas Meier\Development\Taymer-Computer-Vision-Challenge\Input Images\Cut.bmp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)




cnts = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]



#%%

# Get center of imgage
c = cnts[1]
M = cv2.moments(c)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

cv2.circle(image, (cX, cY), 5, (36, 255, 12), -1)
image[cY][:] = (36, 255, 12)
image[:, cX] = (36, 255, 12)
row_pixels = cv2.countNonZero(gray[cY][:])
column_pixels = cv2.countNonZero(gray[:, cX])

print('row', row_pixels)
print('column', column_pixels)


cv2.imshow('inverted', image)
cv2.imwrite('inverted.png', image)
cv2.waitKey(0)



