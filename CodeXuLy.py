
from datetime import datetime
class Tu:  # Lop Tu
    def __init__(self, ma_tu, trang_thai):
        self.ma_tu = ma_tu
        self.trang_thai = trang_thai

class Khachhang:
    def __init__(self,ten_dang_nhap,mat_khau):
        self.ten_dang_nhap=ten_dang_nhap
        self.mat_khau=mat_khau
        self.trang_thai=None
        self.tu_da_chon = None
        self.start_time = None
        self.end_time = None
        self.thoi_gian_su_dung = None

class QuanLyTuDo:
    danh_sach_tu_trong = []
    danh_sach_tu_da_dat = []

    #def __init__(self, danh_sach_tu_trong, danh_sach_tu_da_dat):
        #self.danh_sach_tu_trong = danh_sach_tu_trong  # Danh sách tủ trống
        #self.danh_sach_tu_da_dat = danh_sach_tu_da_dat  # Danh sách tủ đã đặt


    @classmethod
    def cap_nhat_trang_thai_tu(cls, ma_tu):
        for tu in QuanLyTuDo.danh_sach_tu_trong:
            if tu.ma_tu == ma_tu:
                tu.trang_thai = "đã đặt"
                QuanLyTuDo.danh_sach_tu_trong.remove(tu)
                QuanLyTuDo.danh_sach_tu_da_dat.append(tu)
                break

        for tu in QuanLyTuDo.danh_sach_tu_da_dat:
            if tu.ma_tu == ma_tu:
                tu.trang_thai = "trống"
                QuanLyTuDo.danh_sach_tu_da_dat.remove(tu)
                QuanLyTuDo.danh_sach_tu_trong.append(tu)
                break


    @classmethod
    def them_tu_trong(cls, tu):
        if tu.trang_thai == "trống":
            QuanLyTuDo.danh_sach_tu_trong.append(tu)  # Thêm tủ trống vào danh sách tủ trống

    @classmethod
    def them_tu_da_dat(cls, tu):
        if tu.trang_thai == "đã đặt":
            return
        QuanLyTuDo.danh_sach_tu_da_dat.append(tu)  # Thêm tủ đã đặt vào danh sách tủ đã đặt

    @classmethod
    def xoa_tu_trong(cls, ma_tu):
        for tu in QuanLyTuDo.danh_sach_tu_trong:
            if tu.ma_tu == ma_tu:
                QuanLyTuDo.danh_sach_tu_trong.remove(tu)
                break


    @classmethod
    def xoa_tu_da_dat(cls, ma_tu):
        for tu in QuanLyTuDo.danh_sach_tu_da_dat:
            if tu.ma_tu == ma_tu:
                QuanLyTuDo.danh_sach_tu_da_dat.remove(tu)
                break

    @classmethod
    def hien_thi_tu_trong(cls):
        print("Danh sách tủ trống:")
        for tu in QuanLyTuDo.danh_sach_tu_trong:
            print(tu.ma_tu)

    @classmethod
    def hien_thi_tu_da_dat(cls):
        print("Danh sách tủ đã đặt:")
        for tu in QuanLyTuDo.danh_sach_tu_da_dat:
            print(tu.ma_tu)

    @classmethod
    def tinh_tong_so_tu_trong(cls):
        return len(QuanLyTuDo.danh_sach_tu_trong)

    @classmethod
    def tinh_tong_so_tu_da_dat(cls):
        return len(QuanLyTuDo.danh_sach_tu_da_dat)


class QuanLyKhachHang:
    danh_sach_khach_hang=[]
    danh_sach_khach_hang_dang_su_dung=[]
    danh_sach_khach_hang_chua_su_dung=[]

    @classmethod
    def them_khach_hang_vao_ds_dang_su_dung(cls, khachhang):
        if khachhang.trang_thai == "Đang sử dụng":
            cls.danh_sach_khach_hang_dang_su_dung.append(khachhang)


    @classmethod
    def them_khach_hang_vao_ds_chua_su_dung(cls, khachhang):
        if khachhang.trang_thai == "Chưa sử dụng":
            cls.danh_sach_khach_hang_chua_su_dung.append(khachhang)

    @classmethod
    def xoa_khach_hang_khoi_ds_dang_su_dung(cls, khachhang):
        for i in cls.danh_sach_khach_hang_dang_su_dung:
            if i.ten_dang_nhap == khachhang.ten_dang_nhap:
                cls.danh_sach_khach_hang_dang_su_dung.remove(khachhang)

    @classmethod
    def xoa_khach_hang_khoi_ds_chua_su_dung(cls, khachhang):
        for i in cls.danh_sach_khach_hang_chua_su_dung:
            if khachhang.ten_dang_nhap == i.ten_dang_nhap:
                cls.danh_sach_khach_hang_chua_su_dung.remove(khachhang)

    @classmethod
    def cap_nhat_trang_thai_khach_hang(cls, khachhang):
        for i in cls.danh_sach_khach_hang_chua_su_dung:
            if i.ten_dang_nhap == khachhang.ten_dang_nhap:
                khachhang.trang_thai = "Đang sử dụng"
                cls.danh_sach_khach_hang_chua_su_dung.remove(khachhang)
                cls.danh_sach_khach_hang_dang_su_dung.append(khachhang)
                break

        for i in cls.danh_sach_khach_hang_dang_su_dung:
            if i.ten_dang_nhap == khachhang.ten_dang_nhap:
                khachhang.trang_thai = "Chưa sử dụng"
                cls.danh_sach_khach_hang_dang_su_dung.remove(khachhang)
                cls.danh_sach_khach_hang_chua_su_dung.append(khachhang)
                break


