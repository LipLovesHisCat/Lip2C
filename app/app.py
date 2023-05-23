from PyQt6 import QtCore, QtGui, QtWidgets
from window.WelcomeWindow import Ui_Dialog_1
from window.SelectionWindow import Ui_Dialog_2
from window.CommonInfo import Ui_MainWindow_1
from window.ExitWindow import Ui_Dialog_Quit
from window.CancelWindow import Ui_Dialog_Cancel
from window.PPX2 import Ui_MainWindow_PPX

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
        self.pushButton_3.clicked.connect(self.show_PPX2)      # кнопка вперед

    # def program_exit(self):
    #     self.close()
    def show_PPX2(self):
        self.Dialog_PXX2 = PPX2()
        self.Dialog_PXX2.show()
        self.flag = False
        self.close()
    def exit_window(self):

        self.Dialog_3 = ExitWindow()
        self.Dialog_3.show()

    def show_selection_window(self):
        self.Dialog_2 = SelectionWindow()
        self.Dialog_2.show()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        if self.flag == True:
            a0.ignore()
            self.exit_window()
            # self.close()
        else:
            a0.accept()

    def cancel_window(self):
        self.Dialog_4 = CancelWindow()

        self.Dialog_4.show()

        self.Dialog_4.pushButton_228.clicked.connect(self.on_exit_click)  #
        self.Dialog_4.pushButton_111.clicked.connect(self.on_cancel_click)

    def on_cancel_click(self):
        self.Dialog_4.close()

    def on_exit_click(self):
        self.flag = False
        self.Dialog_4.close()
        self.show_selection_window()
        self.close()

    def get_common_window_info(self):

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

        dct = {'kid_surname': self.textEdit.text(),
               'kid_name': self.textEdit_2.text(),
               'kid_lastname': self.textEdit_3.text(),
               'kid_birth_date': self.textEdit_4.text(),
               'kid_class_num': self.textEdit_5.text(),
               'kid_class_letter': self.textEdit_6.text(),
               'kid_date_of_start_study': self.textEdit_10.text(),
               'address_town': self.textEdit_7.text(),
               'address_street': self.textEdit_9.text(),
               'address_house_number': self.textEdit_8.text(),
               'address_flat_number': self.textEdit_11.text(),
               'sex': sex,
               'full_of_family': full_of_family,
               'mum_surname': self.textEdit_14.text(),
               'mum_name': self.textEdit_12.text(),
               'mum_lastname': self.textEdit_13.text(),
               'mum_phone_number': self.textEdit_18.text(),

               'pater_surname': self.textEdit_16.text(),
               'pater_name': self.textEdit_17.text(),
               'pater_lastname': self.textEdit_15.text(),
               'pater_phone_number': self.textEdit_19.text(),
               }
        return dct

class PPX2(QtWidgets.QMainWindow, Ui_MainWindow_PPX):
    def __init__(self, parent=None):
        super(PPX2, self).__init__()
        self.setupUi(self)
        self.flag = True
        self.pushButton.clicked.connect(self.exit_window)      #Exit
        self.pushButton_2.clicked.connect(self.cancel_window)     #Cancel
        self.pushButton_3.clicked.connect(self.show_common_info)  #Back
        # self.pushButton_4.clicked.connect()  #Forward

    def exit_window(self):
        self.Dialog_3 = ExitWindow()
        self.Dialog_3.show()

    def cancel_window(self):
        self.Dialog_4 = CancelWindow()

        self.Dialog_4.show()

        self.Dialog_4.pushButton_228.clicked.connect(self.on_exit_click)  #
        self.Dialog_4.pushButton_111.clicked.connect(self.on_cancel_click)
    def on_cancel_click(self):
        self.Dialog_4.close()

    def on_exit_click(self):

        self.Dialog_4.close()
        self.show_selection_window()
        self.close()
    def show_selection_window(self):
        self.flag=False
        self.Dialog_2 = SelectionWindow()
        self.Dialog_2.show()

    def show_common_info(self):
        self.flag = False
        self.Main_Window_1 = CommonInfo()
        self.Main_Window_1.show()
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        if self.flag == True:
            a0.ignore()
            self.exit_window()
            # self.close()
        else:
            a0.accept()
class ExitWindow(QtWidgets.QDialog, Ui_Dialog_Quit):
    def __init__(self, parent=None):
        super(ExitWindow, self).__init__()
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(exit)

    # def program_exit(self):
    #     self.close()


class CancelWindow(QtWidgets.QDialog, Ui_Dialog_Cancel):
    def __init__(self, parent=None):
        super(CancelWindow, self).__init__()
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)


def start_program():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()

    sys.exit(app.exec())


start_program()
