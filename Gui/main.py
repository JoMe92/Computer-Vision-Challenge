import sys
from PySide2 import  QtWidgets
from mainwindow import MainWindow

from ../img_processing import core 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())