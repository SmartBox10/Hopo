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
      self.kh4 = Khachhang("K224111378", "246")
      self.kh5 = Khachhang("K224060788", "357")
      self.kh1.them_khach_hang()
      self.kh2.them_khach_hang()
      self.kh3.them_khach_hang()
      self.kh4.them_khach_hang()
      self.kh5.them_khach_hang()
      self.tu1 = Tu("A1", "0")
      self.tu2 = Tu("A2", "0")
      self.tu3 = Tu("A3", "0")
      self.tu4 = Tu("B1", "0")
      self.tu5 = Tu("B2", "0")
      self.tu1.them_tu()
      self.tu2.them_tu()
      self.tu3.them_tu()
      self.tu4.them_tu()
      self.tu5.them_tu()

      self.loginUI = QMainWindow()
      self.loginHandle = LOGIN1_HANDLE(self.loginUI)
      self.loginHandle.ButLog.clicked.connect(self.loadMainForm)

      self.chooseUI = QMainWindow()
      self.chooseHandle = CHOOSE_HANDLE(self.chooseUI)
      self.chooseHandle.logout.clicked.connect(self.loadLoginForm1)

      self.checkUI = QMainWindow()
      self.checkHandle = CHECK_HANDLE(self.checkUI)

      self.loginUI.show()
      self.loginHandle.showquanity.setText(str(self.tu1.ting_tong_tu_trong()))
      self.mainHandle.Return.clicked.connect(self.checkout)
  def loadMainForm(self):
      un = self.loginHandle.Ten.text()
      pw = self.loginHandle.Matkhau.text()
      self.khachhang = Khachhang(un, pw)
      ketquadangnhap = self.khachhang.login()
      self.loginHandle.showquanity.setText(str(self.tu1.ting_tong_tu_trong()))


      if ketquadangnhap==1:
          self.mainUI.show()
          self.loginUI.hide()
          self.chooseUI.hide()
          if self.khachhang.ten_dang_nhap == self.kh1.ten_dang_nhap:
              self.khachhang = self.kh1
          elif self.khachhang.ten_dang_nhap == self.kh2.ten_dang_nhap:
              self.khachhang = self.kh2
          elif self.khachhang.ten_dang_nhap == self.kh3.ten_dang_nhap:
              self.khachhang = self.kh3
          elif self.khachhang.ten_dang_nhap == self.kh4.ten_dang_nhap:
              self.khachhang = self.kh4
          elif self.khachhang.ten_dang_nhap == self.kh5.ten_dang_nhap:
              self.khachhang = self.kh5
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
      self.checkUI.hide()


  def loadChooseForm(self):
      self.chooseUI.show()
      self.mainUI.hide()
      self.loginUI.hide()
      self.checkUI.hide()
  def loadcheckForm(self):
      self.chooseUI.hide()
      self.mainUI.hide()
      self.loginUI.hide()
      self.checkUI.show()


  def loadLoginForm1(self):
      if self.chooseHandle.A1.isChecked() == True:
          self.matu="A1"
      elif self.chooseHandle.A2.isChecked() == True:
          self.matu = "A2"
      elif self.chooseHandle.A3.isChecked() == True:
          self.matu = "A3"
      elif self.chooseHandle.B1.isChecked() == True:
          self.matu = "B1"
      elif self.chooseHandle.B2.isChecked() == True:
          self.matu = "B2"

      if chon_tu(self.matu,self.khachhang)== 1:
          self.loginHandle.Ten.setText("")
          self.loginHandle.Matkhau.setText("")
          if self.matu=="A1":
              self.chooseHandle.list.append(self.chooseHandle.A1)
          elif self.matu=="A2":
              self.chooseHandle.list.append(self.chooseHandle.A2)
          elif self.matu=="A3":
              self.chooseHandle.list.append(self.chooseHandle.A3)
          elif self.matu == "B1":
              self.chooseHandle.list.append(self.chooseHandle.B1)
          elif self.matu == "B2":
              self.chooseHandle.list.append(self.chooseHandle.B2)
          self.chooseHandle.hide_tu()
          self.loadLoginForm()
          self.loginHandle.showquanity.setText(str(self.tu1.ting_tong_tu_trong()))


      else: #khách hàng đang sử dụng tủ khác. quay về trang login
          self.mg = QtWidgets.QMessageBox()
          self.mg.setIcon(QtWidgets.QMessageBox.Information)
          self.mg.setInformativeText("Bạn đang sử dụng tủ khác")
          self.mg.setWindowTitle("Thông báo")
          self.mg.exec_()
          self.loadLoginForm()
          self.loginHandle.showquanity.setText(str(self.tu1.ting_tong_tu_trong()))


  def kq(self):
      un = self.loginHandle.Ten.text()
      pw = self.loginHandle.Matkhau.text()
      self.khachhang = Khachhang(un, pw)
      ketquadangnhap = self.khachhang.login()
      if ketquadangnhap == 1:
          self.mainUI.show()
          self.loginUI.hide()
          self.chooseUI.hide()
          if self.khachhang.ten_dang_nhap == self.kh1.ten_dang_nhap:
              self.khachhang = self.kh1
          elif self.khachhang.ten_dang_nhap == self.kh2.ten_dang_nhap:
              self.khachhang = self.kh2
          elif self.khachhang.ten_dang_nhap == self.kh3.ten_dang_nhap:
              self.khachhang = self.kh3
          elif self.khachhang.ten_dang_nhap == self.kh4.ten_dang_nhap:
              self.khachhang = self.kh4
          elif self.khachhang.ten_dang_nhap == self.kh5.ten_dang_nhap:
              self.khachhang = self.kh5


      kq = tra_tu1(self.checkHandle.ma_dinh_danh.text(), self.khachhang)
      if kq == 2:  # nhập đúng mã định danh
          self.loginHandle.showquanity.setText(str(self.tu1.ting_tong_tu_trong()))
          self.checkHandle.ma_dinh_danh.setText("")
          self.loadLoginForm()
          for tu in self.tu1.TuList:
              if tu.trang_thai == '0':
                  if tu.ma_tu == 'A1':
                      self.chooseHandle.list1.append(self.chooseHandle.A1)
                  elif tu.ma_tu == 'A2':
                      self.chooseHandle.list1.append(self.chooseHandle.A2)
                  elif tu.ma_tu=='A3':
                      self.chooseHandle.list1.append(self.chooseHandle.A3)
                  elif tu.ma_tu == 'B1':
                      self.chooseHandle.list1.append(self.chooseHandle.B1)
                  elif tu.ma_tu == 'B2':
                      self.chooseHandle.list1.append(self.chooseHandle.B2)


          self.chooseHandle.show_tu()
      elif kq==4:#nhập sai mã định danh
          self.checkHandle.label.setText("Sai mã. Vui lòng thử lại")
          self.checkHandle.check_ma.clicked.connect(self.kq)


  def checkout(self):
      un = self.loginHandle.Ten.text()
      pw = self.loginHandle.Matkhau.text()
      self.khachhang = Khachhang(un, pw)
      ketquadangnhap = self.khachhang.login()
      self.loginHandle.showquanity.setText(str(self.tu1.ting_tong_tu_trong()))


      if ketquadangnhap == 1:
          self.mainUI.show()
          self.loginUI.hide()
          self.chooseUI.hide()
          if self.khachhang.ten_dang_nhap == self.kh1.ten_dang_nhap:
              self.khachhang = self.kh1
          elif self.khachhang.ten_dang_nhap == self.kh2.ten_dang_nhap:
              self.khachhang = self.kh2
          elif self.khachhang.ten_dang_nhap == self.kh3.ten_dang_nhap:
              self.khachhang = self.kh3
          elif self.khachhang.ten_dang_nhap == self.kh4.ten_dang_nhap:
              self.khachhang = self.kh4
          elif self.khachhang.ten_dang_nhap == self.kh5.ten_dang_nhap:
              self.khachhang = self.kh5

      if tra_tu(self.khachhang) == 1:  # trả đúng thời gian quy định
          self.m2 = QtWidgets.QMessageBox()
          self.m2.setIcon(QtWidgets.QMessageBox.Information)
          self.m2.setInformativeText("Cảm ơn bạn đã tin dùng dịch vụ. Hẹn lại")
          self.m2.setWindowTitle("Thông báo")
          self.m2.exec_()
          self.loadLoginForm()
          self.loginHandle.showquanity.setText(str(self.tu1.ting_tong_tu_trong()))
          for tu in self.tu1.TuList:
              if tu.trang_thai == '0':
                  if tu.ma_tu == 'A1':
                      self.chooseHandle.list1.append(self.chooseHandle.A1)
                  elif tu.ma_tu == 'A2':
                      self.chooseHandle.list1.append(self.chooseHandle.A2)
                  elif tu.ma_tu=='A3':
                      self.chooseHandle.list1.append(self.chooseHandle.A3)
                  elif tu.ma_tu == 'B1':
                      self.chooseHandle.list1.append(self.chooseHandle.B1)
                  elif tu.ma_tu == 'B2':
                      self.chooseHandle.list1.append(self.chooseHandle.B2)
          self.chooseHandle.show_tu()
      elif tra_tu(self.khachhang) == 0:  # khách hàng chưa có đặt tu, hiện ms rồi nhập lại
          self.m3 = QtWidgets.QMessageBox()
          self.m3.setIcon(QtWidgets.QMessageBox.Information)
          self.m3.setInformativeText("Khách hàng chưa đặt tủ. Vui lòng thử lại")
          self.m3.setWindowTitle("Thông báo")
          self.m3.exec_()
          self.loadLoginForm()
      else:#lố thời gian
          print(self.khachhang.ma_dinh_danh)
          self.m7 = QtWidgets.QMessageBox()
          self.m7.setIcon(QtWidgets.QMessageBox.Information)
          self.m7.setInformativeText(f"Thanh toán {self.khachhang.tien_phai_tra} VND để nhận mã mở tủ")
          self.m7.setWindowTitle("Thông báo")
          self.m7.exec_()

          self.loadcheckForm()
          self.checkHandle.label.setText("Nhập mã được cung cấp")
          self.checkHandle.check_ma.clicked.connect(self.kq)


if __name__=="__main__":
  app=QApplication([])
  ui=UI()
  app.exec_()
