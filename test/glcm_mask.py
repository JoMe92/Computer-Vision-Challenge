# -*- coding: utf-8 -*-
"""


@author: https://stackoverflow.com/questions/53100183/cropping-image-to-object-regions-area
"""

import numpy as np 
from skimage import io, color, util
from skimage.feature.texture import greycoprops
import matplotlib.pyplot as plt

def glcm_roi(img, mask, dh=1, dv =0, levels=256):
    glcm = np.zeros(shape=(levels, levels), dtype=np.int_)
    for i in range(img.shape[0] - dv):
        for j in range(img.shape[1] - dh):
            if mask[i, j] and mask[i + dv, j + dh]:
                glcm[img[i, j], img[i + dv, j + dv]] += 1
    return glcm/glcm.sum()

import cv2 
image = cv2.imread(r'C:\Users\Jonas Meier\Development\Taymer-Computer-Vision-Challenge\Input Images\Cut.bmp') #data.camera()
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
mask = img > 90

img = arr # util.img_as_ubyte(color.rgb2gray(arr[:, :, :-1]))

glcm = glcm_roi(img, mask)
energy = greycoprops(glcm[:, :, None, None], 'energy')
print('Energy = {}'.format(energy))

# fig, ax = plt.subplots(1, 3)
# ax[0].imshow(arr, cmap='gray')
# ax[0].set_title('RGB')
# ax[1].imshow(img, cmap='gray')
# ax[1].set_title('Gray')
# ax[2].imshow(mask, cmap='gray')
# ax[2].set(title='Mask')
# for axi in ax: axi.set_axis_off()
# plt.show(fig)