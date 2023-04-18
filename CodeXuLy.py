import pandas as pd
from datetime import datetime

# Đọc file Excel
df = pd.read_excel('KHÁCH HÀNG HOPO.xlsx')

# Tạo danh sách khách hàng từ các cột tương ứng với thuộc tính của khách hàng
danh_sach_khach_hang = [
    {'ten_dang_nhap': row['TÊN ĐĂNG NHẬP'], 'mat_khau': row['MẬT KHẨU'], 'trang_thai': row['TRẠNG THÁI'],
     'ma_tu': row['MÃ TỦ']} for _, row in df.iterrows()]

# Lọc ra danh sách khách hàng có trạng thái chưa sử dụng
danh_sach_khach_hang_chua_su_dung = [khach_hang for khach_hang in danh_sach_khach_hang if
                                     khach_hang['trang_thai'] == 'Chưa sử dụng']

# Lọc ra danh sách khách hàng có trạng thái chưa sử dụng
danh_sach_khach_hang_dang_su_dung = [khach_hang for khach_hang in danh_sach_khach_hang if
                                     khach_hang['trang_thai'] == 'Đang sử dụng']


class Tu:  # Lop Tu
    def __init__(self, ma_tu, trang_thai):
        self.ma_tu = ma_tu
        self.trang_thai = trang_thai


class QuanLyTuDo:
    danh_sach_tu_trong = []
    danh_sach_tu_da_dat = []

    def __init__(self, danh_sach_tu_trong, danh_sach_tu_da_dat):
        self.danh_sach_tu_trong = danh_sach_tu_trong  # Danh sách tủ trống
        self.danh_sach_tu_da_dat = danh_sach_tu_da_dat  # Danh sách tủ đã đặt

    def cap_nhat_trang_thai_tu(self, ma_tu):
        for tu in self.danh_sach_tu_trong:
            if tu.ma_tu == ma_tu:
                tu.trang_thai = "đã đặt"
                self.danh_sach_tu_trong.remove(tu)
                self.danh_sach_tu_da_dat.append(tu)
                break

        for tu in self.danh_sach_tu_da_dat:
            if tu.ma_tu == ma_tu:
                tu.trang_thai = "trống"
                self.danh_sach_tu_da_dat.remove(tu)
                self.danh_sach_tu_trong.append(tu)
                break

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


class QuanLyKhachHang:
    def __init__(self, danh_sach_khach_hang_dang_su_dung, danh_sach_khach_hang_chua_su_dung):
        self.danh_sach_khach_hang_dang_su_dung = danh_sach_khach_hang_dang_su_dung
        self.danh_sach_khach_hang_chua_su_dung = danh_sach_khach_hang_chua_su_dung

    def them_khach_hang_vao_ds_dang_su_dung(self, khachhang):
        if khachhang.trang_thai == "Đang sử dụng":
            self.danh_sach_khach_hang_dang_su_dung(khachhang)

    def them_khach_hang_vao_ds_chua_su_dung(self, khachhang):
        if khachhang.trang_thai == "Chưa sử dụng":
            self.danh_sach_khach_hang_chua_su_dung(khachhang)

    def xoa_khach_hang_khoi_ds_dang_su_dung(self, ten_dang_nhap):
        for khachhang in self.danh_sach_khach_hang_dang_su_dung:
            if khachhang.ten_dang_nhap == ten_dang_nhap:
                self.danh_sach_khach_hang_dang_su_dung.remove(khachhang)

    def xoa_khach_hang_khoi_ds_chua_su_dung(self, ten_dang_nhap):
        for khachhang in self.danh_sach_khach_hang_chua_su_dung:
            if khachhang.ten_dang_nhap == ten_dang_nhap:
                self.danh_sach_khach_hang_chua_su_dung.remove(khachhang)

    def cap_nhat_trang_thai_khach_hang(self, ten_dang_nhap):
        for khachhang in self.danh_sach_khach_hang_chua_su_dung:
            if khachhang.ten_dang_nhap == ten_dang_nhap:
                khachhang.trang_thai = "Đang sử dụng"
                self.danh_sach_khach_hang_chua_su_dung.remove(khachhang)
                self.danh_sach_khach_hang_dang_su_dung.append(khachhang)
                break

        for khachhang in self.danh_sach_khach_hang_dang_su_dung:
            if khachhang.ten_dang_nhap == ten_dang_nhap:
                khachhang.trang_thai = "Chưa sử dụng"
                self.danh_sach_khach_hang_dang_su_dung.remove(khachhang)
                self.danh_sach_khach_hang_chua_su_dung.append(khachhang)
                break


