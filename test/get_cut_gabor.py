import numpy as np
import cv2
import matplotlib.pyplot as plt
def mark_defect(img, center_coordinates):
    '''
    This function draws a red circle around given coordinates
    

    Parameters
    ----------
    img : Array of uint8
        The image in which the values are to be drawn
        
    center_coordinates : tuple of int
        the center  (x,y) of the defect
        

    Returns
    -------
    img : Array of uint8
        the image with the marking

    '''
    # Parameter
    radius = 50
    color = (10, 0, 255)
    thickness = 3
    # Draw a circle with blue line borders of thickness of 2 px
    img = cv2.circle(img, center_coordinates, radius, color, thickness)
    
    return img

def label_defect(img, coordinates, defect_name):
    '''
    the function adds a label to the given coordinates

    Parameters
    ----------
    img :  Array of uint8
        The image in which the values are to be drawn
        
    coordinates : tuple of int
        the center  (x,y) of the defect
        
    defect_name : str
        Name of the error

    Returns
    -------
    img : Array of uint8
        the image with the marking

    '''
    # plot value
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (int(coordinates[0]) + 75 , int(coordinates[1]))
    fontScale              = 0.5
    fontColor              = (0,0,255)
    thickness              = 1
    lineType               = 2
    text  = "Defect: " + defect_name
    
    cv2.putText(img,text, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        thickness,
            lineType)
    
    return img


img_orig = cv2.imread(r'C:\Users\Jonas Meier\Development\Taymer-Computer-Vision-Challenge\Input Images\Pin-Hole.bmp') #data.camera()
img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)


mask = cv2.dilate(img,np.ones((15,15),np.uint8),iterations = 6)
# mask = img > 35
# img[~mask] = 0


ksize = 50  #Use size that makes sense to the image and fetaure size. Large may not be good. 
sigma = 3 #Large sigma on small features will fully miss the features. 
theta = 1*np.pi*1/2  # Horizintal lines
lamda = 1*np.pi *1/4  #1/4 works best for angled. 
gamma = 0.01  #Value of 1 defines spherical. Calue close to 0 has high aspect ratio
phi = 0  #Phase offset. I leave it to 0. 
kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)
fimg = cv2.filter2D(img, cv2.CV_8UC3, kernel)
# plt.imshow(fimg, cmap=plt.cm.gray)

ret, th = cv2.threshold(fimg, 35, 255, cv2.THRESH_BINARY)
kernel = np.ones((2,2),np.uint8)
opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
dilation = cv2.dilate(opening,kernel,iterations = 6)

mask = img > 75
fg = cv2.bitwise_or(dilation, img,  img > 90 )

cnts = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0]
# x,y,w,h = cv2.boundingRect(cnt)
radius =2
color = (0,0,255)

center_coordinates = []
for cn in cnts:
    area = cv2.contourArea(cn)

    if (area > 850 and area < 3000):
        # cv2.drawContours(img_orig, cn, -1,color , radius)
        M = cv2.moments(cn)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        coordinates = (cX, cY)
        center_coordinates.append(coordinates)
        

img_fin = label_defect(img_orig,(cX, cY), "Cut")
img_fin = mark_defect(img_orig,(cX, cY))


cv2.imshow("img", img_fin)
cv2.waitKey(500)

# params = cv2.SimpleBlobDetector_Params()
# detector = cv2.SimpleBlobDetector_create(params)
# keypoints = detector.detect(fimg)
# area = []
# coordinates = []

# for key in keypoints:
#     area.append(key.size)
#     coordinates.append(key.pt)
