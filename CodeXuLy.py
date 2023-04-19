
from datetime import datetime
class Khachhang:
    danh_sach_khach_hang_dang_su_dung = []
    danh_sach_khach_hang_chua_su_dung = []

    def __init__(self,ten_dang_nhap,mat_khau):
        self.ten_dang_nhap=ten_dang_nhap
        self.mat_khau=mat_khau
        self.trang_thai=None
        self.tu_da_chon = None
        self.start_time = None
        self.end_time = None
        self.thoi_gian_su_dung = 1
        self.mabosung= "123"
    def them_khach_hang(self):#khởi tạo danh sách khách hàng ban đầu
        Khachhang.danh_sach_khach_hang_chua_su_dung.append(self)

    @classmethod
    def hienthi_danh_sach_khach_hang_chua_su_dung(cls):
        for kh in cls.danh_sach_khach_hang_chua_su_dung:
            print(f'tên đăng nhập: {kh.ten_dang_nhap}, Mật khẩu: {kh.mat_khau}, Trang thái sử dụng: {kh.trang_thai}')
    @staticmethod
    def them_khach_hang_dang_su_dung():
        for i in Khachhang.danh_sach_khach_hang_chua_su_dung:
            if i.trang_thai=="Đang sử dụng":
                Khachhang.danh_sach_khach_hang_dang_su_dung.append(i)
                Khachhang.danh_sach_khach_hang_chua_su_dung.remove(i)
    @staticmethod
    def them_khach_hang_chua_su_dung():
        for i in Khachhang.danh_sach_khach_hang_dang_su_dung:
            if i.trang_thai==None:
                Khachhang.danh_sach_khach_hang_chua_su_dung.append(i)
                Khachhang.danh_sach_khach_hang_dang_su_dung.remove(i)


    def login(self):
        for i in Khachhang.danh_sach_khach_hang_chua_su_dung:
            if self.ten_dang_nhap == i.ten_dang_nhap and self.mat_khau== i.mat_khau:
                return 1
        return 0
    def kiem_tra_ma_bo_sung(self,mabosung):
        if self.mabosung==mabosung:
            return 1
        else:
            return 0 #ma bổ sung sai






class Tu:  # Lop Tu
    danh_sach_tu_chua_su_dung = []
    danh_sach_tu_dang_su_dung = []
    def __init__(self, ma_tu, trang_thai):
        self.ma_tu = ma_tu
        self.trang_thai = trang_thai
        self.ten_khach_hang=None
    def them_tu(self):#khởi tạo danh sách tu cho ban đầu
        Tu.danh_sach_tu_chua_su_dung.append(self)
def chon_tu(ma_tu,khachhang):
    if (khachhang.trang_thai=="trong"):
        for tu in Tu.danh_sach_tu_chua_su_dung:
            if tu.ma_tu==ma_tu:
                if tu.trang_thai=="trong":
                    khachhang.trang_thai="Đang sử dụng"
                    khachhang.tu_da_chon=ma_tu
                    tu.trang_thai="Đang sử dụng"
                    tu.ten_khach_hang=khachhang.ten_dang_nhap
                    khachhang.start_time = datetime.now().strftime("%H:%M:%S")
        return 1 #chọn tủ thành công
    else:
        return 0 #tu da được người khách sd hoac khach hang dang sử dụng tủ khác


def tra_tu(ma_tu,khachhang):
    #if (khachhang.trang_thai=="Đang sử dụng") and (tu.trang_thai=="Đang sử dụng"):
    if khachhang.tu_da_chon==ma_tu:
        #hàm tính giờ
        #khachhang.end_time = datetime.now().strftime("%H:%M:%S")
        #time_diff = khachhang.end_time - (khachhang.start_time)
        #khachhang.thoi_gian_su_dung = time_diff.seconds / 3600
        if khachhang.thoi_gian_su_dung < 2:
            khachhang.trang_thai = None
            khachhang.tu_da_chon = None
            for tu in Tu.danh_sach_tu_dang_su_dung:
                if tu.ma_tu==ma_tu:
                    tu.trang_thai = "trong"
                    tu.ten_khach_hang = None
                    #khachhang.thoi_gian_su_dung=1
                    khachhang.them_khach_hang_chua_su_dung()
                return 1
        else:
            #tính tiền và in  ra cho người ta biết
            manhap=input("nhập mã bổ sung")
            if khachhang.kiem_tra_ma_bo_sung(manhap) ==1:
                for tu in Tu.danh_sach_tu_dang_su_dung:
                    if tu.ma_tu == ma_tu:
                        tu.trang_thai = "trong"
                        tu.ten_khach_hang = None
                        # khachhang.thoi_gian_su_dung=1
                        khachhang.them_khach_hang_chua_su_dung()
                    return 2 #nhập mã bổ sung đúng
    else:
        return 0 # sai tên tu hoặc tên khach hang


kh1=Khachhang("Co","123")
kh2=Khachhang("Hien","345")
kh3=Khachhang("Linh","567")
kh1.them_khach_hang_chua_su_dung()
kh2.them_khach_hang_chua_su_dung()
kh3.them_khach_hang_chua_su_dung()
tu1=Tu("A1","trong")
tu2=Tu("A2","trong")
tu3=Tu("A3","trong")
tu1.them_tu()
tu2.them_tu()
tu3.them_tu()
print(kh1.hienthi_danh_sach_khach_hang_chua_su_dung())
