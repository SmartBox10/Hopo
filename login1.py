# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 345)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LabelTen = QtWidgets.QLabel(self.centralwidget)
        self.LabelTen.setGeometry(QtCore.QRect(90, 130, 101, 51))
        self.LabelTen.setIndent(9)
        self.LabelTen.setObjectName("LabelTen")
        self.ButLog = QtWidgets.QPushButton(self.centralwidget)
        self.ButLog.setGeometry(QtCore.QRect(280, 230, 75, 23))
        self.ButLog.setObjectName("ButLog")
        self.LabelMk = QtWidgets.QLabel(self.centralwidget)
        self.LabelMk.setGeometry(QtCore.QRect(110, 190, 71, 21))
        self.LabelMk.setObjectName("LabelMk")
        self.Ten = QtWidgets.QLineEdit(self.centralwidget)
        self.Ten.setGeometry(QtCore.QRect(210, 140, 211, 31))
        self.Ten.setObjectName("Ten")
        self.Matkhau = QtWidgets.QLineEdit(self.centralwidget)
        self.Matkhau.setGeometry(QtCore.QRect(210, 180, 211, 31))
        self.Matkhau.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Matkhau.setObjectName("Matkhau")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.showquanity = QtWidgets.QLabel(self.centralwidget)
        self.showquanity.setGeometry(QtCore.QRect(290, 90, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.showquanity.setFont(font)
        self.showquanity.setText("")
        self.showquanity.setObjectName("showquanity")
        self.LabHp = QtWidgets.QLabel(self.centralwidget)
        self.LabHp.setGeometry(QtCore.QRect(240, 10, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.LabHp.setFont(font)
        self.LabHp.setObjectName("LabHp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LabelTen.setText(_translate("MainWindow", "Tên đăng nhập"))
        self.ButLog.setText(_translate("MainWindow", "Login"))
        self.LabelMk.setText(_translate("MainWindow", "Mật khẩu"))
        self.label.setText(_translate("MainWindow", "Số tủ còn trống"))
        self.LabHp.setText(_translate("MainWindow", "HOPO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
