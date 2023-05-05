from PyQt6 import QtCore, QtGui, QtWidgets
from window.WelcomeWindow import Ui_Dialog_1
from window.SelectionWindow import Ui_Dialog_2


class WelcomeWindow(QtWidgets.QDialog, Ui_Dialog_1):
    def __init__(self, parent=None):
        super(WelcomeWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_selection_window)
        self.pushButton_2.clicked.connect(self.program_exit)

    def program_exit(self):
        self.close()
    def show_selection_window(self):
        self.Dialog_2 = SelectionWindow()
        self.Dialog_2.show()
        self.close()

class SelectionWindow(QtWidgets.QDialog, Ui_Dialog_2):
    def __init__(self, parent=None):
        super(SelectionWindow, self).__init__()
        self.setupUi(self)

def start_program():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()

    sys.exit(app.exec())
start_program()
