import pandas as pd
import datetime as date
from datetime import datetime

# Đọc file Excel
df = pd.read_excel('D:/LINH/KHÁCH HÀNG HOPO.xlsx')
# Tạo danh sách khách hàng từ các cột tương ứng với thuộc tính của khách hàng
dskh = [{'ten_dang_nhap': row['TÊN ĐĂNG NHẬP'], 'ma_dinh_danh': row['MÃ ĐỊNH DANH']} for _, row in df.iterrows()]


class Khachhang:
    KhachhangList = []
    danh_sach_khach_hang = dskh

    def __init__(self, ten_dang_nhap, mat_khau):
        self.ten_dang_nhap = ten_dang_nhap
        self.mat_khau = mat_khau
        self.trang_thai = "0"
        self.tu_da_chon = "0"
        self.start_time = "0"
        self.end_time = "0"
        self.thoi_gian_su_dung = 1
        self.ma_dinh_danh = "0"

    def them_khach_hang(self):  # Khởi tạo danh sách khách hàng ban đầu
        Khachhang.KhachhangList.append(self)
        return print("them khach hàng thành công")

    @classmethod
    def hien_thi_danh_sach_khach_hang_chua_su_dung(cls):
        for kh in cls.KhachhangList:
            if kh.trang_thai == "0":
                print(
                    f'tên đăng nhập: {kh.ten_dang_nhap}, Mật khẩu: {kh.mat_khau}, Trang thái sử dụng: {kh.trang_thai}')

    def login(self):
        for i in Khachhang.KhachhangList:
            if self.ten_dang_nhap == i.ten_dang_nhap and self.mat_khau == i.mat_khau:
                return 1
        return 0

    def tao_ma_dinh_danh(self):
        dateNow = str(date.datetime.now())
        self.ma_dinh_danh = dateNow.split(':')[0].replace(' ', '')[8:] + dateNow.split(':')[2][4:]
        return self.ma_dinh_danh

    def kiem_tra_ma_bo_sung(self, ma_dinh_danh):
        if self.ma_dinh_danh == ma_dinh_danh:
            return 1
        else:
            return 0  # ma bổ sung sai


class Tu:  # Lop Tu
    TuList = []

    def __init__(self, ma_tu, trang_thai):
        self.ma_tu = ma_tu
        self.trang_thai = trang_thai
        self.ten_khach_hang = "0"

    def them_tu(self):  # khởi tạo danh sách tu cho ban đầu
        Tu.TuList.append(self)
        return 1

    def ting_tong_tu_trong(self):
        sum = 0
        for tu in Tu.TuList:
            if tu.trang_thai == "0":
                sum += 1
        return sum


def chon_tu(ma_tu, khachhang):
    if khachhang.trang_thai == "0":
        for tu in Tu.TuList:
            if tu.ma_tu == ma_tu:
                if tu.trang_thai == "0":
                    khachhang.trang_thai = "1"
                    khachhang.tu_da_chon = ma_tu
                    khachhang.start_time = datetime.now().strftime("%H:%M:%S")
                    khachhang.ma_dinh_danh = khachhang.tao_ma_dinh_danh()
                    for i in Khachhang.danh_sach_khach_hang:
                        if khachhang.ten_dang_nhap == i['ten_dang_nhap']:
                            i['ma_dinh_danh'] = khachhang.ma_dinh_danh
                    tu.trang_thai = "1"
                    tu.ten_khach_hang = khachhang.ten_dang_nhap
                else:
                    return 0
        return 1  # 1 #chọn tủ thành công
    else:
        return 0  # print("Tủ đã có người sử dụng")#0 #tu da được người khách sd hoac khach hang dang sử dụng tủ khác


def tra_tu(khachhang):
    for tu in Tu.TuList:
        if tu.ten_khach_hang == khachhang.ten_dang_nhap:
            if khachhang.thoi_gian_su_dung < 2:
                khachhang.trang_thai = "0"
                khachhang.tu_da_chon = "0"
                khachhang.ma_dinh_danh = "0"
                for i in Khachhang.danh_sach_khach_hang:
                    if khachhang.ten_dang_nhap == i['ten_dang_nhap']:
                        i['ma_dinh_danh'] = 0
                khachhang.end_time = datetime.now().strftime("%H:%M:%S")
                start_time = datetime.strptime(khachhang.start_time, "%H:%M:%S")
                end_time = datetime.strptime(khachhang.end_time, "%H:%M:%S")
                time_diff = end_time - start_time
                khachhang.thoi_gian_su_dung = time_diff.seconds / 3600
                print(khachhang.thoi_gian_su_dung)
                tu.trang_thai = "0"
                tu.ten_khach_hang = "0"
                return 1  # print("trả tủ đúng thời gian quy định")
            else:
                manhap = input("nhập mã định danh: ")
                if khachhang.kiem_tra_ma_bo_sung(manhap) == 1:
                    khachhang.trang_thai = "0"
                    khachhang.tu_da_chon = "0"
                    tu.trang_thai = "0"
                    tu.ten_khach_hang = "0"
                    return 2  # print("nhập mã bổ sung đúng, trả tủ thành công")
                else:
                    return 4  # nhập sai mã định danh
        else:
            return 0  # print("khách hàng chưa có đặt tủ")#0


kh1 = Khachhang("K224111388", "123")
kh2 = Khachhang("K224111399", "456")
kh3 = Khachhang("K224111381", "789")
kh1.them_khach_hang()
kh2.them_khach_hang()
kh3.them_khach_hang()
tu1 = Tu("A1", "0")
tu2 = Tu("A2", "0")
tu3 = Tu("A3", "0")
tu1.them_tu()
tu2.them_tu()
tu3.them_tu()
print(kh1.login())
print(chon_tu(tu1.ma_tu, kh1))
print(Khachhang.danh_sach_khach_hang)
print(Khachhang.danh_sach_khach_hang)
