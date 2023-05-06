from PyQt6 import QtCore, QtGui, QtWidgets
from window.WelcomeWindow import Ui_Dialog_1
from window.SelectionWindow import Ui_Dialog_2
from window.CommonInfo import Ui_MainWindow_1
from window.ExitWindow import Ui_Dialog_Quit

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
        self.pushButton_5.clicked.connect(self.show_common_info)

    def show_common_info(self):
        self.MainWindow_1 = CommonInfo()
        self.MainWindow_1.show()
        self.close()


class CommonInfo(QtWidgets.QMainWindow, Ui_MainWindow_1):
    def __init__(self, parent=None):
        super(CommonInfo, self).__init__(parent)
        self.setupUi(self)
        # self.pushButton_4.clicked.connect(self.program_exit)
        self.pushButton_4.clicked.connect(self.exit_window)
        self.pushButton_2.clicked.connect(self.show_selection_window)
        self.pushButton.clicked.connect(self.show_selection_window)

    # def program_exit(self):
    #     self.close()

    def exit_window(self):
        self.Dialog_3 = ExitWindow()
        self.Dialog_3.show()


    def show_selection_window(self):
        self.Dialog_2 = SelectionWindow()
        self.Dialog_2.show()
        self.close()


class ExitWindow(QtWidgets.QDialog, Ui_Dialog_Quit):
    def __init__(self, parent=None):
        super(ExitWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(exit)


    # def program_exit(self):
    #     self.close()
def start_program():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()

    sys.exit(app.exec())


start_program()
