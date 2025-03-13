import json
import logging
import datetime
import pandas as pd
from models.sinhvien import SinhVien
from utils.validation import kiem_tra_email, kiem_tra_sdt, kiem_tra_ngay_sinh, kiem_tra_trang_thai
from utils.file_io import load_sinhvien_data, save_sinhvien_data, load_json_file
from services.khoa_service import KhoaService
from services.chuongtrinh_service import ChuongTrinhService
from services.tinhtrang_service import TinhTrangService

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
DELETION_TIME_LIMIT = config['DELETION_TIME_LIMIT']

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("app.log", encoding="utf-8")]
)

class SinhVienService:
    def __init__(
        self,
        sinhvien_data_file="data/sinhvien",
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

    def them_sinh_vien(self, student_data: dict):
        mssv = student_data.get("mssv")
        # Kiểm tra trùng MSSV
        if any(sv.mssv == mssv for sv in self.danh_sach_sinh_vien):
            logging.warning(f"MSSV {mssv} đã tồn tại.")
            return f"MSSV {mssv} đã tồn tại. Vui lòng sử dụng MSSV khác."

        # Kiểm tra định dạng ngày sinh
        ngay_sinh = student_data.get("ngay_sinh")
        if ngay_sinh and not kiem_tra_ngay_sinh(ngay_sinh):
            logging.warning("Ngày sinh không hợp lệ.")
            return "Ngày sinh không hợp lệ. Vui lòng nhập theo định dạng dd/mm/yyyy."

        # Kiểm tra email
        email = student_data.get("email")
        if email and not kiem_tra_email(email):
            logging.warning("Email không hợp lệ.")
            return "Email không hợp lệ. Vui lòng nhập lại."

        # Kiểm tra số điện thoại
        sdt = student_data.get("sdt")
        if sdt and not kiem_tra_sdt(sdt):
            logging.warning("Số điện thoại không hợp lệ.")
            return "Số điện thoại không hợp lệ. Vui lòng nhập lại."

        # Tạo đối tượng SinhVien mới
        sinh_vien_moi = SinhVien(
            mssv,
            student_data.get("ho_ten"),
            ngay_sinh,
            student_data.get("gioi_tinh"),
            student_data.get("khoa"),
            student_data.get("khoa_hoc"),
            student_data.get("chuong_trinh"),
            student_data.get("dia_chi"),
            email,
            sdt,
            student_data.get("tinh_trang"),
        )
        self.danh_sach_sinh_vien.append(sinh_vien_moi)
        self.save_data()
        logging.info(f"Đã thêm sinh viên '{sinh_vien_moi.ho_ten}' thành công.")
        return "Thêm sinh viên thành công!"

    def xoa_sinh_vien(self, mssv_can_xoa: str):
        for i, sv in enumerate(self.danh_sach_sinh_vien):
            if sv.mssv == mssv_can_xoa:
                # Kiểm tra thời gian tạo
                time_difference = datetime.datetime.now() - sv.creation_datetime
                if time_difference.total_seconds() / 60 <= DELETION_TIME_LIMIT:
                    del self.danh_sach_sinh_vien[i]
                    self.save_data()
                    logging.info(f"Đã xóa sinh viên có MSSV {mssv_can_xoa}")
                    return f"Đã xóa sinh viên có MSSV {mssv_can_xoa}"
                else:
                    logging.warning(
                        f"Không thể xóa sinh viên có MSSV {mssv_can_xoa} vì đã quá thời gian quy định."
                    )
                    return (
                        f"Không thể xóa sinh viên có MSSV {mssv_can_xoa} vì đã quá thời gian quy định ("
                        f"{DELETION_TIME_LIMIT} phút)."
                    )

        logging.warning(f"Không tìm thấy sinh viên có MSSV {mssv_can_xoa}")
        return f"Không tìm thấy sinh viên có MSSV {mssv_can_xoa}"

    def cap_nhat_sinh_vien(self, mssv_can_cap_nhat: str, updated_data: dict):
        """
        Cập nhật thông tin sinh viên dựa theo MSSV.
        updated_data chứa các key muốn cập nhật. Nếu key không có trong dict thì giữ nguyên.
        """

        for sv in self.danh_sach_sinh_vien:
            if sv.mssv == mssv_can_cap_nhat:
                sv.ho_ten = updated_data.get("ho_ten", sv.ho_ten)
                
                new_ngay_sinh = updated_data.get("ngay_sinh", sv.ngay_sinh)
                if new_ngay_sinh and not kiem_tra_ngay_sinh(new_ngay_sinh):
                    logging.warning("Ngày sinh không hợp lệ.")
                    return "Ngày sinh không hợp lệ. Vui lòng nhập theo định dạng dd/mm/yyyy."
                sv.ngay_sinh = new_ngay_sinh
                
                sv.gioi_tinh = updated_data.get("gioi_tinh", sv.gioi_tinh)
                sv.khoa = updated_data.get("khoa", sv.khoa)
                sv.khoa_hoc = updated_data.get("khoa_hoc", sv.khoa_hoc)
                sv.chuong_trinh = updated_data.get("chuong_trinh", sv.chuong_trinh)
                sv.dia_chi = updated_data.get("dia_chi", sv.dia_chi)
                
                new_email = updated_data.get("email", sv.email)
                if new_email and not kiem_tra_email(new_email):
                    logging.warning("Email không hợp lệ.")
                    return "Email không hợp lệ. Vui lòng nhập lại."
                sv.email = new_email
                
                new_sdt = updated_data.get("sdt", sv.sdt)
                if new_sdt and not kiem_tra_sdt(new_sdt):
                    logging.warning("Số điện thoại không hợp lệ.")
                    return "Số điện thoại không hợp lệ. Vui lòng nhập lại."
                sv.sdt = new_sdt
                
                new_tinh_trang = updated_data.get("tinh_trang", sv.tinh_trang)
                if new_tinh_trang and not kiem_tra_trang_thai(sv.tinh_trang, new_tinh_trang):
                    logging.warning(f"Không thể thay đổi tình trạng từ {sv.tinh_trang} sang {new_tinh_trang}.")
                    return f"Không thể thay đổi tình trạng từ {sv.tinh_trang} sang {new_tinh_trang}."
                sv.tinh_trang = new_tinh_trang
                
                self.save_data()
                logging.info(f"Đã cập nhật thông tin sinh viên có MSSV {mssv_can_cap_nhat}")
                return "Cập nhật thông tin thành công!"
        
        logging.warning(f"Không tìm thấy sinh viên có MSSV {mssv_can_cap_nhat}")
        return f"Không tìm thấy sinh viên có MSSV {mssv_can_cap_nhat}"


    def tim_kiem_sinh_vien(self, criteria: str, value: str, additional_value: str = None):
        """
        Tìm kiếm sinh viên dựa theo tiêu chí:
          - criteria: 'ho_ten', 'mssv', 'khoa' hoặc 'khoa_ho_ten'
          - value: giá trị tìm kiếm chính
          - additional_value: giá trị phụ (chỉ sử dụng khi criteria = 'khoa_ho_ten')
        Trả về danh sách các sinh viên dưới dạng dict.
        """
        if criteria == "ho_ten":
            ket_qua = [sv for sv in self.danh_sach_sinh_vien if value.lower() in sv.ho_ten.lower()]
        elif criteria == "mssv":
            ket_qua = [sv for sv in self.danh_sach_sinh_vien if sv.mssv == value]
        elif criteria == "khoa":
            ket_qua = [sv for sv in self.danh_sach_sinh_vien if sv.khoa.lower() == value.lower()]
        elif criteria == "khoa_ho_ten":
            ket_qua = [sv for sv in self.danh_sach_sinh_vien if sv.khoa.lower() == value.lower() and additional_value and additional_value.lower() in sv.ho_ten.lower()]
        else:
            logging.warning("Lựa chọn tiêu chí tìm kiếm không hợp lệ.")
            return []

        logging.info(f"Tìm thấy {len(ket_qua)} sinh viên.")
        return [sv.to_dict() for sv in ket_qua]

    def hien_thi_danh_sach(self):
        """
        Trả về danh sách sinh viên dưới dạng list các dict.
        """
        if not self.danh_sach_sinh_vien:
            logging.info("Danh sách sinh viên trống.")
            return []
        data = [sv.to_dict() for sv in self.danh_sach_sinh_vien]
        logging.info("Đã hiển thị danh sách sinh viên.")
        return data

    def save_data(self, filename=None, file_type=None):
        """
        Lưu lại dữ liệu sinh viên.
        Nếu không có filename, sử dụng file mặc định được cấu hình.
        """
        save_sinhvien_data(self.danh_sach_sinh_vien, filename or self.sinhvien_data_file, file_type or "json")
        logging.info(f"Đã lưu dữ liệu sinh viên vào {filename or self.sinhvien_data_file}")

    def import_data(self, filename: str, file_type: str):
        """
        Import dữ liệu từ file có định dạng file_type (csv hoặc json)
        """
        try:
            new_data = load_sinhvien_data(filename, file_type)
            self.danh_sach_sinh_vien.extend(new_data)
            self.save_data()
            logging.info(f"Import dữ liệu từ file {file_type} thành công.")
            return f"Import dữ liệu từ file {file_type} thành công."
        except Exception as e:
            logging.error(f"Lỗi khi import: {e}")
            return f"Lỗi khi import: {e}"

    def export_data(self, filename: str, file_type: str):
        """
        Export dữ liệu ra file với định dạng file_type (csv hoặc json)
        """
        self.save_data(filename, file_type)
        logging.info(f"Export thành công ra file {filename}.")
        return f"Export thành công ra file {filename}."
    
    def xuat_giay_xac_nhan(self, student_data: dict, purpose: str, expiry_date: str, file_type: str):
        """
        Xuất giấy xác nhận tình trạng sinh viên.

        Args:
            student_data: Dictionary chứa thông tin sinh viên.
            purpose: Mục đích xác nhận.
            expiry_date: Ngày hết hạn (dd/mm/yyyy).
            file_type: "md" hoặc "html".

        Returns:
            Tuple: (dữ liệu file, tên file) hoặc (None, None) nếu có lỗi.
        """
        # Tạo nội dung giấy xác nhận
        noi_dung = self._tao_noi_dung_giay_xac_nhan(student_data, purpose, expiry_date)

        # Tạo tên file
        ten_file = f"GiayXacNhan_{student_data['mssv']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.{file_type}"

        try:
            if file_type == "md":
                # Xuất ra Markdown
                return noi_dung.encode('utf-8'), ten_file  # Encode sang UTF-8
            elif file_type == "html":
                # Xuất ra HTML
                noi_dung_html = self._xuat_html(noi_dung)
                return noi_dung_html.encode('utf-8'), ten_file
            else:
                logging.error("Định dạng file không hỗ trợ.")
                return None, None
        except Exception as e:
            logging.error(f"Lỗi khi xuất file: {e}")
            return None, None

    def _tao_noi_dung_giay_xac_nhan(self, student_data: dict, purpose: str, expiry_date: str) -> str:
        # Phần này giữ nguyên như trước, tạo nội dung Markdown
        tinh_trang_text = ""
        if student_data["tinh_trang"] == "Đang học":
            tinh_trang_text = "- Đang theo học"
        elif student_data["tinh_trang"] == "Đã tốt nghiệp":
            tinh_trang_text = "- Đã tốt nghiệp"
        elif student_data["tinh_trang"] == "Đã thôi học":
            tinh_trang_text = "- Đã thôi học"
        elif student_data["tinh_trang"] == "Tạm dừng học":
            tinh_trang_text = "- Tạm dừng học"
        elif student_data["tinh_trang"] == "Bảo lưu":
            tinh_trang_text = "- Bảo lưu"
        elif student_data["tinh_trang"] == "Đình chỉ":
            tinh_trang_text = "- Đình chỉ"


        muc_dich_text = ""
        if purpose == "Vay vốn ngân hàng":
            muc_dich_text = "- Xác nhận đang học để vay vốn ngân hàng"
        elif purpose == "Tạm hoãn nghĩa vụ quân sự":
            muc_dich_text = "- Xác nhận làm thủ tục tạm hoãn nghĩa vụ quân sự"
        elif purpose == "Xin việc/Thực tập":
            muc_dich_text = "- Xác nhận làm hồ sơ xin việc / thực tập"
        else:
            muc_dich_text = f"- {purpose}"

        noi_dung = f"""
**TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN**
**PHÒNG ĐÀO TẠO**
📍 Địa chỉ: 227 Nguyễn Văn Cừ, Quận 5, Thành phố Hồ Chí Minh
📞 Điện thoại: 0123456789 | 📧 Email: hcmus@gmail.edu.vn

---

### **GIẤY XÁC NHẬN TÌNH TRẠNG SINH VIÊN**

Trường Đại học Khoa học Tự Nhiên xác nhận:

**1. Thông tin sinh viên:**
- **Họ và tên:** {student_data['ho_ten']}
- **Mã số sinh viên:** {student_data['mssv']}
- **Ngày sinh:** {datetime.datetime.strptime(student_data['ngay_sinh'], '%Y/%m/%d').strftime('%d/%m/%Y')}
- **Giới tính:** {student_data['gioi_tinh']}
- **Khoa:** {student_data['khoa']}
- **Chương trình đào tạo:** {student_data['chuong_trinh']}
- **Khóa:** {student_data['khoa_hoc']}

**2. Tình trạng sinh viên hiện tại:**
{tinh_trang_text}

**3. Mục đích xác nhận:**
{muc_dich_text}

**4. Thời gian cấp giấy:**
- Giấy xác nhận có hiệu lực đến ngày: {expiry_date}

📍 **Xác nhận của Trường Đại học Khoa học Tự nhiên**

📅 Ngày cấp: {datetime.datetime.now().strftime('%d/%m/%Y')}

🖋 **Trưởng Phòng Đào Tạo**
(Ký, ghi rõ họ tên, đóng dấu)

---
"""
        return noi_dung

    def _xuat_html(self, noi_dung: str):
        from markdown import markdown

        # Chuyển đổi nội dung Markdown sang HTML
        html = markdown(noi_dung)

        # Thêm một chút CSS để định dạng cơ bản (tùy chọn)
        html_with_style = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Giấy Xác Nhận Tình Trạng Sinh Viên</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }}
        h1, h3 {{
            text-align: center;
        }}
        .bold {{
            font-weight: bold;
        }}
    </style>
</head>
<body>
    {html}
</body>
</html>
"""
        return html_with_style
