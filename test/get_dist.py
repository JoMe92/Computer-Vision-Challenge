import cv2
import numpy as np
import skimage.exposure


#%%
# Pree Processing
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
    y1 = 200
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
    point2 = (x + w,y1) 
    cv2.line(img,point1,point2,(255,0,255))
    
    # plot value
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = point2
    fontScale              = 0.5
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

#%%
# plot line
# read image
img  = cv2.imread(r'C:\Users\Jonas Meier\Development\Taymer-Computer-Vision-Challenge\Input Images\Cut.bmp')

y1 = 300
x, w = get_diameter(img, y1)
img_plot = plot_diameter(img, x, y1, w)

cv2.imshow('img_plot', img_plot)
cv2.imwrite('img_plot.png', img_plot)
cv2.waitKey(0)

#%%


