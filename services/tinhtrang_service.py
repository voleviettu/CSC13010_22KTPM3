import json
import logging
from utils.file_io import load_json_file, save_json_file

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    handlers=[logging.FileHandler("app.log", encoding="utf-8")]
)

class TinhTrangService:
    def __init__(self, tinh_trang_file="data/tinhtrang.json", sinh_vien_file="data/sinhvien.json"):
        self.tinh_trang_file = tinh_trang_file
        self.sinh_vien_file = sinh_vien_file
        self.danh_sach_tinh_trang = load_json_file(tinh_trang_file)
        self.danh_sach_sinh_vien = load_json_file(sinh_vien_file)
        logging.info(f"Đã tải dữ liệu tình trạng từ {tinh_trang_file}")

    def them_tinh_trang(self, ten_tinh_trang_moi: str) -> str:
        """
        Thêm tình trạng mới dựa trên tên được cung cấp.
        Nếu tên đã tồn tại, trả về thông báo lỗi.
        """
        if ten_tinh_trang_moi in self.danh_sach_tinh_trang:
            logging.warning(f"Tên tình trạng '{ten_tinh_trang_moi}' đã tồn tại.")
            return f"Tên tình trạng '{ten_tinh_trang_moi}' đã tồn tại. Vui lòng nhập tên khác."
        self.danh_sach_tinh_trang.append(ten_tinh_trang_moi)
        self.save_data()
        logging.info(f"Đã thêm tình trạng '{ten_tinh_trang_moi}' thành công.")
        return f"Đã thêm tình trạng '{ten_tinh_trang_moi}' thành công."

    def sua_tinh_trang(self, ten_tinh_trang_cu: str, ten_tinh_trang_moi: str) -> str:
        """
        Sửa tên của tình trạng.
        Nếu tên cũ không tồn tại hoặc tên mới đã có, trả về thông báo lỗi.
        """
        if ten_tinh_trang_cu not in self.danh_sach_tinh_trang:
            logging.warning(f"Tên tình trạng '{ten_tinh_trang_cu}' không tồn tại.")
            return f"Tên tình trạng '{ten_tinh_trang_cu}' không tồn tại."
        if ten_tinh_trang_moi in self.danh_sach_tinh_trang:
            logging.warning(f"Tên tình trạng '{ten_tinh_trang_moi}' đã tồn tại.")
            return f"Tên tình trạng '{ten_tinh_trang_moi}' đã tồn tại. Vui lòng nhập tên khác."
        index = self.danh_sach_tinh_trang.index(ten_tinh_trang_cu)
        self.danh_sach_tinh_trang[index] = ten_tinh_trang_moi
        self.save_data()
        logging.info(f"Đã sửa tình trạng '{ten_tinh_trang_cu}' thành '{ten_tinh_trang_moi}'.")
        return f"Đã sửa tình trạng '{ten_tinh_trang_cu}' thành '{ten_tinh_trang_moi}'."
    
    def xoa_tinh_trang(self, ten_tinh_trang: str) -> str:
        if ten_tinh_trang not in self.danh_sach_tinh_trang:
            logging.warning(f"Tên tình trạng '{ten_tinh_trang}' không tồn tại.")
            return f"Tên tình trạng '{ten_tinh_trang}' không tồn tại."
        
        for sv in self.danh_sach_sinh_vien:
            if sv.get("tinh_trang") == ten_tinh_trang:
                logging.warning(f"Không thể xóa tình trạng '{ten_tinh_trang}' vì có sinh viên đang ở tình trạng này.")
                return f"Không thể xóa tình trạng '{ten_tinh_trang}' vì có sinh viên đang ở tình trạng này."
        
        self.danh_sach_tinh_trang.remove(ten_tinh_trang)
        self.save_data()
        logging.info(f"Đã xóa tình trạng '{ten_tinh_trang}' thành công.")
        return f"Đã xóa tình trạng '{ten_tinh_trang}' thành công."

    def hien_thi_danh_sach_tinh_trang(self) -> list:
        """
        Trả về danh sách tình trạng dưới dạng list.
        """
        logging.info("Đã hiển thị danh sách tình trạng.")
        return self.danh_sach_tinh_trang

    def save_data(self):
        save_json_file(self.danh_sach_tinh_trang, self.tinh_trang_file)
        logging.info(f"Đã lưu dữ liệu tình trạng vào {self.tinh_trang_file}")
