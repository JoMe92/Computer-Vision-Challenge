import numpy as np
import cv2
import matplotlib.pyplot as plt

ksize = 50  #Use size that makes sense to the image and fetaure size. Large may not be good. 
#On the synthetic image it is clear how ksize affects imgae (try 5 and 50)
sigma = 3 #Large sigma on small features will fully miss the features. 
theta = 1*np.pi*1/2  # Horizintal lines
# theta = 1*np.pi*1/1  # vertical lines
# theta = 1*np.pi*1/4  # 45° lines lines
# theta = 3*np.pi*1/4  # 45° lines lines

lamda = 1*np.pi *1/4  #1/4 works best for angled. 
gamma = 0.7  #Value of 1 defines spherical. Calue close to 0 has high aspect ratio
#Value of 1, spherical may not be ideal as it picks up features from other regions.
phi = 0  #Phase offset. I leave it to 0. 


kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)

img = cv2.imread(r'C:\Users\Jonas Meier\Development\Taymer-Computer-Vision-Challenge\Input Images\Cut.bmp') #data.camera()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
fimg = cv2.filter2D(img, cv2.CV_8UC3, kernel)

kernel_resized = cv2.resize(kernel, (600, 600)) 

fig = plt.figure(figsize=(8, 8))
# display original image with locations of patches
ax = fig.add_subplot(1, 3, 1)
ax.imshow(img, cmap=plt.cm.gray,
          vmin=0, vmax=255)
ax.set_xlabel('Original Image')
ax.set_xticks([])
ax.set_yticks([])
ax.axis('image')

ax = fig.add_subplot(1, 3, 2)
ax.imshow(fimg, cmap=plt.cm.gray,
          vmin=0, vmax=255)
ax.set_xlabel('filtered image')
ax.set_xticks([])
ax.set_yticks([])
ax.axis('image')

ax = fig.add_subplot(1, 3, 3)
ax.imshow(kernel_resized, cmap=plt.cm.gray)
ax.set_xlabel('Kernel')
ax.set_xticks([])
ax.set_yticks([])
ax.axis('image')
plt.tight_layout()
plt.show()
