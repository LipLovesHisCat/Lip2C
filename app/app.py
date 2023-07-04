from PyQt6 import QtCore, QtGui, QtWidgets
from window.WelcomeWindow import Ui_Dialog_1
from window.SelectionWindow import Ui_Dialog_2
from window.CommonInfo import Ui_MainWindow_1
from window.ExitWindow import Ui_Dialog_Quit
from window.CancelWindow import Ui_Dialog_Cancel
from window.PPX2 import Ui_MainWindow_PPX

lst = []
dct = dict.fromkeys(['kid_surname', 'kid_name', 'kid_lastname', 'kid_birth_date', 'kid_class_num', 'kid_class_letter', 'kid_date_of_start_study','address_town',  'address_street',  'address_house_number','address_flat_number', 'sex', 'family', 'mum_surname','mum_name', 'mum_lastname', 'mum_phone_number', 'pater_name','pater_lastname', 'pater_surname',  'pater_phone_number'], None)
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

        # for i, j in enumerate(dct):
        #     a = 'self.textEdit_' + f'{i+1}' + f'.toPlainText()'
        #
        #     dct[j] = self.textEdit_1.toPlainText()
        items = [self.textEdit_1.toPlainText(), self.textEdit_2.toPlainText(), self.textEdit_3.toPlainText(),self.textEdit_4.toPlainText(),self.textEdit_5.toPlainText(), self.textEdit_6.toPlainText(), self.textEdit_10.toPlainText(), self.textEdit_7.toPlainText(), self.textEdit_9.toPlainText(), self.textEdit_8.toPlainText(), self.textEdit_11.toPlainText(), sex, full_of_family, self.textEdit_14.toPlainText(), self.textEdit_12.toPlainText(), self.textEdit_13.toPlainText(), self.textEdit_18.toPlainText(), self.textEdit_16.toPlainText(),self.textEdit_17.toPlainText(),self.textEdit_15.toPlainText(),self.textEdit_19.toPlainText()]

        for key, value in zip(dct, items):
            dct[key] = value


    # def program_exit(self):
    #     self.close()
    def show_PPX2(self):
        self.get_common_window_info()
        self.Dialog_PXX2 = PPX2()
        self.Dialog_PXX2.show()
        self.flag = False
        # self.get_common_window_info()
        self.close()
        # print(dct)
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
        if dct['sex'] == 'М':
            sex = self.Main_Window_1.radioButton
        else:
            sex = self.Main_Window_1.radioButton_2

        if dct['family'] == 'Полная':
            full_of_family = self.Main_Window_1.radioButton_3
        else:
            full_of_family = self.Main_Window_1.radioButton_4
        # print(type(self.Main_Window_1.radioButton), type(self.Main_Window_1.textEdit_1))
        # setChecked(True)
        l = [self.Main_Window_1.textEdit_1,  self.Main_Window_1.textEdit_2,  self.Main_Window_1.textEdit_3, self.Main_Window_1.textEdit_4, self.Main_Window_1.textEdit_5,  self.Main_Window_1.textEdit_6,  self.Main_Window_1.textEdit_10,  self.Main_Window_1.textEdit_7,  self.Main_Window_1.textEdit_9,  self.Main_Window_1.textEdit_8,  self.Main_Window_1.textEdit_11,  sex, full_of_family, self.Main_Window_1.textEdit_14,  self.Main_Window_1.textEdit_12,  self.Main_Window_1.textEdit_13,  self.Main_Window_1.textEdit_18,  self.Main_Window_1.textEdit_16, self.Main_Window_1.textEdit_17, self.Main_Window_1.textEdit_15, self.Main_Window_1.textEdit_19]
        for key, i in zip(dct.keys(), range(len(l))):
            if isinstance(l[i], QtWidgets.QTextEdit):
                l[i].setText(dct[key])
            else:
                l[i].setChecked(True)


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
