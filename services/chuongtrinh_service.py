from utils.file_io import load_json_file, save_json_file
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler("app.log", encoding="utf-8"),
])

class ChuongTrinhService:
    def __init__(self, chuong_trinh_file="data/chuongtrinh.json"):
        self.chuong_trinh_file = chuong_trinh_file
        self.danh_sach_chuong_trinh = load_json_file(chuong_trinh_file)
        logging.info(f"Đã tải dữ liệu chương trình từ {chuong_trinh_file}")

    def them_chuong_trinh(self):
        print("\nThêm chương trình đào tạo mới:")
        ten_chuong_trinh_moi = self._nhap_ten_chuong_trinh()
        self.danh_sach_chuong_trinh.append(ten_chuong_trinh_moi)
        self.save_data()
        logging.info(f"Đã thêm chương trình đào tạo '{ten_chuong_trinh_moi}' thành công.")
        print(f"Đã thêm chương trình đào tạo '{ten_chuong_trinh_moi}' thành công.")

    def sua_chuong_trinh(self):
        print("\nSửa tên chương trình đào tạo:")
        ten_chuong_trinh_cu = self._chon_chuong_trinh()
        if ten_chuong_trinh_cu:
            ten_chuong_trinh_moi = self._nhap_ten_chuong_trinh(ten_chuong_trinh_cu)
            index = self.danh_sach_chuong_trinh.index(ten_chuong_trinh_cu)
            self.danh_sach_chuong_trinh[index] = ten_chuong_trinh_moi
            self.save_data()
            logging.info(f"Đã sửa chương trình đào tạo '{ten_chuong_trinh_cu}' thành '{ten_chuong_trinh_moi}'.")
            print(f"Đã sửa chương trình đào tạo '{ten_chuong_trinh_cu}' thành '{ten_chuong_trinh_moi}'.")

    def hien_thi_danh_sach_chuong_trinh(self):
        print("\nDanh sách chương trình đào tạo:")
        if not self.danh_sach_chuong_trinh:
            print("[]")  # Hoặc thông báo "Danh sách chương trình đào tạo trống"
        else:
            print(json.dumps(self.danh_sach_chuong_trinh, indent=2, ensure_ascii=False))
        logging.info("Đã hiển thị danh sách chương trình đào tạo.")

    def _nhap_ten_chuong_trinh(self, ten_chuong_trinh_cu=None):
        while True:
            if ten_chuong_trinh_cu:
                ten_chuong_trinh = (
                    input(
                        f"Nhập tên chương trình đào tạo mới (hoặc ấn Enter để giữ nguyên '{ten_chuong_trinh_cu}'): "
                    )
                    or ten_chuong_trinh_cu
                )
            else:
                ten_chuong_trinh = input("Nhập tên chương trình đào tạo: ")

            if ten_chuong_trinh not in self.danh_sach_chuong_trinh:
                return ten_chuong_trinh
            else:
                print(
                    f"Tên chương trình đào tạo '{ten_chuong_trinh}' đã tồn tại. Vui lòng nhập tên khác."
                )

    def _chon_chuong_trinh(self):
        self.hien_thi_danh_sach_chuong_trinh()
        while True:
            ten_chuong_trinh = input(
                "Nhập tên chương trình đào tạo bạn muốn chỉnh sửa: "
            )
            if ten_chuong_trinh in self.danh_sach_chuong_trinh:
                return ten_chuong_trinh
            else:
                print("Tên chương trình đào tạo không tồn tại. Vui lòng chọn lại.")

    def save_data(self):
        save_json_file(self.danh_sach_chuong_trinh, self.chuong_trinh_file)
        logging.info(f"Đã lưu dữ liệu chương trình vào {self.chuong_trinh_file}")