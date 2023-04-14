from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Main1Handle import MAIN1_HANDLE
from Login1Handle import LOGIN1_HANDLE
from UsingHandle import USING_HANDLE
class UI():
    def __init__(self):
        self.mainUI = QMainWindow()
        self.mainHandle = MAIN1_HANDLE(self.mainUI)
        self.mainHandle.Logout.clicked.connect(lambda: self.loadLoginForm(0))
        self.mainHandle.Kept.clicked.connect(lambda:self.loadUsingForm(0))

        self.loginUI = QMainWindow()
        self.loginHandle = LOGIN1_HANDLE(self.loginUI)
        self.loginHandle.ButLog.clicked.connect(lambda: self.loadMainForm(0))


        self.usingUI = QMainWindow()
        self.usingHandle = USING_HANDLE(self.usingUI)
        self.usingHandle.Cont.clicked.connect(lambda: self.loadLoginForm(0))

        self.loginUI.show()
    def loadMainForm(self,data):
        #import hàm g từ trang gì như là cái gì (ghi ở phía trên hoặcở đây cx đcd)
        #thay thết dòng 28 thành hàm đã import và truyền vào hai đối số
        un=self.loginHandle.Ten.text()
        pw=self.loginHandle.Matkhau.text()
        if un=="Co" and pw=="123":
            self.mainUI.show()
            self.loginUI.hide()
            self.usingUI.hide()
        else:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setInformativeText("Sai thông tin đăng nhập. Vui lòng thử lại")
            self.msg.setWindowTitle("Thông báo")
            self.msg.exec_()

    def loadLoginForm(self,data):
        #self.loginHandle.Ten.setText("")
        self.loginHandle.Matkhau.setText("")

        self.loginUI.show()
        self.mainUI.hide()
        self.usingUI.hide()
    def loadUsingForm(self,data):
        self.usingUI.show()
        self.mainUI.hide()
        self.loginUI.hide()







if __name__=="__main__":
    app=QApplication([])
    ui=UI()
    app.exec_()