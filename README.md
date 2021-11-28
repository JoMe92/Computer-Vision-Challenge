# Taymer-Computer-Vision-Challenge



     
In Taymer-Computer-Vision-Challenge an application is developed to measure cables and to detect defective ones. Via a graphical user interface it is possible to load images. With the help of function buttons the width of the cable can be measured, a defect can be detected and classified and the image can be saved.


Contents
========

 * [User interface](#user-interface)
 * [Program Structure](#program-structure)
 * [Used Algorithms](#used-algorithms)
 * [Usage](#usage)
 <!--- * [Installation](#installation) --->

## User interface
---
The following describes the operation of the user interface. Images can be loaded and displayed on the screen. The four selection buttons can be used to operate the various functions of the program.  
<img src="https://github.com/JoMe92/Taymer-Computer-Vision-Challenge/blob/main/Output%20Images/GUI.png" align="center"
     alt="img" >

The functions of the buttons are as follows:

Button | Description |Shortcut
| :---: | :---: | :---:
Open  | open a filebroser to load a image | o
Save  | Screenshot of the program window  | s
Mesure  | Measure the width of the Cabel | a
Detect  | Label the found defects and make a screnshoot | b

Note:
There is no scaling of the images, so currently it is only possible to view the images if the monitor used has a better resolution than the image to be displayed.

Die nachfolgende abbildung zeigt ein bild das geladen und analysirt wurde.
<img src="https://github.com/JoMe92/Taymer-Computer-Vision-Challenge/blob/main/Output%20Images/GUI01.png" align="center"
     alt="img" >


## Program Structure
---


* [doc/](.\Taymer-Computer-Vision-Challenge\doc)                                   
  * [Gui/](.\Taymer-Computer-Vision-Challenge\doc\Gui)
  * [img_processing/](.\Taymer-Computer-Vision-Challenge\doc\img_processing)

* [Gui/](.\Taymer-Computer-Vision-Challenge\Gui)  
  * [ProgramImages/](.\Taymer-Computer-Vision-Challenge\Gui\ProgramImages)
  * [main.ui](.\Taymer-Computer-Vision-Challenge\Gui\main.ui)
  * [mainwindow.py](.\Taymer-Computer-Vision-Challenge\Gui\mainwindow.py)
  * [main_new.ui](.\Taymer-Computer-Vision-Challenge\Gui\main_new.ui)
  * [ui_main.py](.\Taymer-Computer-Vision-Challenge\Gui\ui_main.py)
  * [ui_main_new.py](.\Taymer-Computer-Vision-Challenge\Gui\ui_main_new.py)

* [img_processing/](.\Taymer-Computer-Vision-Challenge\img_processing)
  * [core.py](.\Taymer-Computer-Vision-Challenge\img_processing\core.py)

* [test/](.\Taymer-Computer-Vision-Challenge\test)
  * [gabor_filters.py](.\Taymer-Computer-Vision-Challenge\test\gabor_filters.py)
  * [gabor_filter_banks.py](.\Taymer-Computer-Vision-Challenge\test\gabor_filter_banks.py)
  * [get_center.py](.\Taymer-Computer-Vision-Challenge\test\get_center.py)
  * [get_cut_gabor.py](.\Taymer-Computer-Vision-Challenge\test\get_cut_gabor.py)
  * [get_dist.py](.\Taymer-Computer-Vision-Challenge\test\get_dist.py)
  * [get_pin_hole.py](.\Taymer-Computer-Vision-Challenge\test\get_pin_hole.py)
  * [get_scratch.py](.\Taymer-Computer-Vision-Challenge\test\get_scratch.py)
  * [glcm.py](.\Taymer-Computer-Vision-Challenge\test\glcm.py)
  * [glcm_mask.py](.\Taymer-Computer-Vision-Challenge\test\glcm_mask.py)
  * [test.py](.\Taymer-Computer-Vision-Challenge\test\test.py)

* [main.py](.\Taymer-Computer-Vision-Challenge\main.py)


The doc folder contains the documentation of the project. An automatic html document was created from the docstrings that were used. The source code of the application is located in the Gui and img_processing folders. The graphical user interface was realized with QT and pyside2. The layout of the gui can be found in the main.ui file. The logic behind the user interactions is in the file mainwindow.py . In the file mainwindow.py is defined which functions are called when a user interacts with the userinterface. The functions needed to process the images are stored in the folder img_processing in the file core.py. For the functions OPenCv was used to analyze different image features. In order to apply and test the various image processing algorithms, the files for testing the individual functions of the core library are located in the Test folder. The main folder Taymer-Computer-Vision-Challenge contains the main.py file that starts the application.





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
