import cv2
import numpy as np
import os
from os import scandir 
from os import listdir
from matplotlib import pyplot as plt
import img_processing.core as co


import tkinter as tk
from tkinter import filedialog


#%%
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()


img = cv2.imread(file_path,-1) 
# Checking if the image is empty or not
if img is None:
    result = "Image is empty!"
else:
    result = "Image is not empty!"

print(result)

#%%
# Get dist

y = [100, 300, 600]
img_plot = img

for y1 in y:
    x, w = co.get_diameter(img_plot, y1)
    img_plot = co.plot_diameter(img, x, y1, w)
    
    
cv2.imshow('img_plot', img_plot)
cv2.imwrite('img_plot.png', img_plot)
cv2.waitKey(0)

#%%
# detect sratch 

center  = co.classify_scratches(img)
img_with_mark = co.mark_defect(img,center)

cv2.imshow('img_plot', img_with_mark)
cv2.waitKey(0)



print ("end")