from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QShortcut
from PyQt5.QtGui import QKeySequence, QIcon
import sys
from functools import partial
from files.calculator import Calculator
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.calculator = None
        self.last_func  = None

        # set them
        loadUi("files/calculator_gui.ui", self)

        # set the icon
        self.setWindowIcon(QIcon("images/calculator_icon.png"))

        # set the title
        self.setWindowTitle("Calculator")

        #Insert numer to #echo and add numbers shortcuts
        for number in range(0,10):
            b_number = self.findChild(QPushButton, f"b_{number}")
            b_number.clicked.connect( partial(self.insert_number, number) )
            b_number.setShortcut(f"{number}")

        #Insert Period to #echo and add numbers shortcuts
        b_dot = self.findChild(QPushButton, "b_dot")
        b_dot.clicked.connect( self.insert_dot )
        b_dot.setShortcut(".")

        # Delete last input and add backspace shortcut
        b_delete = self.findChild(QPushButton, "b_delete")
        b_delete.clicked.connect( self.delete_number )
        b_delete.setShortcut("Backspace")

        # Clear all
        b_clear_e = self.findChild(QPushButton, "b_clear_e")
        b_clear_e.clicked.connect( self.clear_all )
        
        # Clear all and add Delete shortcut
        b_clear = self.findChild(QPushButton, "b_clear")
        b_clear.clicked.connect( self.clear_all )
        b_clear.setShortcut("Delete")        
        
        # Show calculated number
        b_equal = self.findChild(QPushButton, "b_equal")
        b_equal.clicked.connect( self.equal )  
        b_equal.setShortcut("Enter")
        QShortcut(QKeySequence("="), self).activated.connect( self.equal )
        
        # Sum and add Sum shortcut
        b_equal = self.findChild(QPushButton, "b_addition")
        b_equal.clicked.connect( self.addition )  
        b_equal.setShortcut("+")

        # show all the widgets
        self.show()


    def addition(self):
        self.commiter()
        self.last_func  = 'addition'
        data = self.findChild(QLineEdit, "echo").text()
        if data == "": data = 0
        if self.calculator == None:
            number = float(data)
            self.calculator = Calculator(number)
        
        self.findChild(QLineEdit, "value").setText(str(self.calculator.value))
        self.findChild(QLineEdit, "echo").setText("")
        
             
    def commiter(self):
        if self.last_func  == 'addition':
            data = self.findChild(QLineEdit, "echo").text()
            if data == "": data = 0
            self.calculator += float(data)

        
    def equal(self):
        if self.calculator != None:
            self.commiter()
            self.last_func  = None
            self.findChild(QLineEdit, "echo").setText(str(self.calculator.value))
            self.findChild(QLineEdit, "value").setText(str(self.calculator.value))

        
    def insert_dot(self):
        try:
            echo = self.findChild(QLineEdit, "echo")
            numbers = echo.text()
            if numbers == "":
                echo.setText( "0." )
            elif not "." in numbers:
                echo.setText( numbers + "." )
        except Exception as e:
            print(e)
        

    def insert_number(self, number):
        try:
            echo = self.findChild(QLineEdit, "echo")
            numbers = echo.text()
            data = numbers + str(number)
            if len(data) == 2 and data[1] != "." and data[0] == "0":
                data = data[1:]
                
            echo.setText( data )
            count = len( data)

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
        
    def clear_all(self):
        try:
            echo = self.findChild(QLineEdit, "echo")
            new_font = echo.font()
            new_font.setPointSize(20)
            echo.setFont(new_font)      
            self.findChild(QLineEdit, "echo").setText('')
            self.findChild(QLineEdit, "value").setText("")
            self.calculator = None
            self.last_func  = None
        except Exception as e:
            print(e)

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
