from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QShortcut,
    QMessageBox,
    QAction,
)
from PyQt5.QtGui import QKeySequence, QIcon
import sys
from functools import partial
from files.calculator import Calculator
from math import exp, factorial, pi, sqrt, pow, sin, cos, tan, log10
import webbrowser
from os.path import abspath, dirname, join
class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.calculator = None
        self.last_func = None

        # set them
        loadUi(self.resource_path("files/calculator_gui.ui"), self)

        # set the icon
        self.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))

        # set the title
        self.setWindowTitle("Calculator")

        # Insert numer to #echo and add numbers shortcuts
        for number in range(0, 10):
            b_number = self.findChild(QPushButton, f"b_{number}")
            b_number.clicked.connect(partial(self.insert_number, number))
            b_number.setShortcut(f"{number}")

        # Insert Period to #echo and add numbers shortcuts
        b_dot = self.findChild(QPushButton, "b_dot")
        b_dot.clicked.connect(self.insert_dot)
        b_dot.setShortcut(".")

        # Delete last input and add backspace shortcut
        b_delete = self.findChild(QPushButton, "b_delete")
        b_delete.clicked.connect(self.delete_number)
        b_delete.setShortcut("Backspace")

        # Clear all
        b_clear_e = self.findChild(QPushButton, "b_clear_e")
        b_clear_e.clicked.connect(self.clear_all)
        b_clear_e.setShortcut("Esc")

        # Clear all and add Delete shortcut
        b_clear = self.findChild(QPushButton, "b_clear")
        b_clear.clicked.connect(self.clear_insert)
        b_clear.setShortcut("Delete")

        # Show calculated number
        b_equal = self.findChild(QPushButton, "b_equal")
        b_equal.clicked.connect(self.equal)
        b_equal.setShortcut("Enter")
        QShortcut(QKeySequence("="), self).activated.connect(self.equal)

        # Sum and add Sum shortcut
        b_addition = self.findChild(QPushButton, "b_addition")
        b_addition.clicked.connect(self.addition)
        b_addition.setShortcut("+")

        # multiplication and add multiplication shortcut
        b_multiplication = self.findChild(QPushButton, "b_multiplication")
        b_multiplication.clicked.connect(self.multiplication)
        b_multiplication.setShortcut("*")

        # subtraction and add subtraction shortcut
        b_subtraction = self.findChild(QPushButton, "b_subtraction")
        b_subtraction.clicked.connect(self.subtraction)
        b_subtraction.setShortcut("-")

        # division and add division shortcut
        b_division = self.findChild(QPushButton, "b_division")
        b_division.clicked.connect(self.division)
        b_division.setShortcut("/")

        # pi
        b_pi = self.findChild(QPushButton, "b_pi")
        b_pi.clicked.connect(self.pi_insert)

        # negate
        b_negetive = self.findChild(QPushButton, "b_negetive_2")
        b_negetive.clicked.connect(self.negate)

        # factorial
        b_factorial = self.findChild(QPushButton, "b_factorial")
        b_factorial.clicked.connect(self.factorial)

        # radical 2
        b_radical = self.findChild(QPushButton, "b_radical")
        b_radical.clicked.connect(self.radical)

        # radical x , y
        b_radicalxy = self.findChild(QPushButton, "b_radical_2")
        b_radicalxy.clicked.connect(self.radicalxy)

        # prower x ^ 2
        b_power_2 = self.findChild(QPushButton, "b_power_2")
        b_power_2.clicked.connect(self.power_2)

        # prower x ^ y
        b_power_x_y = self.findChild(QPushButton, "b_power_x_y")
        b_power_x_y.clicked.connect(self.power_x_y)

        # prower 10 ^ x
        b_power_10_x = self.findChild(QPushButton, "b_power_10_x")
        b_power_10_x.clicked.connect(self.power_10_x)

        # sinus
        b_sin = self.findChild(QPushButton, "b_sin")
        b_sin.clicked.connect(self.sin)

        # cosine
        b_cos = self.findChild(QPushButton, "b_cos")
        b_cos.clicked.connect(self.cos)

        # tangent
        b_tan = self.findChild(QPushButton, "b_tan")
        b_tan.clicked.connect(self.tan)

        # logarithm
        b_log = self.findChild(QPushButton, "b_log")
        b_log.clicked.connect(self.log)

        # exp
        b_log_2 = self.findChild(QPushButton, "b_log_2")
        b_log_2.clicked.connect(self.exp)

        # operator button
        self.b_operator = self.findChild(QPushButton, "b_operator")

        # action Github
        actiongithub = self.findChild(QAction, "actiongithub")
        actiongithub.triggered.connect(self.github)

        # action Telegram
        actionTelegram = self.findChild(QAction, "actionTelegram")
        actionTelegram.triggered.connect(self.Telegram)

        # action About
        actionAbout = self.findChild(QAction, "actionAbout")
        actionAbout.triggered.connect(self.About)

        # action exit
        actionExit = self.findChild(QAction, "actionExit")
        actionExit.triggered.connect(self.close)
        b_division.setShortcut("alt+F4")

        # show all the widgets
        self.show()

    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', dirname(abspath(__file__)))
        return join(base_path, relative_path)

    def github(self):
        webbrowser.open("https://github.com/irania9O/")

    def Telegram(self):
        webbrowser.open("https://t.me/irania9O/")

    def About(self):
        msg = QMessageBox()
        msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
        msg.setText("Programmed by : Seyed Ali Kamali \nVersion : 1")
        msg.setWindowTitle("Error")
        msg.exec_()

    def exp(self):
        echo = self.findChild(QLineEdit, "echo")
        value = self.findChild(QLineEdit, "value")
        data = echo.text()
        last_data = value.text()
        try:
            if data == "":
                if last_data != "":
                    self.calculator.exp()
                    value.setText(str(self.calculator.value))
            else:
                new_info = exp(float(data))
                echo.setText(str(new_info))
        except:
            msg = QMessageBox()
            msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
            msg.setIcon(QMessageBox.Critical)
            msg.setText("An error occurred.")
            msg.setWindowTitle("Error")
            msg.exec_()

    def log(self):
        echo = self.findChild(QLineEdit, "echo")
        value = self.findChild(QLineEdit, "value")
        data = echo.text()
        last_data = value.text()
        try:
            if data == "":
                if last_data != "":
                    self.calculator.log10()
                    value.setText(str(self.calculator.value))
            else:
                new_info = log10(float(data))
                echo.setText(str(new_info))
        except:
            msg = QMessageBox()
            msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
            msg.setIcon(QMessageBox.Critical)
            msg.setText("An error occurred.")
            msg.setWindowTitle("Error")
            msg.exec_()

    def tan(self):
        echo = self.findChild(QLineEdit, "echo")
        value = self.findChild(QLineEdit, "value")
        data = echo.text()
        last_data = value.text()
        try:
            if data == "":
                if last_data != "":
                    self.calculator.tan()
                    value.setText(str(self.calculator.value))
            else:
                new_info = tan(float(data))
                echo.setText(str(new_info))
        except:
            msg = QMessageBox()
            msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
            msg.setIcon(QMessageBox.Critical)
            msg.setText("An error occurred.")
            msg.setWindowTitle("Error")
            msg.exec_()

    def cos(self):
        echo = self.findChild(QLineEdit, "echo")
        value = self.findChild(QLineEdit, "value")
        data = echo.text()
        last_data = value.text()
        try:
            if data == "":
                if last_data != "":
                    self.calculator.cos()
                    value.setText(str(self.calculator.value))
            else:
                new_info = cos(float(data))
                echo.setText(str(new_info))
        except:
            msg = QMessageBox()
            msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
            msg.setIcon(QMessageBox.Critical)
            msg.setText("An error occurred.")
            msg.setWindowTitle("Error")
            msg.exec_()

    def sin(self):
        echo = self.findChild(QLineEdit, "echo")
        value = self.findChild(QLineEdit, "value")
        data = echo.text()
        last_data = value.text()
        try:
            if data == "":
                if last_data != "":
                    self.calculator.sin()
                    value.setText(str(self.calculator.value))
            else:
                new_info = sin(float(data))
                echo.setText(str(new_info))
        except:
            msg = QMessageBox()
            msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
            msg.setIcon(QMessageBox.Critical)
            msg.setText("An error occurred.")
            msg.setWindowTitle("Error")
            msg.exec_()

    def power_10_x(self):
        echo = self.findChild(QLineEdit, "echo")
        value = self.findChild(QLineEdit, "value")
        data = echo.text()
        last_data = value.text()
        try:
            if data == "":
                if last_data != "":
                    self.calculator.ten_pow()
                    value.setText(str(self.calculator.value))
            else:
                new_info = pow(10, float(data))
                echo.setText(str(new_info))
        except:
            msg = QMessageBox()
            msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
            msg.setIcon(QMessageBox.Critical)
            msg.setText("An error occurred.")
            msg.setWindowTitle("Error")
            msg.exec_()

    def power_x_y(self):
        self.commiter()
        self.last_func = "power"
        self.b_operator.setText("𝔁ʸ")
        data = self.findChild(QLineEdit, "echo").text()
        if data == "":
            data = 1
        if self.calculator == None:
            number = float(data)
            self.calculator = Calculator(number)

        self.findChild(QLineEdit, "value").setText(str(self.calculator.value))
        self.findChild(QLineEdit, "echo").setText("")

    def power_2(self):
        echo = self.findChild(QLineEdit, "echo")
        value = self.findChild(QLineEdit, "value")
        data = echo.text()
        last_data = value.text()
        try:
            if data == "":
                if last_data != "":
                    self.calculator **= 2
                    value.setText(str(self.calculator.value))
            else:
                new_info = pow(float(data), 2)
                echo.setText(str(new_info))
        except:
            msg = QMessageBox()
            msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
            msg.setIcon(QMessageBox.Critical)
            msg.setText("An error occurred.")
            msg.setWindowTitle("Error")
            msg.exec_()

    def radicalxy(self):
        self.commiter()
        self.last_func = "sqrt"
        self.b_operator.setText("ʸ√𝔁")
        data = self.findChild(QLineEdit, "echo").text()
        if data == "":
            data = 1
        if self.calculator == None:
            number = float(data)
            self.calculator = Calculator(number)

        self.findChild(QLineEdit, "value").setText(str(self.calculator.value))
        self.findChild(QLineEdit, "echo").setText("")

    def radical(self):
        echo = self.findChild(QLineEdit, "echo")
        value = self.findChild(QLineEdit, "value")
        data = echo.text()
        if data == "":
            try:
                if self.calculator.value < 0:
                    raise Exception()
                else:
                    self.calculator.sqrt_2()
                    value.setText(str(self.calculator.value))

            except:
                msg = QMessageBox()
                msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Negative numbers have no roots")
                msg.setWindowTitle("Error")
                msg.exec_()
        else:
            try:
                if float(data) < 0:
                    raise Exception()
                else:
                    new_info = sqrt(float(data))
                    echo.setText(str(new_info))
            except:
                msg = QMessageBox()
                msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Negative numbers have no roots")
                msg.setWindowTitle("Error")
                msg.exec_()

    def factorial(self):
        echo = self.findChild(QLineEdit, "echo")
        value = self.findChild(QLineEdit, "value")
        data = echo.text()
        if data == "":
            try:
                if self.calculator.value > 50000:
                    raise Exception()

                elif int(self.calculator.value) == float(self.calculator.value):
                    self.calculator.factorial()
                    value.setText(str(self.calculator.value))

                else:
                    msg = QMessageBox()
                    msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Accepting positive floats with integral values")
                    msg.setWindowTitle("Error")
                    msg.exec_()
            except:
                msg = QMessageBox()
                msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Overflow")
                msg.setWindowTitle("Error")
                msg.exec_()
        else:
            try:
                if float(data) > 50000:
                    msg = QMessageBox()
                    msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Overflow")
                    msg.setWindowTitle("Error")
                    msg.exec_()

                elif int(data) == float(data):
                    new_info = factorial(int(data))
                    echo.setText(str(new_info))
            except:
                msg = QMessageBox()
                msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Accepting positive floats with integral values")
                msg.setWindowTitle("Error")
                msg.exec_()

    def negate(self):
        echo = self.findChild(QLineEdit, "echo")
        value = self.findChild(QLineEdit, "value")
        last_data = value.text()
        data = echo.text()
        if data == "":
            try:
                self.calculator.negate()
                if "-" in last_data:
                    value.setText(last_data[1:])
                else:
                    value.setText("-" + last_data)
            except:
                pass
        else:
            if "-" in data:
                echo.setText(data[1:])
            else:
                echo.setText("-" + data)

    def pi_insert(self):
        if self.calculator == None:
            number = float(pi)
            self.calculator = Calculator(number)
        self.findChild(QLineEdit, "echo").setText(str(pi))

    def division(self):
        self.commiter()
        self.last_func = "division"
        self.b_operator.setText("÷")
        data = self.findChild(QLineEdit, "echo").text()
        if data == "":
            data = 1
        if self.calculator == None:
            number = float(data)
            self.calculator = Calculator(number)

        self.findChild(QLineEdit, "value").setText(str(self.calculator.value))
        self.findChild(QLineEdit, "echo").setText("")

    def subtraction(self):
        self.commiter()
        self.last_func = "subtraction"
        self.b_operator.setText("-")
        data = self.findChild(QLineEdit, "echo").text()
        if data == "":
            data = 0
        if self.calculator == None:
            number = float(data)
            self.calculator = Calculator(number)

        self.findChild(QLineEdit, "value").setText(str(self.calculator.value))
        self.findChild(QLineEdit, "echo").setText("")

    def multiplication(self):
        self.commiter()
        self.last_func = "multiplication"
        self.b_operator.setText("×")
        data = self.findChild(QLineEdit, "echo").text()
        if data == "":
            data = 1
        if self.calculator == None:
            number = float(data)
            self.calculator = Calculator(number)

        self.findChild(QLineEdit, "value").setText(str(self.calculator.value))
        self.findChild(QLineEdit, "echo").setText("")

    def addition(self):
        self.commiter()
        self.last_func = "addition"
        self.b_operator.setText("+")
        data = self.findChild(QLineEdit, "echo").text()
        if data == "":
            data = 0
        if self.calculator == None:
            number = float(data)
            self.calculator = Calculator(number)

        self.findChild(QLineEdit, "value").setText(str(self.calculator.value))
        self.findChild(QLineEdit, "echo").setText("")

    def commiter(self):
        if self.last_func == "addition":
            data = self.findChild(QLineEdit, "echo").text()
            if data == "":
                data = 0
            self.calculator += float(data)

        elif self.last_func == "multiplication":
            data = self.findChild(QLineEdit, "echo").text()
            if data == "":
                data = 1
            self.calculator *= float(data)

        elif self.last_func == "subtraction":
            data = self.findChild(QLineEdit, "echo").text()
            if data == "":
                data = 0
            self.calculator -= float(data)

        elif self.last_func == "division":
            data = self.findChild(QLineEdit, "echo").text()
            if data == "":
                data = 1
            if float(data) == 0:
                msg = QMessageBox()
                msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Cannot divide by zero!")
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                self.calculator /= float(data)

        elif self.last_func == "sqrt":
            data = self.findChild(QLineEdit, "echo").text()
            if data == "":
                data = 1
            try:
                self.calculator.sqrt_n(int(data))
            except:
                msg = QMessageBox()
                msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Accepting positive floats with integral values")
                msg.setWindowTitle("Error")
                msg.exec_()

        elif self.last_func == "power":
            data = self.findChild(QLineEdit, "echo").text()
            if data == "":
                data = 1
            try:
                self.calculator **= float(data)
            except:
                msg = QMessageBox()
                msg.setWindowIcon(self.resource_path(QIcon("images/calculator_icon.png")))
                msg.setIcon(QMessageBox.Critical)
                msg.setText("An error occurred.")
                msg.setWindowTitle("Error")
                msg.exec_()

    def equal(self):
        if self.calculator != None:
            self.commiter()
            self.last_func = None
            self.b_operator.setText("=")
            self.findChild(QLineEdit, "echo").setText("")
            self.findChild(QLineEdit, "value").setText(str(self.calculator.value))

    def insert_dot(self):
        try:
            echo = self.findChild(QLineEdit, "echo")
            numbers = echo.text()
            if numbers == "":
                echo.setText("0.")
            elif not "." in numbers:
                echo.setText(numbers + ".")
        except Exception as e:
            print(e)

    def insert_number(self, number):
        try:
            echo = self.findChild(QLineEdit, "echo")
            numbers = echo.text()
            data = numbers + str(number)
            if len(data) == 2 and data[1] != "." and data[0] == "0":
                data = data[1:]

            echo.setText(data)

            # count = len( data)
            # if count > 18 :
            #     new_font_size = echo.fontInfo().pointSize() - 1
            #     if new_font_size > 8 :
            #         new_font = echo.font()
            #         new_font.setPointSize(new_font_size)
            #         echo.setFont(new_font)

        except Exception as e:
            print(e)

    def delete_number(self):
        try:
            echo = self.findChild(QLineEdit, "echo")
            echo.setText(echo.text()[:-1])

            if len(echo.text()[:-1]) < 22:
                new_font_size = echo.fontInfo().pointSize() + 1
                if new_font_size < 20:
                    new_font = echo.font()
                    new_font.setPointSize(new_font_size)
                    echo.setFont(new_font)
        except Exception as e:
            print(e)

    def clear_all(self):
        try:
            echo = self.findChild(QLineEdit, "echo")
            self.findChild(QLineEdit, "echo").setText("")
            self.findChild(QLineEdit, "value").setText("")
            self.b_operator.setText("")
            self.calculator = None
            self.last_func = None
        except Exception as e:
            print(e)

    def clear_insert(self):
        try:
            self.findChild(QLineEdit, "echo").setText("")
        except Exception as e:
            print(e)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
