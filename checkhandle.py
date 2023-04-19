from PyQt5 import QtCore, QtGui, QtWidgets
from check import Ui_MainWindow
class CHECK_HANDLE(Ui_MainWindow):
    def __init__(self,mainwindow):
        self.setupUi(mainwindow)
        #----------------------
        self.plainTextEdit.setPlainText("NHAP MA")


    def ham(self):
        code = self.plainTextEdit.toPlainText()
        if code == str(12345):
            return 0

        else:
            return 1
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MAIN_HANDLE()
    MainWindow.show()
    sys.exit(app.exec_())