class Quanlichung():
    @classmethod
    def login(cls,khachhang):  # Ham dang nhap
        for i in QuanLyKhachHang.danh_sach_khach_hang:
            if i.ten_dang_nhap== khachhang.ten_dang_nhap and i.mat_khau==khachhang.mat_khau:
                return 1
        return 0


    @classmethod
    def Chon_tu(cls,khachhang):  # Hàm đặt tủ
        if khachhang.ten_dang_nhap in QuanLyKhachHang.danh_sach_khach_hang_dang_su_dung:
            print("Bạn đang sử dụng dịch vụ Hopo, bạn không được chọn thêm 1 tủ nữa.")
        else:
            while True:
                ma_tu_chon = input("Nhập mã tủ muốn chọn (hoặc 'q' để thoát)")
                if ma_tu_chon == 'q':
                    break
                #tu_da_chon = None
                for tu in QuanLyTuDo.danh_sach_tu_trong:
                    if tu.ma_tu == ma_tu_chon:
                        tu_da_chon = tu
                        break
                if tu_da_chon is None:
                    print("Mã tủ không hợp lệ hoặc tủ đã được chọn. Vui lòng nhập lại.")
                    continue
                else:
                    # Đối với tủ đã được khách hàng nhập mã lựa chọn
                    QuanLyTuDo.cap_nhat_trang_thai_tu(ma_tu_chon)
                    # Đối với khách hàng
                    khachhang.tu_da_chon = ma_tu_chon
                    khachhang.start_time = datetime.now().strftime("%H:%M:%S")
                    QuanLyKhachHang.cap_nhat_trang_thai_khach_hang(khachhang)
                    QuanLyKhachHang.them_khach_hang_vao_ds_dang_su_dung(khachhang)
                    print(khachhang.__dict__)
                    print(QuanLyKhachHang.danh_sach_khach_hang_dang_su_dung)
                    break
                print("Tủ đã được sử dụng hoặc không tồn tại.")

    @classmethod
    def Tra_tu(cls,khachhang):
        if khachhang.ten_dang_nhap in QuanLyKhachHang.danh_sach_khach_hang_chua_su_dung:
            print("Bạn chưa sử dụng tủ Hopo.")
        else:
            while True:
                ma_tu_tra = input("Nhập mã tủ muốn tra (hoặc 'q' để thoát)")
                if ma_tu_tra == 'q':
                    break
                tu_tra = None
                for tu in QuanLyTuDo.danh_sach_tu_da_dat:
                    if tu.ma_tu == ma_tu_tra:
                        tu_tra = tu
                        break
                if tu_tra is None:
                    print("Mã tủ không hợp lệ hoặc tủ trống. Vui lòng nhập lại.")
                    continue
                else:
                    # Đối với tủ đã được khách hàng nhập mã lựa chọn
                    QuanLyTuDo.cap_nhat_trang_thai_tu(tu_tra)
                    # Đối với khách hàng
                    khachhang.tu_da_chon = None
                    khachhang.end_time = datetime.now().strftime("%H:%M:%S")
                    start_time = datetime.strptime(khachhang.start_time, "%H:%M:%S")
                    end_time = datetime.strptime(khachhang.end_time, "%H:%M:%S")
                    time_diff = end_time - start_time
                    khachhang.thoi_gian_su_dung = time_diff.seconds / 3600
                    khachhang.cap_nhat_trang_thai_khach_hang()
                    print("Bạn đã trả tủ thành công.")
                    break
                #print("Tủ đang trống, không giữ đồ hoặc không tồn tại.")



    # Khởi tạo các đối tượng
    # Tạo một đối tượng QuanLyTuDo
quan_ly_tu_do = QuanLyTuDo()
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
quan_ly_tu_do.them_tu_da_dat(tu5)
    # Tạo đối tượng khách hàng
khach_hang1 = Khachhang("Co", "123")
khach_hang2 = Khachhang("Hien", "345")
khach_hang3= Khachhang('Linh',"456")
QuanLyKhachHang.danh_sach_khach_hang.append(khach_hang1)
QuanLyKhachHang.danh_sach_khach_hang.append(khach_hang2)
QuanLyKhachHang.danh_sach_khach_hang.append(khach_hang3)

Quanlichung.Chon_tu(khach_hang1)
Quanlichung.Tra_tu(khach_hang1)

