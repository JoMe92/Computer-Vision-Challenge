# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainV1.1.ui',
# licensing of 'mainV1.1.ui' applies.
#
# Created: Tue Nov 23 08:22:42 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 509, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        # QtGui.QPixmap.fromImage(img)
        # self.label.setPixmap(QtWidgets.QPixmap(QtWidgets.QString("ProgramImages/1618324317566.jpg")))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)
        self.gridLayout_2.addWidget(self.splitter, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(327, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.label.clear)
        # QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.label.clear)
        # QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), self.label.clear)
        # QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), self.label.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.pushButton_2.setShortcut(QtWidgets.QApplication.translate("MainWindow", "S", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Mesure", None, -1))
        self.pushButton_3.setShortcut(QtWidgets.QApplication.translate("MainWindow", "A", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.pushButton.setShortcut(QtWidgets.QApplication.translate("MainWindow", "O", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "Detect", None, -1))
        self.pushButton_4.setShortcut(QtWidgets.QApplication.translate("MainWindow", "B", None, -1))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

