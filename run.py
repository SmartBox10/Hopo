from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Main1Handle import MAIN1_HANDLE
from Login1Handle import LOGIN1_HANDLE

from choosehandle import CHOOSE_HANDLE

from checkhandle import CHECK_HANDLE
from CodeXuLy import *

class UI():

    def __init__(self):
        self.mainUI = QMainWindow()
        self.mainHandle = MAIN1_HANDLE(self.mainUI)
        self.mainHandle.Logout.clicked.connect(self.loadLoginForm)
        self.mainHandle.Kept.clicked.connect(self.loadChooseForm)

        self.kh1 = Khachhang("K224111388", "123")
        self.kh2 = Khachhang("K224111399", "456")
        self.kh3 = Khachhang("K224111381", "789")
        self.kh1.them_khach_hang()
        self.kh2.them_khach_hang()
        self.kh3.them_khach_hang()
        self.tu1 = Tu("A1", "0")
        self.tu2 = Tu("A2", "0")
        self.tu3 = Tu("A3", "0")
        self.tu1.them_tu()
        self.tu2.them_tu()
        self.tu3.them_tu()

        self.loginUI = QMainWindow()
        self.loginHandle = LOGIN1_HANDLE(self.loginUI)
        self.loginHandle.ButLog.clicked.connect(self.loadMainForm)
        self.loginHandle.showquanity.setText(str(self.tu1.ting_tong_tu_trong()))




        self.chooseUI = QMainWindow()
        self.chooseHandle = CHOOSE_HANDLE(self.chooseUI)
        #self.chooseHandle.logout.clicked.connect(self.chooseHandle.chooseRadio)
        self.chooseHandle.logout.clicked.connect(self.loadLoginForm)


        self.checkUI = QMainWindow()
        self.checkHandle = CHECK_HANDLE(self.checkUI)
        #self.checkHandle.pushButton.clicked.connect(self.ham)
        self.loginUI.show()
    def loadMainForm(self):
        un = self.loginHandle.Ten.text()
        pw = self.loginHandle.Matkhau.text()
        self.khachhang = Khachhang(un, pw)
        ketquadangnhap = self.khachhang.login()
        if ketquadangnhap==1:
            self.mainUI.show()
            self.loginUI.hide()
            self.chooseUI.hide()
        else:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setInformativeText(f"Sai thông tin đăng nhập. Vui lòng thử lại")
            self.msg.setWindowTitle("Thông báo")
            self.msg.exec_()

    def loadLoginForm(self):
        self.loginHandle.Ten.setText("")
        self.loginHandle.Matkhau.setText("")
        self.loginUI.show()
        self.mainUI.hide()
        self.chooseUI.hide()

    def loadChooseForm(self):
        self.chooseUI.show()
        self.mainUI.hide()
        self.loginUI.hide()
    #def ham(self):
        #code = self.checkHandle.plainTextEdit.text()
        #self.
        #if self.  =0 :
            #self.loginUI.show()
            #self.mainUI.hide()
            #self.checkUI.hide()

        #else:
            #self.m = QtWidgets.QMessageBox()
            #self.m.setIcon(QtWidgets.QMessageBox.Information)
            #self.m.setInformativeText(f"Sai mã. Vui lòng thử lại")
            #self.m.setWindowTitle("Thông báo")
            #self.m.exec_()











if __name__=="__main__":
    app=QApplication([])
    ui=UI()
    app.exec_()