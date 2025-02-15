# CSC13010_22KTPM3
# Báo cáo: Chương trình Quản Lý Sinh Viên

Em xin trình bày báo cáo về chương trình Quản Lý Sinh Viên, một ứng dụng Python đơn giản được xây dựng để quản lý thông tin sinh viên. Chương trình có các chức năng cơ bản như thêm, xóa, cập nhật, tìm kiếm và hiển thị danh sách sinh viên.

## Cấu trúc mã nguồn

Chương trình được tổ chức thành các thành phần chính như sau:

*   **Lớp `SinhVien`:**
    *   Định nghĩa lớp đối tượng `SinhVien`, đại diện cho thông tin của một sinh viên.
    *   Các thuộc tính bao gồm: `mssv` (Mã số sinh viên), `ho_ten` (Họ và tên), `ngay_sinh` (Ngày sinh), `gioi_tinh` (Giới tính), `khoa` (Khoa), `khoa_hoc` (Khóa học), `chuong_trinh` (Chương trình học), `dia_chi` (Địa chỉ), `email` (Địa chỉ email), `sdt` (Số điện thoại), và `tinh_trang` (Tình trạng học tập).
    *   Phương thức `__str__` được sử dụng để hiển thị thông tin của sinh viên một cách dễ đọc.

*   **Các hàm kiểm tra dữ liệu đầu vào:**
    *   `kiem_tra_email(email)`: Hàm này sử dụng biểu thức chính quy để kiểm tra tính hợp lệ của địa chỉ email.
    *   `kiem_tra_sdt(sdt)`: Hàm này kiểm tra tính hợp lệ của số điện thoại theo định dạng của Việt Nam.
    *   `kiem_tra_ngay_sinh(ngay_sinh)`: Hàm này kiểm tra xem ngày sinh có đúng định dạng `dd/mm/yyyy` hay không.

*   **Các hàm thực hiện chức năng quản lý sinh viên:**
    *   `them_sinh_vien(danh_sach_sinh_vien)`: Thêm một sinh viên mới vào danh sách, có kiểm tra các ràng buộc về dữ liệu.
    *   `xoa_sinh_vien(danh_sach_sinh_vien)`: Xóa một sinh viên khỏi danh sách dựa trên mã số sinh viên.
    *   `cap_nhat_sinh_vien(danh_sach_sinh_vien)`: Cập nhật thông tin của một sinh viên dựa trên mã số sinh viên, cho phép cập nhật từng trường thông tin một cách linh hoạt.
    *   `tim_kiem_sinh_vien(danh_sach_sinh_vien)`: Tìm kiếm sinh viên theo họ tên hoặc mã số sinh viên.
    *   `hien_thi_danh_sach(danh_sach_sinh_vien)`: Hiển thị danh sách tất cả sinh viên hiện có.

*   **Hàm `main()`:**
    *   Đây là hàm chính của chương trình, chứa vòng lặp để hiển thị menu và xử lý các lựa chọn tương ứng của người dùng.

## Hướng dẫn cài đặt và chạy chương trình

1.  **Tải file mã nguồn:** Tải file mã nguồn Python (`.py`) về máy tính.  (Giả sử tên file là `quan_ly_sinh_vien.py`).

2.  **Mở Terminal/Command Prompt:** Mở cửa sổ dòng lệnh (Terminal trên Linux/macOS hoặc Command Prompt trên Windows).

3.  **Di chuyển đến thư mục chứa file mã nguồn:** Sử dụng lệnh `cd` để di chuyển đến thư mục chứa file `main.py`.

    ```bash
    cd /duong/dan/den/thu/muc
    ```

4.  **Thực thi chương trình:** Sử dụng lệnh `python` (hoặc `python3` tùy thuộc vào cấu hình hệ thống) để chạy file mã nguồn:

    ```bash
    python main.py
    ```

5.  **Thao tác với chương trình:** Chương trình sẽ hiển thị một menu. Người dùng nhập các số tương ứng với các chức năng để thực hiện các thao tác thêm, xóa, cập nhật, tìm kiếm, và hiển thị danh sách sinh viên.

## Giao diện
