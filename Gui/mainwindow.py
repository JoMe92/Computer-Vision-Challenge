from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow, QFileDialog
import cv2, time, imutils, os, numpy as np

import tkinter as tk
from tkinter import filedialog

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


        # initalization of the default parameters
        self.filename = 'Img_'+str(time.strftime("%Y-%b-%d_at_%H.%M.%S %p"))+'.png' # Will hold the image address location
        self.tmp = None # Will hold the temporary image for display


    def loadImage(self):
        """ This function will load the camera device, obtain the image
            and set it to label using the setPhoto function
        """
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        # self.image = core.plot_diameter(self.image, 500,500,50)


        self.setPhoto(self.image)

    def measure_dist(self, image):
        """


        """
        y1 = [100,300,600]
        for y in y1:
            x, w = core.get_diameter(self.image, y)
            self.image = core.plot_diameter(self.image, x, y, w)
        #self.image = core.plot_diameter(self.image, 500,500,50)
        self.setPhoto(self.image)

    def setPhoto(self,image):
        """ This function will take image input and resize it
            only for display purpose and convert it to QImage
            to set at the label.
        """
        self.tmp = image
        # image = imutils.resize(image,width=640)
        frame =  image # np.dstack([image, image, image]) # only for B&W image to get (x,x,3) shape
        image = QtGui.QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QtGui.QImage.Format_RGB888)
        self.ui.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def update(self):
        """ This function will update the photo according to the
            current values of blur and brightness and set it to photo label.
        """
        img = self.image
        self.setPhoto(img)
        # self.savePhoto()


    def savePhoto(self):
        """ This function will save the image"""


        self.filename = 'Snapshot '+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png'
        cv2.imwrite(self.filename,self.tmp)
        print('Image saved as:',self.filename)




