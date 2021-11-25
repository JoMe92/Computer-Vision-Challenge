import matplotlib.pyplot as plt
from skimage.feature import greycomatrix, greycoprops
from skimage import data
import cv2
import numpy as np

PATCH_SIZE = 10

# open the camera image
image = cv2.imread(r'C:\Users\Jonas Meier\Development\Taymer-Computer-Vision-Challenge\Input Images\Cut.bmp') #data.camera()
	
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# select some patches from cable areas of the image
cabel_locations = [] 

for x in np.arange(0,500,50):
    tup = (x,275)
    cabel_locations.append(tup)
    tup1 = (x,295)
    cabel_locations.append(tup1)
for x in np.arange(600,1000,50):
    tup = (x,320)
    cabel_locations.append(tup)

cabel_patches = []
for loc in cabel_locations:
    cabel_patches.append(image[loc[0]:loc[0] + PATCH_SIZE,
                               loc[1]:loc[1] + PATCH_SIZE])




# select some defect areas
defect_locations = [] 
for x in np.arange(260,340,PATCH_SIZE + 1):
    tup = (490,x)
    defect_locations.append(tup)

    tup1 = (490 + PATCH_SIZE + 1  , x)
    defect_locations.append(tup1)


defect_patches = []
for loc in defect_locations:
    defect_patches.append(image[loc[0]:loc[0] + PATCH_SIZE,
                               loc[1]:loc[1] + PATCH_SIZE])

# select some patches from the backround areas of the image
backround_locations = []

for x in np.arange(0,1000,100):
    tup = (x,100)
    tup1 = (x,200)
    tup2 = (x,500)
    tup3 = (x,700)

    backround_locations.append(tup)
    backround_locations.append(tup1)
    backround_locations.append(tup2)
    backround_locations.append(tup3)


back_patches = []
for loc in backround_locations:
    back_patches.append(image[loc[0]:loc[0] + PATCH_SIZE,
                             loc[1]:loc[1] + PATCH_SIZE])

# compute some GLCM properties each patch
xs = []
ys = []
for patch in (cabel_patches):
    glcm = greycomatrix(patch, distances=[5], angles=[0], levels=256,
                        symmetric=True, normed=True)    
    xs.append(greycoprops(glcm, 'dissimilarity')[0, 0])
    ys.append(greycoprops(glcm, 'correlation')[0, 0])


xsb = []
ysb = []
for patch in (back_patches):
    glcm = greycomatrix(patch, distances=[5], angles=[0], levels=256,
                        symmetric=True, normed=True)    
    xsb.append(greycoprops(glcm, 'dissimilarity')[0, 0])
    ysb.append(greycoprops(glcm, 'correlation')[0, 0])

xsd = []
ysd = []
for patch in (defect_patches):
    glcm = greycomatrix(patch, distances=[5], angles=[0], levels=256,
                        symmetric=True, normed=True)    
    xsd.append(greycoprops(glcm, 'dissimilarity')[0, 0])
    ysd.append(greycoprops(glcm, 'correlation')[0, 0])




# create the figure
fig = plt.figure(figsize=(8, 8))
# display original image with locations of patches
ax = fig.add_subplot(2, 1, 1)
ax.imshow(image, cmap=plt.cm.gray,
          vmin=0, vmax=255)
for (y, x) in cabel_locations:
    ax.plot(x + PATCH_SIZE / 2, y + PATCH_SIZE / 2, 'bs')
for (y, x) in backround_locations:
    ax.plot(x + PATCH_SIZE / 2, y + PATCH_SIZE / 2, 'rs')
for (y, x) in defect_locations:
    ax.plot(x + PATCH_SIZE / 2, y + PATCH_SIZE / 2, 'gs')
ax.set_xlabel('Original Image with the patch areas')
ax.set_xticks([])
ax.set_yticks([])
ax.axis('image')


# for each patch, plot (dissimilarity, correlation)
ax = fig.add_subplot(2, 1, 2)
ax.plot(xs, ys, 'b+',label='cable')
ax.plot(xsb, ysb, 'r+',label='background')
ax.plot(xsd, ysd, 'g+',label='defect')
ax.set_xlabel('GLCM Dissimilarity')
ax.set_ylabel('GLCM Correlation')
ax.legend()
fig.suptitle('Grey level co-occurrence matrix features', fontsize=14, y=1.05)
plt.tight_layout()
plt.show()

# # display the image patches
# fig = plt.figure(figsize=(8, 8))
# ax = fig.add_subplot(1, 1, 1)
# for i, patch in enumerate(cabel_patches):
#     ax = fig.add_subplot(3, len(cabel_patches), len(cabel_patches)*1 + i + 1)
#     ax.imshow(patch, cmap=plt.cm.gray,
#               vmin=0, vmax=255)
#     ax.set_xlabel('cable %d' % (i + 1))

# for i, patch in enumerate(back_patches):
#     ax = fig.add_subplot(3, len(back_patches), len(back_patches)*2 + i + 1)
#     ax.imshow(patch, cmap=plt.cm.gray,
#               vmin=0, vmax=255)
#     ax.set_xlabel('backround %d' % (i + 1))



# # display the patches and plot
# fig.suptitle('Grey level co-occurrence matrix features', fontsize=14, y=1.05)
# plt.tight_layout()
# plt.show()