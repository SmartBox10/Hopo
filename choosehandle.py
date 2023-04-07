from PyQt5 import QtCore, QtGui, QtWidgets
from fileUI1 import Ui_MainWindow1
class MAIN_HANDLE1(Ui_MainWindow1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())