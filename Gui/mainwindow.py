from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow, QFileDialog
import cv2, time, imutils, os, numpy as np


from img_processing import core
from Gui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Call the corresponding functions when interacting with the gui
        self.ui.pushButton.clicked.connect(self.loadImage)
        self.ui.pushButton_2.clicked.connect(self.savePhoto)
        self.ui.pushButton_3.clicked.connect(self.measure_dist)
        self.ui.pushButton_4.clicked.connect(self.detect_defect)


        # initalization of the default parameters
        self.filename = 'Img_'+str(time.strftime("%Y-%b-%d_at_%H.%M.%S %p"))+'.png' # Will hold the image address location
        self.tmp = None # Will hold the temporary image for display
        self.image = None # Will hold        self.show_fft()
        self.loadImage()
        # self.setPhoto(self.image)


    def loadImage(self):
        """ This function will load the Image
        """
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)
        

    def setPhoto(self,img):
        """ This function will take image input and resize it
            only for display purpose and convert it to QImage
            to set at the label.
        """
        self.tmp = img
        img = imutils.resize(img,width=640)
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = QtGui.QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QtGui.QImage.Format_RGB888)
        self.ui.label.setPixmap(QtGui.QPixmap.fromImage(img))
    
    def measure_dist(self):
        """ this function measures the diameter of the cable
        """
        y1 = [50,300,950]
        img = self.image
        for y in y1:
            x, w = core.get_diameter(img, y)
            plot_img = core.plot_diameter(img, x, y, w)
        self.setPhoto(plot_img)



    def detect_defect(self):
        """ This function classifies the defect
        """

        image_disp = self.image
        # center_coordinates = core.classify_scratches(image_disp)
        # if not center_coordinates:
        #     print("no scratches found")
        # else:
        #     image_disp = core.mark_defect(image_disp, center_coordinates)
        #     image_disp = core.label_defect(image_disp, center_coordinates, "scratch")
        
        
        center_coordinates_cut = core.get_cut(image_disp) 

        if not center_coordinates_cut:
            print("no cut found")
        else:
            ce_co = center_coordinates_cut[0]
            image_disp = core.mark_defect(image_disp, ce_co)
            image_disp = core.label_defect(image_disp, ce_co, "cut")

        self.setPhoto(image_disp)




    def savePhoto(self):
        """ This function will save the image"""

        self.filename = 'defectoutput_'+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.jpg'
        cv2.imwrite(self.filename,self.tmp)
        print('Image saved as:',self.filename)



