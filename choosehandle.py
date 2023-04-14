from PyQt5 import QtCore, QtGui, QtWidgets
from choose import Ui_MainWindow1
class MAIN_HANDLE1(Ui_MainWindow1):
    def __init__(self):
        self.setupUi(MainWindow)
        self.logout.clicked.connect(self.chooseRadio)

    def chooseRadio(self):
        if self.A1.isChecked() == True:
            self.list.append(self.A1)
        elif self.A2.isChecked() == True:
            self.list.append(self.A2)
        elif self.A3.isChecked() == True:
            self.list.append(self.A3)
        elif self.A4.isChecked() == True:
            self.list.append(self.A4)
        elif self.A5.isChecked() == True:
            self.list.append(self.A5)
        elif self.B1.isChecked() == True:
            self.list.append(self.B1)
        elif self.B2.isChecked() == True:
            self.list.append(self.B2)
        elif self.B3.isChecked() == True:
            self.list.append(self.B3)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())