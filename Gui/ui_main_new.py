# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainqMoIIN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1580, 858)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 509, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(':/ProgramImages/1618324317566.jpg'))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.splitter.addWidget(self.layoutWidget)

        self.gridLayout_2.addWidget(self.splitter, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(327, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1580, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.label)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)
        # self.pushButton.clicked.connect(self.label.clear)
        # self.pushButton_2.clicked.connect(self.label.clear)
        # self.pushButton_3.clicked.connect(self.label.clear)
        # self.pushButton_4.clicked.connect(self.label.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Mesure", None))
#if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"M", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"O", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Detect", None))
#if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

