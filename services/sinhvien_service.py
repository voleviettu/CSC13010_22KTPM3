import json
import logging
import pandas as pd
from models.sinhvien import SinhVien
from utils.validation import kiem_tra_email, kiem_tra_sdt, kiem_tra_ngay_sinh
from utils.file_io import load_sinhvien_data, save_sinhvien_data, load_json_file
from services.khoa_service import KhoaService
from services.chuongtrinh_service import ChuongTrinhService
from services.tinhtrang_service import TinhTrangService

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler("app.log", encoding="utf-8"),
])

class SinhVienService:
    def __init__(
        self,
        sinhvien_data_file="data/sinhvien.json",
        khoa_file="data/khoa.json",
        tinh_trang_file="data/tinhtrang.json",
        chuong_trinh_file="data/chuongtrinh.json",
    ):
        self.sinhvien_data_file = sinhvien_data_file
        self.danh_sach_sinh_vien = load_sinhvien_data(sinhvien_data_file)
        self.khoa_service = KhoaService(khoa_file)
        self.danh_sach_khoa = self.khoa_service.danh_sach_khoa
        self.chuong_trinh_service = ChuongTrinhService(chuong_trinh_file)
        self.danh_sach_chuong_trinh = self.chuong_trinh_service.danh_sach_chuong_trinh
        self.tinh_trang_service = TinhTrangService(tinh_trang_file)
        self.danh_sach_tinh_trang = self.tinh_trang_service.danh_sach_tinh_trang
        logging.info(f"Đã tải dữ liệu sinh viên từ {sinhvien_data_file}")

    def them_sinh_vien(self):
        print("\nThêm sinh viên mới:")
        mssv = self._nhap_mssv()
        ho_ten = input("Nhập họ tên: ")
        ngay_sinh = self._nhap_ngay_sinh()
        gioi_tinh = input("Nhập giới tính (Nam/Nữ/Khác): ")
        khoa = self._nhap_khoa()
        khoa_hoc = input("Nhập khóa: ")
        chuong_trinh = self._nhap_chuong_trinh()
        dia_chi = input("Nhập địa chỉ: ")
        email = self._nhap_email()
        sdt = self._nhap_sdt()
        tinh_trang = self._nhap_tinh_trang()

        sinh_vien_moi = SinhVien(
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
        )
        self.danh_sach_sinh_vien.append(sinh_vien_moi)
        self.save_data()
        logging.info(f"Đã thêm sinh viên '{ho_ten}' thành công.")
        print("Thêm sinh viên thành công!")

    def xoa_sinh_vien(self):
        mssv_can_xoa = input("Nhập MSSV của sinh viên cần xóa: ")
        for i, sv in enumerate(self.danh_sach_sinh_vien):
            if sv.mssv == mssv_can_xoa:
                del self.danh_sach_sinh_vien[i]
                self.save_data()
                logging.info(f"Đã xóa sinh viên có MSSV {mssv_can_xoa}")
                print("Đã xóa sinh viên có MSSV", mssv_can_xoa)
                return
        logging.warning(f"Không tìm thấy sinh viên có MSSV {mssv_can_xoa}")
        print("Không tìm thấy sinh viên có MSSV", mssv_can_xoa)

    def cap_nhat_sinh_vien(self):
        mssv_can_cap_nhat = input("Nhập MSSV của sinh viên cần cập nhật: ")
        for sv in self.danh_sach_sinh_vien:
            if sv.mssv == mssv_can_cap_nhat:
                print("Nhập thông tin mới (để trống nếu không muốn thay đổi):")
                sv.ho_ten = input(f"Họ tên ({sv.ho_ten}): ") or sv.ho_ten
                sv.ngay_sinh = self._nhap_ngay_sinh(sv.ngay_sinh)
                sv.gioi_tinh = input(f"Giới tính ({sv.gioi_tinh}): ") or sv.gioi_tinh
                sv.khoa = self._nhap_khoa(sv.khoa)
                sv.khoa_hoc = input(f"Khóa ({sv.khoa_hoc}): ") or sv.khoa_hoc
                sv.chuong_trinh = self._nhap_chuong_trinh(sv.chuong_trinh)
                sv.dia_chi = input(f"Địa chỉ ({sv.dia_chi}): ") or sv.dia_chi
                sv.email = self._nhap_email(sv.email)
                sv.sdt = self._nhap_sdt(sv.sdt)
                sv.tinh_trang = self._nhap_tinh_trang(sv.tinh_trang)

                self.save_data()
                logging.info(f"Đã cập nhật thông tin sinh viên có MSSV {mssv_can_cap_nhat}")
                print("Cập nhật thông tin thành công!")
                return

        logging.warning(f"Không tìm thấy sinh viên có MSSV {mssv_can_cap_nhat}")
        print("Không tìm thấy sinh viên có MSSV", mssv_can_cap_nhat)

    def tim_kiem_sinh_vien(self):
        print("Chọn tiêu chí tìm kiếm:")
        print("1: Tìm theo Họ tên")
        print("2: Tìm theo MSSV")
        print("3: Tìm theo Khoa")
        print("4: Tìm theo Khoa và Họ tên")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == "1":
            ten_can_tim = input("Nhập họ tên cần tìm: ")
            ket_qua = [
                sv
                for sv in self.danh_sach_sinh_vien
                if ten_can_tim.lower() in sv.ho_ten.lower()
            ]
        elif lua_chon == "2":
            mssv_can_tim = input("Nhập MSSV cần tìm: ")
            ket_qua = [sv for sv in self.danh_sach_sinh_vien if sv.mssv == mssv_can_tim]
        elif lua_chon == "3":
            ten_khoa_can_tim = input("Nhập tên khoa cần tìm: ")
            ket_qua = [
                sv
                for sv in self.danh_sach_sinh_vien
                if sv.khoa.lower() == ten_khoa_can_tim.lower()
            ]
        elif lua_chon == "4":
            ten_khoa_can_tim = input("Nhập tên khoa cần tìm: ")
            ten_can_tim = input("Nhập họ tên cần tìm: ")
            ket_qua = [
                sv
                for sv in self.danh_sach_sinh_vien
                if sv.khoa.lower() == ten_khoa_can_tim.lower()
                and ten_can_tim.lower() in sv.ho_ten.lower()
            ]
        else:
            logging.warning("Lựa chọn không hợp lệ.")
            print("Lựa chọn không hợp lệ.")
            return

        if ket_qua:
            logging.info(f"Tìm thấy {len(ket_qua)} sinh viên.")
            print("\nKết quả tìm kiếm:")
            for sv in ket_qua:
                print(sv)
        else:
            logging.info("Không tìm thấy sinh viên nào.")
            print("Không tìm thấy sinh viên nào.")

    def hien_thi_danh_sach(self):
        print("\nDanh sách sinh viên:")
        if not self.danh_sach_sinh_vien:
            print("[]")
            logging.info("Danh sách sinh viên trống.")
            return
        data = [sv.to_dict() for sv in self.danh_sach_sinh_vien]
        print(json.dumps(data, ensure_ascii=False, indent=4))
        logging.info("Đã hiển thị danh sách sinh viên.")

    def save_data(self, filename=None, file_type=None):
        save_sinhvien_data(self.danh_sach_sinh_vien, filename or self.sinhvien_data_file, file_type or "json")
        logging.info(f"Đã lưu dữ liệu sinh viên vào {filename or self.sinhvien_data_file}")

    def _nhap_mssv(self):
        while True:
            mssv = input("Nhập MSSV: ")
            if not any(sv.mssv == mssv for sv in self.danh_sach_sinh_vien):
                return mssv
            logging.warning(f"MSSV {mssv} đã tồn tại.")
            print("MSSV đã tồn tại. Vui lòng nhập lại.")

    def _nhap_ngay_sinh(self, default_value=""):
        while True:
            ngay_sinh = (
                input(f"Nhập ngày sinh (dd/mm/yyyy) ({default_value}): ")
                or default_value
            )
            if kiem_tra_ngay_sinh(ngay_sinh):
                return ngay_sinh
            logging.warning("Ngày sinh không hợp lệ.")
            print(
                "Ngày sinh không hợp lệ. Vui lòng nhập lại theo định dạng dd/mm/yyyy."
            )

    def _nhap_khoa(self, default_value=""):
        self.khoa_service.hien_thi_danh_sach_khoa()
        while True:
            khoa = input(f"Nhập khoa ({default_value}): ") or default_value
            if khoa in self.khoa_service.danh_sach_khoa or khoa == "":
                return khoa
            logging.warning("Khoa không hợp lệ.")
            print("Khoa không hợp lệ. Vui lòng chọn một trong các khoa đã liệt kê.")

    def _nhap_chuong_trinh(self, default_value=""):
        self.chuong_trinh_service.hien_thi_danh_sach_chuong_trinh()
        while True:
            chuong_trinh = (
                input(f"Nhập chương trình ({default_value}): ") or default_value
            )
            if (
                chuong_trinh in self.chuong_trinh_service.danh_sach_chuong_trinh
                or chuong_trinh == ""
            ):
                return chuong_trinh
            logging.warning("Chương trình không hợp lệ.")
            print(
                "Chương trình không hợp lệ.  Vui lòng chọn một trong các chương trình đã liệt kê"
            )

    def _nhap_email(self, default_value=""):
        while True:
            email = input(f"Nhập email ({default_value}): ") or default_value
            if email == "" or kiem_tra_email(email):
                return email
            logging.warning("Email không hợp lệ.")
            print("Email không hợp lệ. Vui lòng nhập lại.")

    def _nhap_sdt(self, default_value=""):
        while True:
            sdt = input(f"Nhập số điện thoại ({default_value}): ") or default_value
            if sdt == "" or kiem_tra_sdt(sdt):
                return sdt
            logging.warning("Số điện thoại không hợp lệ.")
            print("Số điện thoại không hợp lệ. Vui lòng nhập lại.")

    def _nhap_tinh_trang(self, default_value=""):
        self.tinh_trang_service.hien_thi_danh_sach_tinh_trang()
        while True:
            tinh_trang = input(f"Nhập tình trạng ({default_value}): ") or default_value
            if (
                tinh_trang in self.tinh_trang_service.danh_sach_tinh_trang
                or tinh_trang == ""
            ):
                return tinh_trang
            logging.warning("Tình trạng không hợp lệ.")
            print(
                "Tình trạng không hợp lệ. Vui lòng chọn một trong các tình trạng đã liệt kê."
            )

    def import_data(self, file_type):
        filename = input(f"Nhập tên file {file_type} để import (bao gồm phần mở rộng .csv hoặc .json): ")
        try:
            new_data = load_sinhvien_data(filename, file_type)
            self.danh_sach_sinh_vien.extend(new_data)  # Thêm vào danh sách hiện tại
            self.save_data()
            logging.info(f"Import dữ liệu từ file {file_type} thành công.")
            print(f"Import dữ liệu từ file {file_type} thành công.")
        except Exception as e:
            logging.error(f"Lỗi khi import: {e}")
            print(f"Lỗi khi import: {e}")

    def export_data(self, file_type):
        filename = input("Nhập tên file để export (bao gồm phần mở rộng .csv hoặc .json): ")
        self.save_data(filename, file_type)  # Sử dụng hàm save_data có sẵn
        logging.info(f"Export thành công ra file {filename}.")
        print(f"Export thành công ra file {filename}.")