import re
import datetime

class SinhVien:
    def __init__(self, mssv, ho_ten, ngay_sinh, gioi_tinh, khoa, khoa_hoc, chuong_trinh, dia_chi, email, sdt, tinh_trang):
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
        return f"MSSV: {self.mssv}, Họ tên: {self.ho_ten}, Ngày sinh: {self.ngay_sinh}, Giới tính: {self.gioi_tinh}, Khoa: {self.khoa}, Khóa: {self.khoa_hoc}, Chương trình: {self.chuong_trinh}, Địa chỉ: {self.dia_chi}, Email: {self.email}, SĐT: {self.sdt}, Tình trạng: {self.tinh_trang}"


def kiem_tra_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def kiem_tra_sdt(sdt):
    pattern = r"^(0|\+84)(\d{9})$"  
    return re.match(pattern, sdt) is not None

def kiem_tra_ngay_sinh(ngay_sinh):
    try:
        datetime.datetime.strptime(ngay_sinh, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def them_sinh_vien(danh_sach_sinh_vien):
    print("\nThêm sinh viên mới:")
    mssv = input("Nhập MSSV: ")
    while any(sv.mssv == mssv for sv in danh_sach_sinh_vien):
        print("MSSV đã tồn tại. Vui lòng nhập lại.")
        mssv = input("Nhập MSSV: ")

    ho_ten = input("Nhập họ tên: ")
    
    ngay_sinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
    while not kiem_tra_ngay_sinh(ngay_sinh):
      print("Ngày sinh không hợp lệ. Vui lòng nhập lại theo định dạng dd/mm/yyyy.")
      ngay_sinh = input("Nhập ngày sinh (dd/mm/yyyy): ")

    gioi_tinh = input("Nhập giới tính (Nam/Nữ/Khác): ")

    print("Danh sách khoa: Khoa Luật, Khoa Tiếng Anh thương mại, Khoa Tiếng Nhật, Khoa Tiếng Pháp")
    khoa = input("Nhập khoa: ")
    while khoa not in ["Khoa Luật", "Khoa Tiếng Anh thương mại", "Khoa Tiếng Nhật", "Khoa Tiếng Pháp"]:
        print("Khoa không hợp lệ. Vui lòng chọn một trong các khoa đã liệt kê.")
        khoa = input("Nhập khoa: ")

    khoa_hoc = input("Nhập khóa: ")
    chuong_trinh = input("Nhập chương trình: ")
    dia_chi = input("Nhập địa chỉ: ")

    email = input("Nhập email: ")
    while not kiem_tra_email(email):
        print("Email không hợp lệ. Vui lòng nhập lại.")
        email = input("Nhập email: ")

    sdt = input("Nhập số điện thoại: ")
    while not kiem_tra_sdt(sdt):
        print("Số điện thoại không hợp lệ. Vui lòng nhập lại.")
        sdt = input("Nhập số điện thoại: ")

    print("Tình trạng sinh viên: Đang học, Đã tốt nghiệp, Đã thôi học, Tạm dừng học")
    tinh_trang = input("Nhập tình trạng: ")
    while tinh_trang not in ["Đang học", "Đã tốt nghiệp", "Đã thôi học", "Tạm dừng học"]:
        print("Tình trạng không hợp lệ. Vui lòng chọn một trong các tình trạng đã liệt kê.")
        tinh_trang = input("Nhập tình trạng: ")

    sinh_vien_moi = SinhVien(mssv, ho_ten, ngay_sinh, gioi_tinh, khoa, khoa_hoc, chuong_trinh, dia_chi, email, sdt, tinh_trang)
    danh_sach_sinh_vien.append(sinh_vien_moi)
    print("Thêm sinh viên thành công!")


def xoa_sinh_vien(danh_sach_sinh_vien):
    mssv_can_xoa = input("Nhập MSSV của sinh viên cần xóa: ")
    for i, sv in enumerate(danh_sach_sinh_vien):
        if sv.mssv == mssv_can_xoa:
            del danh_sach_sinh_vien[i]
            print("Đã xóa sinh viên có MSSV", mssv_can_xoa)
            return
    print("Không tìm thấy sinh viên có MSSV", mssv_can_xoa)


def cap_nhat_sinh_vien(danh_sach_sinh_vien):
    mssv_can_cap_nhat = input("Nhập MSSV của sinh viên cần cập nhật: ")
    for sv in danh_sach_sinh_vien:
        if sv.mssv == mssv_can_cap_nhat:
            print("Nhập thông tin mới (để trống nếu không muốn thay đổi):")
            ho_ten = input(f"Họ tên ({sv.ho_ten}): ") or sv.ho_ten
            
            ngay_sinh = input(f"Ngày sinh ({sv.ngay_sinh}) (dd/mm/yyyy): ") or sv.ngay_sinh
            while not kiem_tra_ngay_sinh(ngay_sinh):
              print("Ngày sinh không hợp lệ. Vui lòng nhập lại theo định dạng dd/mm/yyyy.")
              ngay_sinh = input(f"Ngày sinh ({sv.ngay_sinh}) (dd/mm/yyyy): ") or sv.ngay_sinh

            gioi_tinh = input(f"Giới tính ({sv.gioi_tinh}): ") or sv.gioi_tinh

            print("Danh sách khoa: Khoa Luật, Khoa Tiếng Anh thương mại, Khoa Tiếng Nhật, Khoa Tiếng Pháp")
            khoa = input(f"Khoa ({sv.khoa}): ") or sv.khoa
            while khoa not in ["Khoa Luật", "Khoa Tiếng Anh thương mại", "Khoa Tiếng Nhật", "Khoa Tiếng Pháp"] and khoa != "":
                print("Khoa không hợp lệ. Vui lòng chọn một trong các khoa đã liệt kê.")
                khoa = input(f"Khoa ({sv.khoa}): ") or sv.khoa

            khoa_hoc = input(f"Khóa ({sv.khoa_hoc}): ") or sv.khoa_hoc
            chuong_trinh = input(f"Chương trình ({sv.chuong_trinh}): ") or sv.chuong_trinh
            dia_chi = input(f"Địa chỉ ({sv.dia_chi}): ") or sv.dia_chi

            email = input(f"Email ({sv.email}): ") or sv.email
            while not kiem_tra_email(email) and email != "":
                print("Email không hợp lệ. Vui lòng nhập lại.")
                email = input(f"Email ({sv.email}): ") or sv.email

            sdt = input(f"Số điện thoại ({sv.sdt}): ") or sv.sdt
            while not kiem_tra_sdt(sdt) and sdt != "":
                print("Số điện thoại không hợp lệ. Vui lòng nhập lại.")
                sdt = input(f"Số điện thoại ({sv.sdt}): ") or sv.sdt
            
            print("Tình trạng sinh viên: Đang học, Đã tốt nghiệp, Đã thôi học, Tạm dừng học")
            tinh_trang = input(f"Tình trạng ({sv.tinh_trang}): ") or sv.tinh_trang
            while tinh_trang not in ["Đang học", "Đã tốt nghiệp", "Đã thôi học", "Tạm dừng học"] and tinh_trang != "":
                print("Tình trạng không hợp lệ. Vui lòng chọn một trong các tình trạng đã liệt kê.")
                tinh_trang = input(f"Tình trạng ({sv.tinh_trang}): ") or sv.tinh_trang

            sv.ho_ten = ho_ten
            sv.ngay_sinh = ngay_sinh
            sv.gioi_tinh = gioi_tinh
            sv.khoa = khoa
            sv.khoa_hoc = khoa_hoc
            sv.chuong_trinh = chuong_trinh
            sv.dia_chi = dia_chi
            sv.email = email
            sv.sdt = sdt
            sv.tinh_trang = tinh_trang
            
            print("Cập nhật thông tin thành công!")
            return

    print("Không tìm thấy sinh viên có MSSV", mssv_can_cap_nhat)


def tim_kiem_sinh_vien(danh_sach_sinh_vien):
    lua_chon = input("Tìm kiếm theo (1: Họ tên, 2: MSSV): ")
    if lua_chon == '1':
        ten_can_tim = input("Nhập họ tên cần tìm: ")
        ket_qua = [sv for sv in danh_sach_sinh_vien if ten_can_tim.lower() in sv.ho_ten.lower()]
    elif lua_chon == '2':
        mssv_can_tim = input("Nhập MSSV cần tìm: ")
        ket_qua = [sv for sv in danh_sach_sinh_vien if sv.mssv == mssv_can_tim]
    else:
        print("Lựa chọn không hợp lệ.")
        return

    if ket_qua:
        print("\nKết quả tìm kiếm:")
        for sv in ket_qua:
            print(sv)
    else:
        print("Không tìm thấy sinh viên nào.")
    

def hien_thi_danh_sach(danh_sach_sinh_vien):
    print("\nDanh sách sinh viên:")
    if not danh_sach_sinh_vien:
      print("Danh sách trống.")
      return
    for sv in danh_sach_sinh_vien:
        print(sv)

def main():
    danh_sach_sinh_vien = []

    while True:
        print("\n----- QUẢN LÝ SINH VIÊN -----")
        print("1. Thêm sinh viên")
        print("2. Xóa sinh viên")
        print("3. Cập nhật thông tin sinh viên")
        print("4. Tìm kiếm sinh viên")
        print("5. Hiển thị danh sách sinh viên")
        print("0. Thoát")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            them_sinh_vien(danh_sach_sinh_vien)
        elif lua_chon == '2':
            xoa_sinh_vien(danh_sach_sinh_vien)
        elif lua_chon == '3':
            cap_nhat_sinh_vien(danh_sach_sinh_vien)
        elif lua_chon == '4':
            tim_kiem_sinh_vien(danh_sach_sinh_vien)
        elif lua_chon == '5':
            hien_thi_danh_sach(danh_sach_sinh_vien)
        elif lua_chon == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()