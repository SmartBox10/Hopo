import pandas as pd

# Đọc file Excel
df = pd.read_excel('KHÁCH HÀNG HOPO.xlsx')


class Tu:  # Lop Tu
    def __init__(self, ma_tu, trang_thai):
        self.ma_tu = ma_tu
        self.trang_thai = trang_thai


class QuanLyTuDo:  # Lop Quan Li Tu Do
    def __init__(self, danh_sach_tu):
        self.danh_sach_tu = danh_sach_tu

    def hien_thi_so_tu_con_trong(self):
        so_tu_con_trong = sum(tu.trang_thai == "trong" for tu in self.danh_sach_tu)
        print(f"Số tủ còn trống: {so_tu_con_trong}")

    def hien_thi_tu_trong(self):
        print("Các mã tủ còn trống:")
        for tu in self.danh_sach_tu:
            if tu.trang_thai == "trong":
                print(tu.ma_tu)

    def hien_thi_tu_da_dat(self):
        print("Tủ bạn đang sử dụng là tủ nào:")
        for tu in self.danh_sach_tu:
            if tu.trang_thai == "Đã đặt":
                print(tu.ma_tu)

    def xoa_tu(self, ma_tu):
        for tu in self.danh_sach_tu:
            if tu.ma_tu == ma_tu:
                self.danh_sach_tu.remove(tu)
                break


class Khachhang(QuanLyTuDo):  # Lop Khach hang
    def __init__(self, ten_dang_nhap, mat_khau):
        super().__init__(danh_sach_tu)
        self.ten_dang_nhap = ten_dang_nhap
        self.mat_khau = mat_khau
        self.tu_da_chon = None
        self.start_time = None
        self.end_time = None
        self.thoi_gian_su_dung = None


    def login(self):  # Ham dang nhap
        # Kiểm tra tên đăng nhập
        if self.ten_dang_nhap in df['TÊN ĐĂNG NHẬP'].values:
            # Lọc các hàng có tên đăng nhập trùng với self.ten_dang_nhap
            df_filtered = df[df['TÊN ĐĂNG NHẬP'] == self.ten_dang_nhap]
            # Kiểm tra mật khẩu
            if len(df_filtered) > 0 and df_filtered['MẬT KHẨU'].values[0] == self.mat_khau:
                # Tên đăng nhập và mật khẩu đúng
                return 0
            else:
                # Mật khẩu không đúng
                return 1
        else:
            # Tên đăng nhập không tồn tại trong file Excel
            return 1


tu1 = Tu("A1", "trong")
tu2 = Tu("A2", "trong")
tu3 = Tu("A3", "trong")
tu4 = Tu("A4", "trong")
tu5 = Tu("A5", "trong")
danh_sach_tu = [tu1, tu2, tu3, tu4, tu5]
quan_ly_tu_do = QuanLyTuDo(danh_sach_tu)
quan_ly_tu_do.hien_thi_so_tu_con_trong()
quan_ly_tu_do.hien_thi_tu_trong()


