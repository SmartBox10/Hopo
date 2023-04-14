from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Main1Handle import MAIN1_HANDLE
from Login1Handle import LOGIN1_HANDLE
from UsingHandle import USING_HANDLE


from CodeXuLy import *

class UI():
    def __init__(self):
        self.mainUI = QMainWindow()
        self.mainHandle = MAIN1_HANDLE(self.mainUI)
        self.mainHandle.Logout.clicked.connect(self.loadLoginForm)
        self.mainHandle.Kept.clicked.connect(self.loadUsingForm)

        self.loginUI = QMainWindow()
        self.loginHandle = LOGIN1_HANDLE(self.loginUI)
        self.loginHandle.ButLog.clicked.connect(self.loadMainForm)


        self.usingUI = QMainWindow()
        self.usingHandle = USING_HANDLE(self.usingUI)
        self.usingHandle.Cont.clicked.connect(self.loadLoginForm)


        self.loginUI.show()
    def loadMainForm(self):
        #import hàm g từ trang gì như là cái gì (ghi ở phía trên hoặcở đây cx đcd)
        #thay thết dòng 28 thành hàm đã import và truyền vào hai đối số
        un = self.loginHandle.Ten.text()
        pw = self.loginHandle.Matkhau.text()
        self.Khachhang = Khachhang(un, pw)
        ketquadangnhap = self.Khachhang.login()
        if ketquadangnhap==0: #bien kq=0
            self.mainUI.show()
            self.loginUI.hide()
            self.usingUI.hide()
        else:
            #bien kq=1
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setInformativeText(f"Sai thông tin đăng nhập. Vui lòng thử lại")
            self.msg.setWindowTitle("Thông báo")
            self.msg.exec_()

    def loadLoginForm(self):
        #self.loginHandle.Ten.setText("")
        self.loginHandle.Matkhau.setText("")

        self.loginUI.show()
        self.mainUI.hide()
        self.usingUI.hide()
    def loadUsingForm(self):
        self.usingUI.show()
        self.mainUI.hide()
        self.loginUI.hide()







if __name__=="__main__":
    app=QApplication([])
    ui=UI()
    app.exec_()