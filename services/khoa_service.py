import json
import logging
from utils.file_io import load_json_file, save_json_file

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler("app.log", encoding="utf-8"),
])

class KhoaService:
    def __init__(self, khoa_file="data/khoa.json"):
        self.khoa_file = khoa_file
        self.danh_sach_khoa = load_json_file(khoa_file)
        logging.info(f"Đã tải dữ liệu khoa từ {khoa_file}")

    def them_khoa(self):
        print("\nThêm khoa mới:")
        ten_khoa_moi = self._nhap_ten_khoa()
        self.danh_sach_khoa.append(ten_khoa_moi)
        self.save_data()
        logging.info(f"Đã thêm khoa '{ten_khoa_moi}' thành công.")
        print(f"Đã thêm khoa '{ten_khoa_moi}' thành công.")

    def sua_khoa(self):
        print("\nSửa tên khoa:")
        ten_khoa_cu = self._chon_khoa()
        if ten_khoa_cu:
            ten_khoa_moi = self._nhap_ten_khoa(ten_khoa_cu)
            index = self.danh_sach_khoa.index(ten_khoa_cu)
            self.danh_sach_khoa[index] = ten_khoa_moi
            self.save_data()
            logging.info(f"Đã sửa khoa '{ten_khoa_cu}' thành '{ten_khoa_moi}'.")
            print(f"Đã sửa khoa '{ten_khoa_cu}' thành '{ten_khoa_moi}'.")

    def hien_thi_danh_sach_khoa(self):
        print("\nDanh sách khoa:")
        if not self.danh_sach_khoa:
            print("[]")
        else:
            print(json.dumps(self.danh_sach_khoa, indent=2, ensure_ascii=False))
        logging.info("Đã hiển thị danh sách khoa.")

    def _nhap_ten_khoa(self, ten_khoa_cu=None):
        while True:
            if ten_khoa_cu:
                ten_khoa = (
                    input(
                        f"Nhập tên khoa mới (hoặc ấn Enter để giữ nguyên '{ten_khoa_cu}'): "
                    )
                    or ten_khoa_cu
                )
            else:
                ten_khoa = input("Nhập tên khoa: ")

            if ten_khoa not in self.danh_sach_khoa:
                return ten_khoa
            else:
                print(f"Tên khoa '{ten_khoa}' đã tồn tại. Vui lòng nhập tên khác.")

    def _chon_khoa(self):
        self.hien_thi_danh_sach_khoa()
        while True:
            ten_khoa = input("Nhập tên khoa bạn muốn chỉnh sửa: ")
            if ten_khoa in self.danh_sach_khoa:
                return ten_khoa
            else:
                print("Tên khoa không tồn tại. Vui lòng chọn lại.")

    def save_data(self):
        save_json_file(self.danh_sach_khoa, self.khoa_file)
        logging.info(f"Đã lưu dữ liệu khoa vào {self.khoa_file}")