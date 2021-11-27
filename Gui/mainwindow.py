from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow, QFileDialog
import cv2, time, imutils, os, numpy as np
from PIL import ImageQt

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
        # self.loadImage()
        
        # self.setPhoto(self.image)
        



    def loadImage(self):
        """ This function will load the Image
        """
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)

        if self.image is None:
            print("img is empty")
            pass
        else:
            self.setPhoto(self.image)
        

    def setPhoto(self,img):
        """ This function will take image input and resize it
            only for display purpose and convert it to QImage
            to set at the label.
        """
        self.tmp = img
        # img = imutils.resize(img,width=640)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        QImg = QtGui.QImage(img, img.shape[1],img.shape[0],img.strides[0],QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(QImg)
        self.ui.label.setPixmap(pixmap)
        # self.ui.show()


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
            self.draw_Ellipse(ce_co,"Defect: Cut")


    def savePhoto(self):
        """ This function will save the image"""

        self.filename = 'defectoutput_'+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png'
                
        image = ImageQt.fromqpixmap(self.ui.label.grab())
        image.save(self.filename)


    def draw_Ellipse(self,coordinates,text):
        '''This function draws a red elypse around the center point which is passed as (x,y) tuple.
        
        '''
        x = coordinates[0]
        y = coordinates[1]
        print('center Point x: ' + str(x ))
        print('center Point y: ' + str(y ))
        rx = 80
        ry = 120
        painter = QtGui.QPainter(self.ui.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)
        painter.drawEllipse(x-rx/2, y-ry/2,rx, ry)

        # text font settings
        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(15)
        painter.setFont(font)
        painter.drawText(x + rx*1.01, y, text)

        painter.end()
        # self.ui.label.show()

        self.ui.label.adjustSize()
        # self.ui.label_top.setPixmap(self.ui.label.pixmap())
        # self.ui.label_bot.setText(self.ui.label.pixmap())
        
        # self.image.save(self.filename)
        
  
  
