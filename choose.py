# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    list=[]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 273)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.A1 = QtWidgets.QRadioButton(self.centralwidget)
        self.A1.setGeometry(QtCore.QRect(130, 40, 62, 14))
        self.A1.setObjectName("A1")
        self.A2 = QtWidgets.QRadioButton(self.centralwidget)
        self.A2.setGeometry(QtCore.QRect(130, 60, 62, 14))
        self.A2.setObjectName("A2")
        self.B1 = QtWidgets.QRadioButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(210, 40, 62, 14))
        self.B1.setObjectName("B1")
        self.B2 = QtWidgets.QRadioButton(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(210, 60, 62, 14))
        self.B2.setObjectName("B2")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(290, 40, 62, 14))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(290, 60, 62, 14))
        self.radioButton_6.setObjectName("radioButton_6")
        self.A3 = QtWidgets.QRadioButton(self.centralwidget)
        self.A3.setGeometry(QtCore.QRect(130, 80, 62, 14))
        self.A3.setObjectName("A3")
        self.B3 = QtWidgets.QRadioButton(self.centralwidget)
        self.B3.setGeometry(QtCore.QRect(210, 80, 62, 14))
        self.B3.setObjectName("B3")
        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_9.setGeometry(QtCore.QRect(290, 80, 62, 14))
        self.radioButton_9.setObjectName("radioButton_9")
        self.B4 = QtWidgets.QRadioButton(self.centralwidget)
        self.B4.setGeometry(QtCore.QRect(210, 100, 62, 14))
        self.B4.setObjectName("B4")
        self.radioButton_12 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_12.setGeometry(QtCore.QRect(290, 100, 62, 14))
        self.radioButton_12.setObjectName("radioButton_12")
        self.A4 = QtWidgets.QRadioButton(self.centralwidget)
        self.A4.setGeometry(QtCore.QRect(130, 100, 62, 14))
        self.A4.setObjectName("A4")
        self.A5 = QtWidgets.QRadioButton(self.centralwidget)
        self.A5.setGeometry(QtCore.QRect(130, 120, 62, 14))
        self.A5.setObjectName("A5")
        self.B5 = QtWidgets.QRadioButton(self.centralwidget)
        self.B5.setGeometry(QtCore.QRect(210, 120, 62, 14))
        self.B5.setObjectName("B5")
        self.radioButton_15 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_15.setGeometry(QtCore.QRect(290, 120, 62, 14))
        self.radioButton_15.setObjectName("radioButton_15")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(180, 150, 81, 21))
        self.logout.setObjectName("logout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 511, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow ):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.A1.setText(_translate("MainWindow", "A1"))
        self.A2.setText(_translate("MainWindow", "A2"))
        self.B1.setText(_translate("MainWindow", "B1"))
        self.B2.setText(_translate("MainWindow", "B2"))
        self.radioButton_5.setText(_translate("MainWindow", "C1"))
        self.radioButton_6.setText(_translate("MainWindow", "C2"))
        self.A3.setText(_translate("MainWindow", "A3"))
        self.B3.setText(_translate("MainWindow", "B3"))
        self.radioButton_9.setText(_translate("MainWindow", "C3"))
        self.B4.setText(_translate("MainWindow", "B4"))
        self.radioButton_12.setText(_translate("MainWindow", "C4"))
        self.A4.setText(_translate("MainWindow", "A4"))
        self.A5.setText(_translate("MainWindow", "A5"))
        self.B5.setText(_translate("MainWindow", "B5"))
        self.radioButton_15.setText(_translate("MainWindow", "C5"))
        self.logout.setText(_translate("MainWindow", "GIỮ ĐỒ"))

        for i in self.list:
            i.hide()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
