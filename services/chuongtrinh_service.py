import json
import logging
from utils.file_io import load_json_file, save_json_file

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s', 
    handlers=[logging.FileHandler("app.log", encoding="utf-8")]
)

class ChuongTrinhService:
    def __init__(self, chuong_trinh_file="data/chuongtrinh.json", sinh_vien_file="data/sinhvien.json"):
        self.chuong_trinh_file = chuong_trinh_file
        self.sinh_vien_file = sinh_vien_file
        self.danh_sach_chuong_trinh = load_json_file(chuong_trinh_file)
        self.danh_sach_sinh_vien = load_json_file(sinh_vien_file)
        logging.info(f"Đã tải dữ liệu chương trình từ {chuong_trinh_file}")

    def them_chuong_trinh(self, ten_chuong_trinh_moi: str) -> str:
        """
        Thêm chương trình đào tạo mới dựa trên tên chương trình.
        Nếu tên chương trình đã tồn tại, trả về thông báo lỗi.
        """
        if ten_chuong_trinh_moi in self.danh_sach_chuong_trinh:
            logging.warning(f"Tên chương trình đào tạo '{ten_chuong_trinh_moi}' đã tồn tại.")
            return f"Tên chương trình đào tạo '{ten_chuong_trinh_moi}' đã tồn tại. Vui lòng nhập tên khác."
        self.danh_sach_chuong_trinh.append(ten_chuong_trinh_moi)
        self.save_data()
        logging.info(f"Đã thêm chương trình đào tạo '{ten_chuong_trinh_moi}' thành công.")
        return f"Đã thêm chương trình đào tạo '{ten_chuong_trinh_moi}' thành công."
    
    def xoa_chuong_trinh(self, ten_chuong_trinh: str) -> str:
        """
        Xóa chương trình đào tạo nếu không có sinh viên nào theo học.
        """
        if ten_chuong_trinh not in self.danh_sach_chuong_trinh:
            logging.warning(f"Tên chương trình đào tạo '{ten_chuong_trinh}' không tồn tại.")
            return f"Tên chương trình đào tạo '{ten_chuong_trinh}' không tồn tại."

        # Kiểm tra xem có sinh viên nào đang theo học chương trình này không
        for sv in self.danh_sach_sinh_vien:
            if sv.get("chuong_trinh") == ten_chuong_trinh:
                logging.warning(f"Không thể xóa chương trình '{ten_chuong_trinh}' vì có sinh viên đang theo học.")
                return f"Không thể xóa chương trình '{ten_chuong_trinh}' vì có sinh viên đang theo học."

    def sua_chuong_trinh(self, ten_chuong_trinh_cu: str, ten_chuong_trinh_moi: str) -> str:
        """
        Sửa tên chương trình đào tạo.
        Nếu tên chương trình cũ không tồn tại hoặc tên mới đã có, trả về thông báo lỗi.
        """
        if ten_chuong_trinh_cu not in self.danh_sach_chuong_trinh:
            logging.warning(f"Tên chương trình đào tạo '{ten_chuong_trinh_cu}' không tồn tại.")
            return f"Tên chương trình đào tạo '{ten_chuong_trinh_cu}' không tồn tại."
        if ten_chuong_trinh_moi in self.danh_sach_chuong_trinh:
            logging.warning(f"Tên chương trình đào tạo '{ten_chuong_trinh_moi}' đã tồn tại.")
            return f"Tên chương trình đào tạo '{ten_chuong_trinh_moi}' đã tồn tại. Vui lòng chọn tên khác."
        index = self.danh_sach_chuong_trinh.index(ten_chuong_trinh_cu)
        self.danh_sach_chuong_trinh[index] = ten_chuong_trinh_moi
        self.save_data()
        logging.info(f"Đã sửa chương trình đào tạo '{ten_chuong_trinh_cu}' thành '{ten_chuong_trinh_moi}'.")
        return f"Đã sửa chương trình đào tạo '{ten_chuong_trinh_cu}' thành '{ten_chuong_trinh_moi}'."

    def hien_thi_danh_sach_chuong_trinh(self) -> list:
        """
        Trả về danh sách chương trình đào tạo.
        """
        logging.info("Đã hiển thị danh sách chương trình đào tạo.")
        return self.danh_sach_chuong_trinh

    def save_data(self):
        save_json_file(self.danh_sach_chuong_trinh, self.chuong_trinh_file)
        logging.info(f"Đã lưu dữ liệu chương trình vào {self.chuong_trinh_file}")
