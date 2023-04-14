import pandas as pd

# Đọc file Excel
df = pd.read_excel('KHÁCH HÀNG HOPO.xlsx')


class Khachhang(ghgh):  # Lop Khach hang
    def __init__(self,):
        self.ten_dang_nhap = ten_dang_nhap
        self.mat_khau = self.mat_khau
        self.tu_da_chon = None
        self.start_time = None
        self.end_time = None
        self.thoi_gian_su_dung = None

    def login(self, ten_dang_nhap, mat_khau):  # Ham dang nhap
        if any((df['TÊN ĐĂNG NHẬP'] == self.ten_dang_nhap) & (df['MẬT KHẨU'] == self.mat_khau)):
            return 0
                # Tên đăng nhập và mật khẩu khớp với dữ liệu trong file Excel
        else:
            return 1


