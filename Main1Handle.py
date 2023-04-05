from PyQt5 import QtWidgets
from main1 import Ui_MainWindow
class MAIN1_HANDLE(Ui_MainWindow):
    def __init__(self,mainwindow):
        #tạo cái thuocj tính tinhs thời gian. bằng lúc bấm nút gửi đồ với lấy đồ ra
        self.setupUi(mainwindow)
        #self.Kept.clicked.connect(self.messeage1)
        self.Return.clicked.connect(self.messeage2)
    def messeage1(self):
        self.msg1 = QtWidgets.QMessageBox()
        self.msg1.setIcon(QtWidgets.QMessageBox.Information)
        self.gio="3"
        self.msg1.setInformativeText(f"Mời bạn bỏ đồ của hộp. Vui lòng quay lại lấy đồ trước {self.gio} giờ")
        self.msg1.setWindowTitle("Thông báo")
        self.msg1.exec_()

    def messeage2(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Information)
        self.gio="3"
        self.msg.setInformativeText(f"Cảm ơn bạn đã tin dùng dịch vụ")
        self.msg.setWindowTitle("Thông báo")
        self.msg.exec_()





