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

Hệ thống sử dụng cơ chế logging để ghi lại các hoạt động và lỗi xảy ra trong quá trình chạy chương trình. Các log được ghi vào các file log riêng biệt cho từng module:

- `app.log`: Ghi lại các hoạt động và lỗi chung của hệ thống.
- `validation.log`: Ghi lại các hoạt động và lỗi liên quan đến việc kiểm tra dữ liệu (email, số điện thoại, ngày sinh).

## Hướng dẫn cài đặt và chạy chương trình

1.  **Tải file mã nguồn:** Tải file mã nguồn Python (`.py`) về máy tính. (Giả sử tên file là `quan_ly_sinh_vien.py`).

2.  **Mở Terminal/Command Prompt:** Mở cửa sổ dòng lệnh (Terminal trên Linux/macOS hoặc Command Prompt trên Windows).

3.  **Di chuyển đến thư mục chứa file mã nguồn:** Sử dụng lệnh `cd` để di chuyển đến thư mục chứa file `main.py`.

    ```bash
    cd /duong/dan/den/thu/muc
    ```

4.  **Thực thi chương trình:** Sử dụng lệnh `python` để chạy file mã nguồn:

    ```bash
    python main.py
    ```

5.  **Thao tác với chương trình:** Chương trình sẽ hiển thị một menu. Người dùng nhập các số tương ứng với các chức năng để thực hiện các thao tác thêm, xóa, cập nhật, tìm kiếm, và hiển thị danh sách sinh viên.

## Giao diện

- Xem giao diện console trong folder images.