class Khachhang(QuanLyKhachHang, QuanLyTuDo):
    # Lớp Khachhang chỉ có 4 thuộc tính riêng của nó
    def __init__(self, ten_dang_nhap, mat_khau):
        super().__init__(danh_sach_khach_hang_dang_su_dung, danh_sach_khach_hang_chua_su_dung)
        self.ten_dang_nhap = ten_dang_nhap
        self.mat_khau = mat_khau
        self.trang_thai = None
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
                for khach_hang in danh_sach_khach_hang:
                    if khach_hang['ten_dang_nhap'] == self.ten_dang_nhap:
                        self.trang_thai = khach_hang['trang_thai']
                return 1
            else:
                # Mật khẩu không đúng
                return 0
        else:
            # Tên đăng nhập không tồn tại trong file Excel
            return 0

    def Chon_tu(self):  # Hàm đặt tủ
        if self.ten_dang_nhap in self.danh_sach_khach_hang_dang_su_dung:
            print("Bạn đang sử dụng dịch vụ Hopo, bạn không được chọn thêm 1 tủ nữa.")
        else:
            while True:
                ma_tu_chon = input("Nhập mã tủ muốn chọn (hoặc 'q' để thoát)")
                if ma_tu_chon == 'q':
                    break
                tu_da_chon = None
                for tu in self.danh_sach_tu_trong:
                    if tu.ma_tu == ma_tu_chon:
                        tu_da_chon = tu
                        break
                if tu_da_chon is None:
                    print("Mã tủ không hợp lệ hoặc tủ đã được chọn. Vui lòng nhập lại.")
                    continue
                else:
                    # Đối với tủ đã được khách hàng nhập mã lựa chọn
                    self.cap_nhat_trang_thai_tu(tu_da_chon)
                    # Đối với khách hàng
                    self.tu_da_chon = tu_da_chon
                    self.start_time = datetime.now().strftime("%H:%M:%S")
                    self.cap_nhat_trang_thai_khach_hang()
                    # Cập nhật trạng thái của khách hàng trong file Excel
                    index = df.index[df['TÊN ĐĂNG NHẬP'] == self.ten_dang_nhap].tolist()[0]
                    df.at[index, 'TRẠNG THÁI'] = "Đang sử dụng"
                    df.at[index, 'MÃ TỦ'] = tu_da_chon.ma_tu
                    # Ghi lại danh sách khách hàng vào file Excel sau khi cập nhật
                    df.to_excel('KHÁCH HÀNG HOPO.xlsx', index=False)
                    print("Bạn đã chọn tủ thành công.")
                    break
                print("Tủ đã được sử dụng hoặc không tồn tại.")

    def Tra_tu(self):
        if self.ten_dang_nhap in self.danh_sach_khach_hang_chua_su_dung:
            print("Bạn chưa sử dụng tủ Hopo.")
        else:
            while True:
                ma_tu_tra = input("Nhập mã tủ muốn tra (hoặc 'q' để thoát)")
                if ma_tu_tra == 'q':
                    break
                tu_tra = None
                for tu in self.danh_sach_tu_da_dat:
                    if tu.ma_tu == ma_tu_tra:
                        tu_tra = tu
                        break
                if tu_tra is None:
                    print("Mã tủ không hợp lệ hoặc tủ trống. Vui lòng nhập lại.")
                    continue
                else:
                    # Đối với tủ đã được khách hàng nhập mã lựa chọn
                    self.cap_nhat_trang_thai_tu(tu_tra)
                    # Đối với khách hàng
                    self.tu_da_chon = None
                    self.end_time = datetime.now().strftime("%H:%M:%S")
                    start_time = datetime.strptime(self.start_time, "%H:%M:%S")
                    end_time = datetime.strptime(self.end_time, "%H:%M:%S")
                    time_diff = end_time - start_time
                    self.thoi_gian_su_dung = time_diff.seconds / 3600
                    self.cap_nhat_trang_thai_khach_hang()
                    # Cập nhật trạng thái của khách hàng trong file Excel
                    index = df.index[df['TÊN ĐĂNG NHẬP'] == self.ten_dang_nhap].tolist()[0]
                    df.at[index, 'TRẠNG THÁI'] = "Chưa sử dụng"
                    df.at[index, 'MÃ TỦ'] = None
                    # Ghi lại danh sách khách hàng vào file Excel sau khi cập nhật
                    df.to_excel('KHÁCH HÀNG HOPO.xlsx', index=False)
                    print("Bạn đã trả tủ thành công.")
                    break
                print("Tủ đang trống, không giữ đồ hoặc không tồn tại.")


def main():
    # Khởi tạo các đối tượng
    # Tạo một đối tượng QuanLyTuDo
    quan_ly_tu_do = QuanLyTuDo([], [])
    # Giả sử đưa vào ban đầu tất cả các tủ đều trống
    tu1 = Tu("A1", "trống")
    tu2 = Tu("A2", "trống")
    tu3 = Tu("A3", "trống")
    tu4 = Tu("A4", "trống")
    tu5 = Tu("A5", "trống")
    # Thêm các đối tượng Tu vào danh sách tủ trống
    quan_ly_tu_do.them_tu_trong(tu1)
    quan_ly_tu_do.them_tu_trong(tu2)
    quan_ly_tu_do.them_tu_trong(tu3)
    quan_ly_tu_do.them_tu_trong(tu4)
    quan_ly_tu_do.them_tu_trong(tu5)
    QuanLyKhachHang(danh_sach_khach_hang_dang_su_dung, danh_sach_khach_hang_chua_su_dung)
    # Tạo đối tượng khách hàng
    khach_hang = Khachhang("", "")
    while True:
        print("Vui lòng đăng nhập")
        khach_hang.ten_dang_nhap = input("Nhập tên đăng nhập: ")
        khach_hang.mat_khau = input("Nhật mật khẩu: ")
        if khach_hang.login() == 1:
            while True:
                print("----- MENU -----")
                print("1. Chọn tủ")
                print("2. Trả tủ")
                print("3. Thoát")
                choice = input("Nhập lựa chọn của bạn (1/2/3): ")
                if choice == "1":
                    quan_ly_tu_do.hien_thi_tu_trong()
                    khach_hang.Chon_tu()
                elif choice == "2":
                    quan_ly_tu_do.hien_thi_tu_da_dat()
                    khach_hang.Tra_tu()
                elif choice == "3":
                    print("Đã thoát chương trình.")
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
        else:
            print("Tên đăng nhập hoặc mật khẩu không đúng, vui lòng nhập lại.")


if __name__ == '__main__':
    main()
