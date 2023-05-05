from PyQt6 import QtCore, QtGui, QtWidgets
from window.WelcomeWindow import Ui_Dialog


class WelcomeWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(WelcomeWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.program_exit)
    def program_exit(self):
        self.close()

def start_program():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()

    sys.exit(app.exec())



start_program()