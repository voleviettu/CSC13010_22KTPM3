# Quản Lý Sinh Viên

Đây là chương trình Quản Lý Sinh Viên - bài tập môn Thiết kế phần mềm - một ứng dụng Python đơn giản được xây dựng để quản lý thông tin sinh viên. Chương trình có các chức năng cơ bản như thêm, xóa, cập nhật, tìm kiếm và hiển thị danh sách sinh viên, khoa, chương trình đào tạo và tình trạng.

## Cấu trúc mã nguồn

Chương trình được tổ chức thành các thành phần chính như sau:

- **Lớp `SinhVien`:**

  - Định nghĩa lớp đối tượng `SinhVien`, đại diện cho thông tin của một sinh viên.
  - Các thuộc tính bao gồm: `mssv` (Mã số sinh viên), `ho_ten` (Họ và tên), `ngay_sinh` (Ngày sinh), `gioi_tinh` (Giới tính), `khoa` (Khoa), `khoa_hoc` (Khóa học), `chuong_trinh` (Chương trình học), `dia_chi` (Địa chỉ), `email` (Địa chỉ email), `sdt` (Số điện thoại), và `tinh_trang` (Tình trạng học tập).
  - Phương thức `__str__` được sử dụng để hiển thị thông tin của sinh viên một cách dễ đọc.

- **Các hàm kiểm tra dữ liệu đầu vào:**

  - `kiem_tra_email(email)`: Hàm này sử dụng biểu thức chính quy để kiểm tra tính hợp lệ của địa chỉ email.
  - `kiem_tra_sdt(sdt)`: Hàm này kiểm tra tính hợp lệ của số điện thoại theo định dạng của Việt Nam.
  - `kiem_tra_ngay_sinh(ngay_sinh)`: Hàm này kiểm tra xem ngày sinh có đúng định dạng `dd/mm/yyyy` hay không.

- **Các hàm thực hiện chức năng quản lý sinh viên:**

  - `them_sinh_vien(danh_sach_sinh_vien)`: Thêm một sinh viên mới vào danh sách, có kiểm tra các ràng buộc về dữ liệu.
  - `xoa_sinh_vien(danh_sach_sinh_vien)`: Xóa một sinh viên khỏi danh sách dựa trên mã số sinh viên.
  - `cap_nhat_sinh_vien(danh_sach_sinh_vien)`: Cập nhật thông tin của một sinh viên dựa trên mã số sinh viên, cho phép cập nhật từng trường thông tin một cách linh hoạt.
  - `tim_kiem_sinh_vien(danh_sach_sinh_vien)`: Tìm kiếm sinh viên theo họ tên hoặc mã số sinh viên.
  - `hien_thi_danh_sach(danh_sach_sinh_vien)`: Hiển thị danh sách tất cả sinh viên hiện có.

- **Các hàm thực hiện chức năng quản lý khoa:**

  - `them_khoa(danh_sach_khoa)`: Thêm một khoa mới vào danh sách.
  - `sua_khoa(danh_sach_khoa)`: Sửa tên của một khoa trong danh sách.
  - `hien_thi_danh_sach_khoa(danh_sach_khoa)`: Hiển thị danh sách tất cả các khoa hiện có.

- **Các hàm thực hiện chức năng quản lý chương trình đào tạo:**

  - `them_chuong_trinh(danh_sach_chuong_trinh)`: Thêm một chương trình đào tạo mới vào danh sách.
  - `sua_chuong_trinh(danh_sach_chuong_trinh)`: Sửa tên của một chương trình đào tạo trong danh sách.
  - `hien_thi_danh_sach_chuong_trinh(danh_sach_chuong_trinh)`: Hiển thị danh sách tất cả các chương trình đào tạo hiện có.

- **Các hàm thực hiện chức năng quản lý tình trạng:**

  - `them_tinh_trang(danh_sach_tinh_trang)`: Thêm một tình trạng mới vào danh sách.
  - `sua_tinh_trang(danh_sach_tinh_trang)`: Sửa tên của một tình trạng trong danh sách.
  - `hien_thi_danh_sach_tinh_trang(danh_sach_tinh_trang)`: Hiển thị danh sách tất cả các tình trạng hiện có.

- **Hàm `main()`:**
  - Đây là hàm chính của chương trình, chứa vòng lặp để hiển thị menu và xử lý các lựa chọn tương ứng của người dùng.

## Logging Mechanism

Hệ thống sử dụng cơ chế logging để ghi lại các hoạt động và lỗi xảy ra trong quá trình chạy chương trình. Các log được ghi vào file `app.log`.

