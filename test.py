import unittest
import tempfile
import os
import json

from services.sinhvien_service import SinhVienService
from utils.validation import kiem_tra_email, kiem_tra_sdt, kiem_tra_ngay_sinh, kiem_tra_trang_thai

class TestSinhVienService(unittest.TestCase):
    def setUp(self):
        # Tạo thư mục tạm và các file dữ liệu mẫu để không ảnh hưởng dữ liệu thật
        self.temp_dir = tempfile.TemporaryDirectory()
        
        # File sinh viên (dữ liệu ban đầu rỗng)
        self.sinhvien_file = os.path.join(self.temp_dir.name, "sinhvien.json")
        with open(self.sinhvien_file, "w", encoding="utf-8") as f:
            json.dump([], f)
        
        # File khoa: danh sách khoa theo cấu hình mới
        self.khoa_file = os.path.join(self.temp_dir.name, "khoa.json")
        valid_khoa = [
            "Khoa Luật",
            "Khoa Tiếng Anh thương mại",
            "Khoa Tiếng Nhật",
            "Khoa Tiếng Pháp",
            "Khoa Báo Chí"
        ]
        with open(self.khoa_file, "w", encoding="utf-8") as f:
            json.dump(valid_khoa, f)
        
        # File chương trình đào tạo
        self.chuongtrinh_file = os.path.join(self.temp_dir.name, "chuongtrinh.json")
        valid_chuong_trinh = [
            "Chất lượng cao",
            "Chuẩn",
            "Tiên tiến",
            "Tăng cường tiếng Anh"
        ]
        with open(self.chuongtrinh_file, "w", encoding="utf-8") as f:
            json.dump(valid_chuong_trinh, f)
        
        # File tình trạng: danh sách tình trạng theo cấu hình mới
        self.tinhtrang_file = os.path.join(self.temp_dir.name, "tinhtrang.json")
        valid_tinhtrang = [
            "Đang học",
            "Đã tốt nghiệp",
            "Đã thôi học",
            "Tạm dừng học",
            "Bảo lưu kết quả"
        ]
        with open(self.tinhtrang_file, "w", encoding="utf-8") as f:
            json.dump(valid_tinhtrang, f)
        
        self.service = SinhVienService(
            sinhvien_data_file=self.sinhvien_file,
            khoa_file=self.khoa_file,
            chuong_trinh_file=self.chuongtrinh_file,
            tinh_trang_file=self.tinhtrang_file
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_them_sinh_vien_valid(self):
        student_data = {
            "mssv": "001",
            "ho_ten": "Nguyen Van A",
            "ngay_sinh": "01/01/2000",
            "gioi_tinh": "Nam",
            "khoa": "Khoa Luật",
            "khoa_hoc": "2020",
            "chuong_trinh": "Chất lượng cao",
            "dia_chi": "Hanoi",
            "email": "nguyenvana@student.university.edu.vn",  # domain đúng theo config
            "sdt": "0912345678",                           # khớp với regex VALID_MOBILE
            "tinh_trang": "Đang học"                        # có trong danh sách tình trạng
        }
        result = self.service.them_sinh_vien(student_data)
        self.assertEqual(result, "Thêm sinh viên thành công!")
        # Thử thêm lại cùng MSSV
        result_duplicate = self.service.them_sinh_vien(student_data)
        self.assertIn("đã tồn tại", result_duplicate)

    def test_them_sinh_vien_invalid_email(self):
        student_data = {
            "mssv": "002",
            "ho_ten": "Nguyen Van B",
            "ngay_sinh": "02/02/2000",
            "gioi_tinh": "Nam",
            "khoa": "Khoa Luật",
            "khoa_hoc": "2020",
            "chuong_trinh": "Chuẩn",
            "dia_chi": "Hanoi",
            "email": "nguyenvanb@invalid.com",  # domain không đúng
            "sdt": "0912345678",
            "tinh_trang": "Đang học"
        }
        result = self.service.them_sinh_vien(student_data)
        self.assertIn("Email không hợp lệ", result)

    def test_them_sinh_vien_invalid_sdt(self):
        student_data = {
            "mssv": "003",
            "ho_ten": "Nguyen Van C",
            "ngay_sinh": "03/03/2000",
            "gioi_tinh": "Nam",
            "khoa": "Khoa Tiếng Nhật",
            "khoa_hoc": "2020",
            "chuong_trinh": "Tiên tiến",
            "dia_chi": "Hanoi",
            "email": "nguyenvanc@student.university.edu.vn",
            "sdt": "0123456789",  # không khớp với regex: số sau "0" phải là 3,5,7,8 hoặc 9
            "tinh_trang": "Đang học"
        }
        result = self.service.them_sinh_vien(student_data)
        self.assertIn("Số điện thoại không hợp lệ", result)

    def test_them_sinh_vien_invalid_ngay_sinh(self):
        student_data = {
            "mssv": "004",
            "ho_ten": "Nguyen Van D",
            "ngay_sinh": "31-12-2000",  # sai định dạng dd/mm/yyyy
            "gioi_tinh": "Nam",
            "khoa": "Khoa Tiếng Pháp",
            "khoa_hoc": "2020",
            "chuong_trinh": "Tăng cường tiếng Anh",
            "dia_chi": "Hanoi",
            "email": "nguyenvand@student.university.edu.vn",
            "sdt": "0912345678",
            "tinh_trang": "Đang học"
        }
        result = self.service.them_sinh_vien(student_data)
        self.assertIn("Ngày sinh không hợp lệ", result)

    def test_xoa_sinh_vien(self):
        student_data = {
            "mssv": "005",
            "ho_ten": "Nguyen Van E",
            "ngay_sinh": "04/04/2000",
            "gioi_tinh": "Nam",
            "khoa": "Khoa Báo Chí",
            "khoa_hoc": "2020",
            "chuong_trinh": "Chất lượng cao",
            "dia_chi": "Hanoi",
            "email": "nguyenvane@student.university.edu.vn",
            "sdt": "0912345678",
            "tinh_trang": "Đang học"
        }
        self.service.them_sinh_vien(student_data)
        result = self.service.xoa_sinh_vien("005")
        self.assertIn("Đã xóa", result)
        # Xóa lại phải báo không tìm thấy
        result_not_found = self.service.xoa_sinh_vien("005")
        self.assertIn("Không tìm thấy", result_not_found)

    def test_cap_nhat_sinh_vien(self):
        student_data = {
            "mssv": "006",
            "ho_ten": "Nguyen Van F",
            "ngay_sinh": "05/05/2000",
            "gioi_tinh": "Nam",
            "khoa": "Khoa Tiếng Anh thương mại",
            "khoa_hoc": "2020",
            "chuong_trinh": "Chuẩn",
            "dia_chi": "Hanoi",
            "email": "nguyenvanf@student.university.edu.vn",
            "sdt": "0912345678",
            "tinh_trang": "Đang học"
        }
        self.service.them_sinh_vien(student_data)
        # Cập nhật hợp lệ: chuyển từ "Đang học" sang "Đã tốt nghiệp" (vì "Đã tốt nghiệp" nằm trong danh sách)
        updated_data = {
            "ho_ten": "Nguyen Van F Updated",
            "ngay_sinh": "05/05/2000",
            "email": "nguyenvanf@student.university.edu.vn",
            "sdt": "0912345678",
            "tinh_trang": "Đã tốt nghiệp"
        }
        result = self.service.cap_nhat_sinh_vien("006", updated_data)
        self.assertIn("Cập nhật thông tin thành công", result)
        # Cập nhật không hợp lệ: chuyển sang trạng thái không có trong danh sách
        updated_data_invalid = {
            "tinh_trang": "Không hợp lệ"
        }
        result_invalid = self.service.cap_nhat_sinh_vien("006", updated_data_invalid)
        self.assertIn("Không thể thay đổi tình trạng", result_invalid)

    def test_tim_kiem_sinh_vien(self):
        students = [
            {
                "mssv": "007",
                "ho_ten": "Le Thi A",
                "ngay_sinh": "06/06/2000",
                "gioi_tinh": "Nữ",
                "khoa": "Khoa Tiếng Anh thương mại",
                "khoa_hoc": "2020",
                "chuong_trinh": "Tiên tiến",
                "dia_chi": "HCM",
                "email": "lethia@student.university.edu.vn",
                "sdt": "0912345678",
                "tinh_trang": "Đang học"
            },
            {
                "mssv": "008",
                "ho_ten": "Tran Van B",
                "ngay_sinh": "07/07/2000",
                "gioi_tinh": "Nam",
                "khoa": "Khoa Tiếng Anh thương mại",
                "khoa_hoc": "2020",
                "chuong_trinh": "Tăng cường tiếng Anh",
                "dia_chi": "HCM",
                "email": "tranvanb@student.university.edu.vn",
                "sdt": "0912345678",
                "tinh_trang": "Đang học"
            }
        ]
        for s in students:
            self.service.them_sinh_vien(s)
        # Tìm kiếm theo tên
        result_name = self.service.tim_kiem_sinh_vien("ho_ten", "Le")
        self.assertEqual(len(result_name), 1)
        # Tìm kiếm theo MSSV
        result_mssv = self.service.tim_kiem_sinh_vien("mssv", "008")
        self.assertEqual(len(result_mssv), 1)
        # Tìm kiếm theo khoa
        result_khoa = self.service.tim_kiem_sinh_vien("khoa", "Khoa Tiếng Anh thương mại")
        self.assertEqual(len(result_khoa), 2)
        # Tìm kiếm theo khoa_ho_ten
        result_khoa_hoten = self.service.tim_kiem_sinh_vien("khoa_ho_ten", "Khoa Tiếng Anh thương mại", "Tran")
        self.assertEqual(len(result_khoa_hoten), 1)

    def test_hien_thi_danh_sach(self):
        # Ban đầu danh sách rỗng
        result_empty = self.service.hien_thi_danh_sach()
        self.assertEqual(len(result_empty), 0)
        # Sau khi thêm sinh viên
        student_data = {
            "mssv": "009",
            "ho_ten": "Nguyen Van G",
            "ngay_sinh": "08/08/2000",
            "gioi_tinh": "Nam",
            "khoa": "Khoa Tiếng Nhật",
            "khoa_hoc": "2020",
            "chuong_trinh": "Chất lượng cao",
            "dia_chi": "Hanoi",
            "email": "nguyenvang@student.university.edu.vn",
            "sdt": "0912345678",
            "tinh_trang": "Đang học"
        }
        self.service.them_sinh_vien(student_data)
        result_non_empty = self.service.hien_thi_danh_sach()
        self.assertEqual(len(result_non_empty), 1)

class TestValidation(unittest.TestCase):
    def test_kiem_tra_email_valid(self):
        result = kiem_tra_email("user@student.university.edu.vn")
        self.assertTrue(result)

    def test_kiem_tra_email_invalid(self):
        result = kiem_tra_email("user@notstudent.edu.vn")
        self.assertFalse(result)

    def test_kiem_tra_sdt_valid(self):
        result = kiem_tra_sdt("0912345678")
        self.assertTrue(result)

    def test_kiem_tra_sdt_invalid(self):
        result = kiem_tra_sdt("0123456789")
        self.assertFalse(result)

    def test_kiem_tra_ngay_sinh_valid(self):
        result = kiem_tra_ngay_sinh("31/12/1999")
        self.assertTrue(result)

    def test_kiem_tra_ngay_sinh_invalid(self):
        result = kiem_tra_ngay_sinh("1999-12-31")
        self.assertFalse(result)

    def test_kiem_tra_trang_thai_valid(self):
        # Với cấu hình mới, chỉ cần kiểm tra new_status có nằm trong danh sách tình trạng không
        result = kiem_tra_trang_thai("Đang học", "Đã tốt nghiệp")
        self.assertTrue(result)

    def test_kiem_tra_trang_thai_invalid(self):
        result = kiem_tra_trang_thai("Đang học", "Không hợp lệ")
        self.assertFalse(result)

class TestFileIO(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.json_file = os.path.join(self.temp_dir.name, "test.json")
        self.csv_file = os.path.join(self.temp_dir.name, "test.csv")
        self.sample_data = [{"key": "value"}]

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_save_and_load_json_file(self):
        from utils.file_io import save_json_file, load_json_file
        save_json_file(self.sample_data, self.json_file)
        loaded_data = load_json_file(self.json_file)
        self.assertEqual(loaded_data, self.sample_data)

    def test_save_and_load_csv_file(self):
        from utils.file_io import save_csv_file, load_csv_file
        save_csv_file(self.sample_data, self.csv_file)
        loaded_data = load_csv_file(self.csv_file)
        self.assertEqual(loaded_data[0]["key"], "value")

if __name__ == "__main__":
    unittest.main()
