from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow, QFileDialog
import cv2, time, os, numpy as np
from PIL import ImageQt

from img_processing import core
from Gui.ui_main_new import Ui_MainWindow


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

    def loadImage(self):
        """ This function will load the Image
        """
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        img = self.image
        if self.image is None:
            print("img is empty")
            pass
        else:
            self.setPhoto(self.image)
        

    def setPhoto(self,img):
        """ This function will take image input and  and convert it to QImage to set at the label.
        """
        self.tmp = img
        # img = imutils.resize(img,width=640)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        QImg = QtGui.QImage(img, img.shape[1],img.shape[0],img.strides[0],QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(QImg)
        self.ui.label.setPixmap(pixmap)
        self.ui.label.setGeometry(0, 0, self.x_size, self.y_size)

    def measure_dist(self):
        """ this function measures the diameter of the cable. The function is linked to the mesure button
        """
        y1 = [50,300,950]
        img = self.image
        for y in y1:
            x, w = core.get_diameter(img, y)
            self.plot_diameterQt((x, y), w)


    def detect_defect(self):
        """ This function classifies the defects found in the loaded image. Via the is_active flag the individual inspections can be switched on or off.
        The coordinates of the respective defect are determined for display. These coordinates are passed on to a function in order to place an annotation as an overlay on the image. 
        """

        image_disp = self.image
        cut_nr = 1
        # Clasification of a scratch in the cable
        is_active = False
        if is_active == True:
           
            center_coordinates = core.get_scratches(image_disp)
            if not center_coordinates:
                print("no scratches found")
            else:
                for ce_co in center_coordinates:
                    self.draw_Ellipse(ce_co,"Defect: scratch")
        
        # Clasification of a cut in the cable
        is_active = True
        if is_active == True:
            center_coordinates_cut = core.get_cut(image_disp) 
            if not center_coordinates_cut:
                print("no cut found")
            else:
                for ce_co in center_coordinates_cut:
                    self.draw_Ellipse(ce_co,"Defect: Cut {}".format(cut_nr))
                    cut_nr = cut_nr + 1

        # Clasification of a pin_hole in the cable
        is_active = True
        if is_active == True:
            circles  = core.get_pin_hole(image_disp) 
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0, :]:
                    center = (i[0], i[1]) # circle center
                    radius = i[2]
                    self.draw_Ellipse(center,"Defect: pin_hole")

        self.savePhoto()

    def savePhoto(self):
        '''
        This function saves the image with overlay
        '''

        self.filename = 'defectoutput_'+str(time.strftime("%Y-%b-%d at %H.%M.%S %p"))+'.png'
        image = ImageQt.fromqpixmap(self.ui.label.grab())
        image.save(self.filename)


    def draw_Ellipse(self,coordinates,text):
        '''
        This function draws a red elypse around the center point which is passed as (x,y) tuple.
        '''
        x = coordinates[0]
        y = coordinates[1]
        # print('center Point x: ' + str(x ))
        # print('center Point y: ' + str(y ))
        rx = 80
        ry = 120
        painter = QtGui.QPainter(self.ui.label.pixmap())
        pen = QtGui.QPen()
        # pen settings
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
        self.ui.label.move(11, 11) 
        self.ui.label.move(10, 10) 
        # self.ui.label.adjustSize()

  
    def plot_diameterQt(self,coordinates,w):
        '''
        These functions draw a line at the given x-y position in an image.

        '''
        x = coordinates[0]
        y = coordinates[1]
        # print('center Point x: ' + str(x ))
        # print('center Point y: ' + str(y ))
        painter = QtGui.QPainter(self.ui.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)
        
        painter.drawLine(x- 0.1*w ,y, x  , y) # int x1, int y1, int x2, int y2
        painter.drawLine(x + w,y , x + w + 0.1*w, y) 

        # text font settings
        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(11)
        painter.setFont(font)
        painter.drawText(x + w + 0.2 * w, y, "diameter = " + str(w))
        painter.end()
        self.ui.label.move(11, 11) 
        self.ui.label.move(10, 10) 
        # self.ui.label.adjustSize()

