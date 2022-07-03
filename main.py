from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # set them
        loadUi("files/calculator_gui.ui", self)

        # set the icon
        self.setWindowIcon(QtGui.QIcon("images/calculator_icon.png"))

        # set the title
        self.setWindowTitle("Calculator")

        # show all the widgets
        self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
