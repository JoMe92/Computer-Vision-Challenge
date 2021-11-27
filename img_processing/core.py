import cv2
import numpy as np

# Measure and Display the diameter
def get_diameter(img, y1 ):
    '''
    This function measures the diameter of a cable at a given position x

    Parameters
    ----------
    img : Array of uint8
        
    y1 : int
        the y position of the image at which a diameter is to be measured
        
    Returns
    -------
    x : int
        the x position at which the measurement begins
        
    w : int
        the diameter of the cable in pixels
    '''
    # Preprocessing of the image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(5,5),0)
    
    # Apply ROI to the image
    # y1 = 200
    y2 = y1 + 1
    gray_slice = gray[y1:y2,:]
    
    # Image Biarisiren and contours determine
    ret, th = cv2.threshold(gray_slice, 35, 255, cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(th, 1, 2)
    cnt = contours[0]
    x,y,w,h = cv2.boundingRect(cnt)
 
    return x, w

def plot_diameter(img, x,y1,w):
    '''
    These functions draw a line at the given x-y position in an image.

    Parameters
    ----------
    img : Array of uint8
        The image in which the values are to be drawn
        
    x : int
        x position of the drawing.
        
    y1 : int
        y position of the drawing.
        
    w : int
        line width.

    Returns
    -------
    img : TYPE
        DESCRIPTION.

    '''
    point1 = (x , y1)
    point2 = (x + w + 10,y1) 
    cv2.line(img,point1,point2,(255,0,255))
    
    # plot value
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = point2
    fontScale              = 0.3
    fontColor              = (255,255,255)
    thickness              = 1
    lineType               = 2
    text  = "Diameter = {} pix".format(w)
    
    cv2.putText(img,text, 
        bottomLeftCornerOfText, 
        font, 
        fontScale,
        fontColor,
        thickness,
        lineType)
    
    return img



def classify_scratches(img):
    '''
    The function checks if there is a scratch on the cable

    Parameters
    ----------
    img : Array of uint8
        The image in which the values are to be drawn

    Returns
    -------
    center_coordinates : tuple of int
        the center  (x,y) of the scratch

    '''
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(25,25),0)

    sobelxy = cv2.Sobel(gray,cv2.CV_64F,1,1,ksize=5)  
    sobelxy = cv2.convertScaleAbs(sobelxy) # covert to 8-bit
    
    ret, th = cv2.threshold(sobelxy, 6, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
    kernel = np.ones((4,4),np.uint8)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    
    params = cv2.SimpleBlobDetector_Params()
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 7
    
    detector = cv2.SimpleBlobDetector_create(params)
    # Detect blobs.
    keypoints = detector.detect(closing)
    
    if not keypoints:
        print("No scratch were  found")
        return 0
    
    else:
        area = []
        coordinates = []
    
        for key in keypoints:
            area.append(key.size)
            coordinates.append(key.pt)
            
        center_coordinates = (int(coordinates[0][0]), int(coordinates[0][1]))
        
        return center_coordinates
    

def get_cut(img):
    '''
    The function checks if there is a horizontal cut in the cable

    Parameters
    ----------
    img : Array of uint8
        the input image to be analyzed

    Returns
    -------
    center_coordinates : list of tuples with int
        each tuple contains the x and y coordinates of the center of gravity of the defect

    '''
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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
    
    cnts = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnts = cnts[0]

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
            
    return center_coordinates

    
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


