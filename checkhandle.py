from PyQt5 import QtCore, QtGui, QtWidgets
from fileUI import Ui_MainWindow
class MAIN_HANDLE(Ui_MainWindow):
    def __init__(self):
        self.setupUi(MainWindow)
        #----------------------
        self.plainTextEdit.setPlainText("NHAP MA")
        self.pushButton.clicked.connect(self.ham)

    def ham(self):
        code = self.plainTextEdit.toPlainText()
        if code == str(12345):
            self.label.setText("success")

        else:
            self.label.setText("fail")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MAIN_HANDLE()
    MainWindow.show()
    sys.exit(app.exec_())