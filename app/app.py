from PyQt6 import QtCore, QtGui, QtWidgets
from window.WelcomeWindow import Ui_Dialog_1
from window.SelectionWindow import Ui_Dialog_2
from window.CommonInfo import Ui_MainWindow_1
from window.ExitWindow import Ui_Dialog_Quit
from window.CancelWindow import Ui_Dialog_Cancel


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
        self.flag = True
        # self.pushButton_4.clicked.connect(self.program_exit)
        self.pushButton_4.clicked.connect(self.exit_window)
        self.pushButton_2.clicked.connect(self.cancel_window)  # кнопка назад
        self.pushButton.clicked.connect(self.cancel_window)  # кнопка отмена

    # def program_exit(self):
    #     self.close()

    def exit_window(self):

        self.Dialog_3 = ExitWindow()
        self.Dialog_3.exec()

    def show_selection_window(self):
        self.Dialog_2 = SelectionWindow()
        self.Dialog_2.show()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        if self.flag == True:
            a0.ignore()
            self.exit_window()
        else:
            a0.accept()

    def cancel_window(self):
        self.Dialog_4 = CancelWindow()
        self.Dialog_4.show()

    def get_common_window_info(self):
        kid_surname = self.textEdit.text()
        kid_name = self.textEdit_2.text()
        kid_lastname = self.textEdit_3.text()
        kid_birth_date = self.textEdit_4.text()
        kid_class_num = self.textEdit_5.text()
        kid_class_letter = self.textEdit_6.text()
        kid_date_of_start_study = self.textEdit_10.text()
        address_town = self.textEdit_7.text()
        address_street = self.textEdit_9.text()
        address_house_number = self.textEdit_8.text()
        adress_flat_number = self.textEdit_11.text()

        sex = 'None'
        if self.radioButton.isChecked():
            sex = 'M'
        elif self.radioButton_2.isChecked():
            sex = 'Ж'

        full_of_family = 'None'
        if self.radioButton_3.isChecked():
            full_of_family = 'Полная'
        elif self.radioButton_4.isChecked():
            full_of_family = 'Неполная'

        mum_surname = self.textEdit_14.text()
        mun_name = self.textEdit_12.text()
        mun_lastname = self.textEdit_13.text()
        mun_phone_number = self.textEdit_18.text()

        pater_surname = self.textEdit_16.text()
        pater_name = self.textEdit_17.text()
        pater_lastname = self.textEdit_15.text()
        pater_phone_number = self.textEdit_19.text()


class ExitWindow(QtWidgets.QDialog, Ui_Dialog_Quit):
    def __init__(self, parent=None):
        super(ExitWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(exit)

    # def program_exit(self):
    #     self.close()


class CancelWindow(QtWidgets.QDialog, Ui_Dialog_Cancel):
    def __init__(self, parent=None):
        super(CancelWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.back_to_selection_window)

    def back_to_selection_window(self):
        self.bact_step = CommonInfo()
        self.bact_step.flag = False
        self.bact_step.close()
        self.Dialog_4 = SelectionWindow()
        self.Dialog_4.show()
        self.close()



def start_program():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()

    sys.exit(app.exec())


start_program()
