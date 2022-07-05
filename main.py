from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QShortcut
from PyQt5.QtGui import QKeySequence, QIcon
import sys
from functools import partial


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # set them
        loadUi("files/calculator_gui.ui", self)

        # set the icon
        self.setWindowIcon(QIcon("images/calculator_icon.png"))

        # set the title
        self.setWindowTitle("Calculator")

        #Insert numer to #echo and add numbers shortcuts
        for number in range(0,10):
            self.findChild(QPushButton, f"b_{number}").clicked.connect( partial(self.insert_number, number) )
            QShortcut(QKeySequence(f"{number}"), self).activated.connect(partial(self.insert_number, number))
 
              
        # Delete last input add backspace shortcut
        self.findChild(QPushButton, "b_delete").clicked.connect( self.delete_number )
        QShortcut(QKeySequence("Backspace"), self).activated.connect( self.delete_number )
        
        # show all the widgets
        self.show()


    def insert_number(self, number):
        try:
            echo = self.findChild(QLineEdit, "echo")
            numbers = echo.text()
            echo.setText( numbers + str(number) )
            count = len( numbers + str(number))

            if count > 18 :
                new_font_size = echo.fontInfo().pointSize() - 1 
                if new_font_size > 8 :
                    new_font = echo.font()
                    new_font.setPointSize(new_font_size)
                    echo.setFont(new_font)
        except Exception as e:
            print(e)

    def delete_number(self):
        try:
            echo = self.findChild(QLineEdit, "echo")
            echo.setText( echo.text()[:-1] )
            
            if len(echo.text()[:-1]) < 22 :
                new_font_size = echo.fontInfo().pointSize() + 1 
                if new_font_size < 20 :
                    new_font = echo.font()
                    new_font.setPointSize(new_font_size)
                    echo.setFont(new_font)           
        except Exception as e:
            print(e)
        
        

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
