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
[Fabric Defect Detection Using Fourier Transform and Gabor Filters](https://www.researchgate.net/publication/323046716_Fabric_Defect_Detection_Using_Fourier_Transform_and_Gabor_Filters)

[Tutorial 74 - What are Gabor filters and how to use them to generate features for machine learning](https://www.youtube.com/watch?v=yn1NUwaxhZg)

[58 - What are Gabor filters?](https://www.youtube.com/watch?v=QEz4bG9P3Qs)


<img src="https://github.com/JoMe92/Taymer-Computer-Vision-Challenge/blob/main/Output%20Images/horizontal Gabor filter.png" align="center"
     alt="img" >


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
