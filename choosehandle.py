from PyQt5 import QtCore, QtGui, QtWidgets
from choose import Ui_MainWindow1
from CodeXuLy import Tu
class CHOOSE_HANDLE(Ui_MainWindow1,Tu):
    def __init__(self,mainwindow):
        self.setupUi(mainwindow)
        self.logout.clicked.connect(self.chooseRadio)

    def chooseRadio(self):
        if self.A1.isChecked() == True:
            self.list.append(self.A1)
            tu1 = Tu("A1", "trong")
            tu1.them_tu()
        elif self.A2.isChecked() == True:
            self.list.append(self.A2)
            self.danh_sach_tu_dang_su_dung.append('A2')
        elif self.A3.isChecked() == True:
            self.list.append(self.A3)
            self.danh_sach_tu_dang_su_dung.append('A3')
        elif self.A4.isChecked() == True:
            self.list.append(self.A4)
            self.danh_sach_tu_dang_su_dung.append('A4')
        elif self.A5.isChecked() == True:
            self.list.append(self.A5)
            self.danh_sach_tu_dang_su_dung.append('A5')
        elif self.B1.isChecked() == True:
            self.list.append(self.B1)
            self.danh_sach_tu_dang_su_dung.append('B1')
        elif self.B2.isChecked() == True:
            self.list.append(self.B2)
            self.danh_sach_tu_dang_su_dung.append('B2')
        elif self.B3.isChecked() == True:
            self.list.append(self.B3)
            self.danh_sach_tu_dang_su_dung.append('B3')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())