# Hướng Dẫn Cài Đặt và Sử Dụng Chương Trình Quản Lý Sinh Viên

## Cài Đặt Streamlit

1. **Cài đặt Python**: Đảm bảo rằng bạn đã cài đặt Python trên máy tính của mình. Bạn có thể tải Python từ [python.org](https://www.python.org/downloads/).

2. **Cài đặt Streamlit**: Mở Terminal (Linux/macOS) hoặc Command Prompt (Windows) và chạy lệnh sau để cài đặt Streamlit:
    ```sh
    pip install streamlit
    ```

## Chạy Chương Trình

1. **Tải file mã nguồn**: Tải cả project về máy tính của bạn.

2. **Mở Terminal/Command Prompt**: Mở cửa sổ dòng lệnh (Terminal trên Linux/macOS hoặc Command Prompt trên Windows).

3. **Di chuyển đến thư mục chứa file mã nguồn**: Sử dụng lệnh `cd` để di chuyển đến thư mục chứa file [main.py]:
    ```sh
    cd /duong/dan/den/thu/muc
    ```

4. **Chạy chương trình**: Sử dụng lệnh `streamlit run` để chạy file [main.py](http://_vscodecontentref_/4):
    ```sh
    streamlit run main.py
    ```

5. **Mở trình duyệt**: Chương trình sẽ tự động mở trình duyệt web và hiển thị giao diện quản lý sinh viên.

## Sử Dụng Chương Trình

### Menu Chính

Khi chạy chương trình, bạn sẽ thấy menu chính với các lựa chọn sau:

- **QUẢN LÝ SINH VIÊN**: Quản lý thông tin sinh viên.
- **QUẢN LÝ KHOA**: Quản lý thông tin khoa.
- **QUẢN LÝ CHƯƠNG TRÌNH ĐÀO TẠO**: Quản lý thông tin chương trình đào tạo.
- **QUẢN LÝ TÌNH TRẠNG**: Quản lý thông tin tình trạng sinh viên.
- **THÔNG TIN PHIÊN BẢN**: Hiển thị thông tin phiên bản của chương trình.

### Quản Lý Sinh Viên

1. **Thêm sinh viên**: Nhập thông tin sinh viên mới và nhấn nút "Thêm sinh viên".
2. **Xóa sinh viên**: Nhập MSSV của sinh viên cần xóa và nhấn nút "Xóa".
3. **Cập nhật thông tin sinh viên**: Nhập MSSV của sinh viên cần cập nhật, sau đó nhập thông tin mới và nhấn nút "Cập nhật".
4. **Tìm kiếm sinh viên**: Chọn tiêu chí tìm kiếm, nhập giá trị tìm kiếm và nhấn nút "Tìm kiếm".
5. **Hiển thị danh sách sinh viên**: Hiển thị danh sách tất cả sinh viên hiện có.
6. **Import/Export dữ liệu**: Import hoặc export dữ liệu sinh viên từ/ra file CSV hoặc JSON.

### Quản Lý Khoa

1. **Thêm khoa**: Nhập tên khoa mới và nhấn nút "Thêm khoa".
2. **Sửa khoa**: Chọn khoa cần sửa, nhập tên khoa mới và nhấn nút "Sửa khoa".
3. **Hiển thị danh sách khoa**: Hiển thị danh sách tất cả các khoa hiện có.

### Quản Lý Chương Trình Đào Tạo

1. **Thêm chương trình đào tạo**: Nhập tên chương trình đào tạo mới và nhấn nút "Thêm chương trình đào tạo".
2. **Sửa chương trình đào tạo**: Chọn chương trình cần sửa, nhập tên chương trình mới và nhấn nút "Sửa chương trình đào tạo".
3. **Hiển thị danh sách chương trình đào tạo**: Hiển thị danh sách tất cả các chương trình đào tạo hiện có.

### Quản Lý Tình Trạng

1. **Thêm tình trạng**: Nhập tên tình trạng mới và nhấn nút "Thêm tình trạng".
2. **Sửa tình trạng**: Chọn tình trạng cần sửa, nhập tên tình trạng mới và nhấn nút "Sửa tình trạng".
3. **Hiển thị danh sách tình trạng**: Hiển thị danh sách tất cả các tình trạng hiện có.

### Thông Tin Phiên Bản

Hiển thị thông tin phiên bản của chương trình từ file [version.txt](http://_vscodecontentref_/5).

---

## Giao diện

- Xem giao diện trong folder images.
