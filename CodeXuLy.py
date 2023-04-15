import pandas as pd

# Đọc file Excel
df = pd.read_excel('KHÁCH HÀNG HOPO.xlsx')


class Tu:  # Lop Tu
    def __init__(self, ma_tu, trang_thai):
        self.ma_tu = ma_tu
        self.trang_thai = trang_thai


class QuanLyTuDo:
    def __init__(self):
        self.danh_sach_tu_trong = []  # Danh sách tủ trống
        self.danh_sach_tu_da_dat = []  # Danh sách tủ đã đặt

    def them_tu_trong(self, tu):
        if tu.trang_thai == "trống":
            self.danh_sach_tu_trong.append(tu)  # Thêm tủ trống vào danh sách tủ trống

    def them_tu_da_dat(self, tu):
        if tu.trang_thai == "đã đặt":
            return
        self.danh_sach_tu_da_dat.append(tu)  # Thêm tủ đã đặt vào danh sách tủ đã đặt

    def xoa_tu_trong(self, ma_tu):
        for tu in self.danh_sach_tu_trong:
            if tu.ma_tu == ma_tu:
                self.danh_sach_tu_trong.remove(tu)
                break

    def xoa_tu_da_dat(self, ma_tu):
        for tu in self.danh_sach_tu_da_dat:
            if tu.ma_tu == ma_tu:
                self.danh_sach_tu_da_dat.remove(tu)
                break

    def hien_thi_tu_trong(self):
        print("Danh sách tủ trống:")
        for tu in self.danh_sach_tu_trong:
            print(tu.ma_tu)

    def hien_thi_tu_da_dat(self):
        print("Danh sách tủ đã đặt:")
        for tu in self.danh_sach_tu_da_dat:
            print(tu.ma_tu)

    def tinh_tong_so_tu_trong(self):
        return len(self.danh_sach_tu_trong)

    def tinh_tong_so_tu_da_dat(self):
        return len(self.danh_sach_tu_da_dat)


class Khachhang(QuanLyTuDo):  # Lop Khach hang
    def __init__(self, ten_dang_nhap, mat_khau):
        super().__init__()
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


# Giả sử đưa vào ban đầu tất cả các tủ đều trống
tu1 = Tu("A1", "trống")
tu2 = Tu("A2", "trống")
tu3 = Tu("A3", "trống")
tu4 = Tu("A4", "trống")
tu5 = Tu("A5", "trống")
# Tạo một đối tượng QuanLyTuDo
quan_ly_tu_do = QuanLyTuDo()
# Thêm các đối tượng Tu vào danh sách tủ trống
quan_ly_tu_do.them_tu_trong(tu1)
quan_ly_tu_do.them_tu_trong(tu2)
quan_ly_tu_do.them_tu_trong(tu3)
quan_ly_tu_do.them_tu_trong(tu4)
quan_ly_tu_do.them_tu_trong(tu5)
# Tính tổng số tủ trống
print(quan_ly_tu_do.tinh_tong_so_tu_trong())
