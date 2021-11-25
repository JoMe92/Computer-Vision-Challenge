# Taymer-Computer-Vision-Challenge



     
In `Taymer-Computer-Vision-Challenge` an application for the measurement and CLassification of cables is developed. It is possible to load images via a graphical user interface. Using function buttons, the width of the cabel can be measured, an error can be detected and Classified, and the image can be saved with overly.


Contents
========

 * [Why?](#why)
 * [Main Task](#main-task)
 * [Used Algorithms](#used-algorithms)
 * [Usage](#usage)
 <!--- * [Installation](#installation) --->

## Why?
---


## Main Task
---




## Used algorithms 
---

#### Grey-level Cooccurrence Matrix (GLCM)
A co-occurrence matrix or co-occurrence distribution (also referred to as : gray-level co-occurrence matrices GLCMs) is a matrix that is defined over an image to be the distribution of co-occurring pixel values (grayscale values, or colors) at a given offset. Further information can be found at 
[Wikipedia](https://en.wikipedia.org/wiki/Co-occurrence_matrix) and 
[University of Calgary](https://prism.ucalgary.ca/handle/1880/51900)

In the following section, it is evaluated whether the GLCM algorithm is suitable for the classification of defects such as scratch cuts or holes on calves. The function was implemented and evaluated using skimage. A test image was divided into three areas, the background, the cable and the defect. In each Brerich, 10x10 large pixel areas were viewed and analyzed with the GLCM. The following graph illustrates the results of the analysis.
<img src="https://github.com/JoMe92/Taymer-Computer-Vision-Challenge/blob/main/Output%20Images/glcm.png" align="center"
     alt="img" >
     
The upper image shows the original image and the patch areas to be examined. Care has been taken to ensure that the individual areas do not overlap and that there is a minimum distance of 1 pixel between the areas. Below is the graph for the evaluation of the GLCM algorithm, it shows the Calculate texture properties of the GLCM. It is shown that the texture analysis is suitable for separating the cable from the background but cannot be used for the classification of the defect.


### Gabor transform 
The Gabor transform, named after Dennis Gabor, is a special case of the short-time Fourier transform. It is used to determine the sinusoidal frequency and phase content of local sections of a signal as it changes over time. The function to be transformed is first multiplied by a Gaussian function, which can be regarded as a window function, and the resulting function is then transformed with a Fourier transform to derive the time-frequency analysis. [[Wikipedia](https://en.wikipedia.org/wiki/Gabor_transform)]
In the tutorial "[What are Gabor filters?](https://www.youtube.com/watch?v=QEz4bG9P3Qs)" is described how gabor filter can be used with OpenCv. Furthermore the meaning of the parameters to be set is explained. The figure below shows the original image on the left, the filtered image in the middle and the kernel used on the right.
<img src="https://github.com/JoMe92/Taymer-Computer-Vision-Challenge/blob/main/Output%20Images/horizontal Gabor filter.png" align="center"
     alt="img" >
The orientation of the cursor was chosen horizontally in order to segment lateral cuts. Es wurden Folgende PArameter verwendet: ksize = 50, sigma = 3, theta = 1*np.pi*1/2, lamda = 1*np.pi *1/4, gamma = 0.7, phi = 0  
In conclusion, the Gabor filter is well suited for defect detection when the direction of the defect is already known. 

By using a larger dataset, a classifier could be developed using SVM or Random Forest. First, the Gabor filter would be parameterized for classification purposes "[How to create Gabor feature banks](https://www.youtube.com/watch?v=BTbIS1mriuY)". Afterwards, the classifier can be trained with the data and a test train split "[Training RF](https://www.youtube.com/watch?v=XmRKkMjD8hM&t=563s
)". In the video "[Image Segmentation](https://www.youtube.com/watch?v=f205EmfXi84)" Describes how the model can be saved and used for classification
### to Read
local binary pattern (LBP)

scale-invariant feature transform (SIFT) 

Histograms of oriented gradient (HOG) 

Speeded up robust features (SURF) 

binary robust independent elementary features (BRIEF)

oriented FAST and rotated BRIEF (ORB)

completed local binary pattern (CLBP)

elliptical local binary pattern (ELBP) 

adjacent evaluation completed local binary pattern (AECLBP)

robust local binary pattern (RLBP)

 discriminant manifold regularized local descriptor (DMRLD) 

SVMs are suitable for small and medium-sized data samples 
