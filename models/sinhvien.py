import json


class SinhVien:
    def __init__(
        self,
        mssv,
        ho_ten,
        ngay_sinh,
        gioi_tinh,
        khoa,
        khoa_hoc,
        chuong_trinh,
        dia_chi,
        email,
        sdt,
        tinh_trang,
    ):
        self.mssv = mssv
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.gioi_tinh = gioi_tinh
        self.khoa = khoa
        self.khoa_hoc = khoa_hoc
        self.chuong_trinh = chuong_trinh
        self.dia_chi = dia_chi
        self.email = email
        self.sdt = sdt
        self.tinh_trang = tinh_trang

    def __str__(self):
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)

    def to_dict(self):
        return {
            "mssv": self.mssv,
            "ho_ten": self.ho_ten,
            "ngay_sinh": self.ngay_sinh,
            "gioi_tinh": self.gioi_tinh,
            "khoa": self.khoa,
            "khoa_hoc": self.khoa_hoc,
            "chuong_trinh": self.chuong_trinh,
            "dia_chi": self.dia_chi,
            "email": self.email,
            "sdt": self.sdt,
            "tinh_trang": self.tinh_trang,
        }
