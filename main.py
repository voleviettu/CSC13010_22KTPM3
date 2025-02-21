from services.sinhvien_service import SinhVienService
from services.khoa_service import KhoaService
from services.chuongtrinh_service import ChuongTrinhService
from services.tinhtrang_service import TinhTrangService
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler("app.log", encoding="utf-8")
])

def show_version():
    try:
        with open("version.txt", "r") as file:
            version_info = file.read()
            print("\n----- THÔNG TIN PHIÊN BẢN -----")
            print(version_info)
    except FileNotFoundError:
        print("Không tìm thấy file version.txt.")

def menu_import_export(service):
    while True:
        print("\n----- IMPORT/EXPORT SINH VIÊN -----")
        print("1. Import từ file CSV")
        print("2. Import từ file JSON")
        print("3. Export ra file CSV")
        print("4. Export ra file JSON")
        print("0. Quay lại")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            service.import_data("csv")
        elif lua_chon == '2':
            service.import_data("json")
        elif lua_chon == '3':
            service.export_data("csv")
        elif lua_chon == '4':
            service.export_data("json")
        elif lua_chon == '0':
            break
        else:
            logging.warning("Lựa chọn không hợp lệ. Vui lòng thử lại.")
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

def menu_sinh_vien(service):
    while True:
        print("\n----- QUẢN LÝ SINH VIÊN -----")
        print("1. Thêm sinh viên")
        print("2. Xóa sinh viên")
        print("3. Cập nhật thông tin sinh viên")
        print("4. Tìm kiếm sinh viên")
        print("5. Hiển thị danh sách sinh viên")
        print("6. Import/Export dữ liệu")  
        print("0. Quay lại menu chính")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            service.them_sinh_vien()
        elif lua_chon == '2':
            service.xoa_sinh_vien()
        elif lua_chon == '3':
            service.cap_nhat_sinh_vien()
        elif lua_chon == '4':
            service.tim_kiem_sinh_vien()
        elif lua_chon == '5':
            service.hien_thi_danh_sach()
        elif lua_chon == '6':
            menu_import_export(service)  
        elif lua_chon == '0':
            break
        else:
            logging.warning("Lựa chọn không hợp lệ. Vui lòng thử lại.")
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

def menu_khoa(service):
    while True:
        print("\n----- QUẢN LÝ KHOA -----")
        print("1. Thêm khoa")
        print("2. Sửa khoa")
        print("3. Hiển thị danh sách khoa")
        print("0. Quay lại menu chính")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            service.them_khoa()
        elif lua_chon == '2':
            service.sua_khoa()
        elif lua_chon == '3':
            service.hien_thi_danh_sach_khoa()
        elif lua_chon == '0':
            break
        else:
            logging.warning("Lựa chọn không hợp lệ.")
            print("Lựa chọn không hợp lệ.")

def menu_chuong_trinh(service):
    while True:
        print("\n----- QUẢN LÝ CHƯƠNG TRÌNH ĐÀO TẠO -----")
        print("1. Thêm chương trình đào tạo")
        print("2. Sửa chương trình đào tạo")
        print("3. Hiển thị danh sách chương trình đào tạo")
        print("0. Quay lại menu chính")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            service.them_chuong_trinh()
        elif lua_chon == '2':
            service.sua_chuong_trinh()
        elif lua_chon == '3':
            service.hien_thi_danh_sach_chuong_trinh()
        elif lua_chon == '0':
            break
        else:
            logging.warning("Lựa chọn không hợp lệ.")
            print("Lựa chọn không hợp lệ.")

def menu_tinh_trang(service):
    while True:
        print("\n----- QUẢN LÝ TÌNH TRẠNG -----")
        print("1. Thêm tình trạng")
        print("2. Sửa tình trạng")
        print("3. Hiển thị danh sách tình trạng")
        print("0. Quay lại menu chính")

        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == '1':
            service.them_tinh_trang()
        elif lua_chon == '2':
            service.sua_tinh_trang()
        elif lua_chon == '3':
            service.hien_thi_danh_sach_tinh_trang()
        elif lua_chon == '0':
            break
        else:
            logging.warning("Lựa chọn không hợp lệ.")
            print("Lựa chọn không hợp lệ")

def main():
    sinhvien_service = SinhVienService()
    khoa_service = KhoaService()
    chuong_trinh_service = ChuongTrinhService()
    tinh_trang_service = TinhTrangService()

    while True:
        print("\n----- CHỌN MỤC QUẢN LÝ -----")
        print("1. Quản lý sinh viên")
        print("2. Quản lý khoa")
        print("3. Quản lý chương trình đào tạo")
        print("4. Quản lý tình trạng")
        print("5. Hiển thị thông tin phiên bản")
        print("0. Thoát")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            menu_sinh_vien(sinhvien_service)
        elif lua_chon == '2':
            menu_khoa(khoa_service)
        elif lua_chon == '3':
            menu_chuong_trinh(chuong_trinh_service)
        elif lua_chon == '4':
            menu_tinh_trang(tinh_trang_service)
        elif lua_chon == '5':
            show_version()
        elif lua_chon == '0':
            logging.info("Thoát chương trình.")
            print("Thoát chương trình.")
            break
        else:
            logging.warning("Lựa chọn không hợp lệ. Vui lòng thử lại.")
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()