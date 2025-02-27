import json
import logging
from utils.file_io import load_json_file, save_json_file

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    handlers=[logging.FileHandler("app.log", encoding="utf-8")]
)

class KhoaService:
    def __init__(self, khoa_file="data/khoa.json"):
        self.khoa_file = khoa_file
        self.danh_sach_khoa = load_json_file(khoa_file)
        logging.info(f"Đã tải dữ liệu khoa từ {khoa_file}")

    def them_khoa(self, ten_khoa_moi: str):
        """
        Thêm một khoa mới.
        Nếu tên khoa đã tồn tại, trả về thông báo lỗi.
        """
        if ten_khoa_moi in self.danh_sach_khoa:
            logging.warning(f"Tên khoa '{ten_khoa_moi}' đã tồn tại.")
            return f"Tên khoa '{ten_khoa_moi}' đã tồn tại. Vui lòng nhập tên khác."
        self.danh_sach_khoa.append(ten_khoa_moi)
        self.save_data()
        logging.info(f"Đã thêm khoa '{ten_khoa_moi}' thành công.")
        return f"Đã thêm khoa '{ten_khoa_moi}' thành công."

    def sua_khoa(self, ten_khoa_cu: str, ten_khoa_moi: str):
        """
        Sửa tên của một khoa.
        Nếu tên khoa cũ không tồn tại hoặc tên mới đã có, trả về thông báo lỗi.
        """
        if ten_khoa_cu not in self.danh_sach_khoa:
            logging.warning(f"Tên khoa '{ten_khoa_cu}' không tồn tại.")
            return f"Tên khoa '{ten_khoa_cu}' không tồn tại."
        if ten_khoa_moi in self.danh_sach_khoa:
            logging.warning(f"Tên khoa '{ten_khoa_moi}' đã tồn tại.")
            return f"Tên khoa '{ten_khoa_moi}' đã tồn tại. Vui lòng chọn tên khác."
        index = self.danh_sach_khoa.index(ten_khoa_cu)
        self.danh_sach_khoa[index] = ten_khoa_moi
        self.save_data()
        logging.info(f"Đã sửa khoa '{ten_khoa_cu}' thành '{ten_khoa_moi}'.")
        return f"Đã sửa khoa '{ten_khoa_cu}' thành '{ten_khoa_moi}'."

    def hien_thi_danh_sach_khoa(self):
        """
        Trả về danh sách các khoa dưới dạng list.
        """
        logging.info("Đã hiển thị danh sách khoa.")
        return self.danh_sach_khoa

    def save_data(self):
        save_json_file(self.danh_sach_khoa, self.khoa_file)
        logging.info(f"Đã lưu dữ liệu khoa vào {self.khoa_file}")
