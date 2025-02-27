import streamlit as st
import datetime
import logging
import pandas as pd
from PIL import Image
from services.sinhvien_service import SinhVienService
from services.khoa_service import KhoaService
from services.chuongtrinh_service import ChuongTrinhService
from services.tinhtrang_service import TinhTrangService

# Cấu hình logging (nếu cần lưu log vào file, bạn có thể giữ lại hoặc điều chỉnh cho phù hợp)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def show_version():
    try:
        with open("version.txt", "r", encoding="utf-8") as file:
            version_info = file.read()
            st.text(version_info)
    except FileNotFoundError:
        st.error("Không tìm thấy file version.txt.")

def menu_import_export(service):
    st.subheader("IMPORT/EXPORT SINH VIÊN")
    option = st.selectbox(
        "Chọn thao tác", 
        ("Import từ file CSV", "Import từ file JSON", "Export ra file CSV", "Export ra file JSON")
    )
    
    # Dựa vào lựa chọn, hiển thị ô nhập tên file
    if option.startswith("Import"):
        filename = st.text_input("Nhập đường dẫn file cần import (bao gồm phần mở rộng)")
    else:
        filename = st.text_input("Nhập tên file để export (bao gồm phần mở rộng)")
    
    if st.button("Thực hiện"):
        if option == "Import từ file CSV":
            result = service.import_data(filename, "csv")
            if "thành công" in result.lower():
                st.success(result)
            else:
                st.error(result)
        elif option == "Import từ file JSON":
            result = service.import_data(filename, "json")
            if "thành công" in result.lower():
                st.success(result)
            else:
                st.error(result)
        elif option == "Export ra file CSV":
            result = service.export_data(filename, "csv")
            if "thành công" in result.lower():
                st.success(result)
            else:
                st.error(result)
        elif option == "Export ra file JSON":
            result = service.export_data(filename, "json")
            if "thành công" in result.lower():
                st.success(result)
            else:
                st.error(result)


def menu_sinh_vien(service):
    operation = st.selectbox("Chọn thao tác", 
                             ("Thêm sinh viên", "Xóa sinh viên", "Cập nhật thông tin sinh viên", 
                              "Tìm kiếm sinh viên", "Hiển thị danh sách sinh viên", "Import/Export dữ liệu"))
    
    if operation == "Thêm sinh viên":
        st.subheader("Thêm sinh viên")
        # Thu thập thông tin sinh viên từ người dùng
        mssv = st.text_input("MSSV")
        ho_ten = st.text_input("Họ và tên")
        ngay_sinh = st.date_input("Ngày sinh", value=datetime.date.today(), min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())
        gioi_tinh = st.selectbox("Giới tính", ["Nam", "Nữ", "Khác"])
        khoa = st.selectbox("Khoa", [
                                        "Khoa Luật",
                                        "Khoa Tiếng Anh thương mại",
                                        "Khoa Tiếng Nhật",
                                        "Khoa Tiếng Pháp",
                                        "Khoa Báo Chí"
                                    ])
        khoa_hoc = st.text_input("Khóa")
        chuong_trinh = st.selectbox("Chương trình đào tạo", [
                                                                "Chất lượng cao",
                                                                "Chuẩn",
                                                                "Tiên tiến",
                                                                "Tăng cường tiếng Anh"
                                                            ])
        dia_chi = st.text_input("Địa chỉ")
        email = st.text_input("Email")
        sdt = st.text_input("Số điện thoại")
        tinh_trang = st.selectbox("Tình trạng", [
                                                    "Đang học",
                                                    "Đã tốt nghiệp",
                                                    "Đã thôi học",
                                                    "Tạm dừng học",
                                                    "Bảo lưu kết quả"
                                                ])

        if st.button("Thêm sinh viên"):
            # Chuyển đổi đối tượng date thành chuỗi theo định dạng dd/mm/yyyy
            ngay_sinh_str = ngay_sinh.strftime("%d/%m/%Y")
            # Tạo dictionary chứa dữ liệu sinh viên
            student_data = {
                "mssv": mssv,
                "ho_ten": ho_ten,
                "ngay_sinh": ngay_sinh_str,
                "gioi_tinh": gioi_tinh,
                "khoa": khoa,
                "khoa_hoc": khoa_hoc,
                "chuong_trinh": chuong_trinh,
                "dia_chi": dia_chi,
                "email": email,
                "sdt": sdt,
                "tinh_trang": tinh_trang,
            }
            # Gọi hàm thêm sinh viên và nhận kết quả trả về
            result = service.them_sinh_vien(student_data)
            if "thành công" in result.lower():
                st.success(result)
            else:
                st.error(result)
    
    elif operation == "Xóa sinh viên":
        st.subheader("Xóa sinh viên")
        mssv = st.text_input("Nhập MSSV của sinh viên cần xóa")
        if st.button("Xóa"):
            result = service.xoa_sinh_vien(mssv)
            if "Đã xóa" in result:
                st.success(result)
            else:
                st.error(result)

    
    elif operation == "Cập nhật thông tin sinh viên":
        st.subheader("Cập nhật sinh viên")
        st.info("Nhập thông tin mới cho các trường cần cập nhật. Để trống nếu không muốn thay đổi giá trị.")
        mssv = st.text_input("Nhập MSSV của sinh viên cần cập nhật")
        ho_ten = st.text_input("Họ và tên mới")
        ngay_sinh = st.date_input("Ngày sinh mới", value=datetime.date.today(), min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())
        gioi_tinh = st.selectbox("Giới tính mới", ["Trống", "Nam", "Nữ", "Khác"])
        khoa = st.selectbox("Khoa mới", ["Trống",
                                        "Khoa Luật",
                                        "Khoa Tiếng Anh thương mại",
                                        "Khoa Tiếng Nhật",
                                        "Khoa Tiếng Pháp",
                                        "Khoa Báo Chí"
                                    ])
        khoa_hoc = st.text_input("Khóa mới")
        chuong_trinh = st.selectbox("Chương trình đào tạo mới", ["Trống",
                                                                "Chất lượng cao",
                                                                "Chuẩn",
                                                                "Tiên tiến",
                                                                "Tăng cường tiếng Anh"
                                                            ])
        dia_chi = st.text_input("Địa chỉ mới")
        email = st.text_input("Email mới")
        sdt = st.text_input("Số điện thoại mới")
        tinh_trang = st.selectbox("Tình trạng mới", ["Trống",
                                                    "Đang học",
                                                    "Đã tốt nghiệp",
                                                    "Đã thôi học",
                                                    "Tạm dừng học",
                                                    "Bảo lưu kết quả"
                                                ])
        
        if st.button("Cập nhật"):
            updated_data = {}
            if ho_ten:
                updated_data["ho_ten"] = ho_ten
            # Nếu người dùng thay đổi ngày sinh, chuyển đối tượng date thành chuỗi định dạng dd/mm/yyyy
            if ngay_sinh:
                updated_data["ngay_sinh"] = ngay_sinh.strftime("%d/%m/%Y")
            if gioi_tinh:
                updated_data["gioi_tinh"] = gioi_tinh
            if khoa and khoa != "Trống":
                updated_data["khoa"] = khoa
            if khoa_hoc:
                updated_data["khoa_hoc"] = khoa_hoc
            if chuong_trinh and chuong_trinh != "Trống":
                updated_data["chuong_trinh"] = chuong_trinh
            if dia_chi:
                updated_data["dia_chi"] = dia_chi
            if email:
                updated_data["email"] = email
            if sdt:
                updated_data["sdt"] = sdt
            if tinh_trang and tinh_trang != "Trống":
                updated_data["tinh_trang"] = tinh_trang

            result = service.cap_nhat_sinh_vien(mssv, updated_data)
            if "thành công" in result.lower():
                st.success(result)
            else:
                st.error(result)

    
    elif operation == "Tìm kiếm sinh viên":
        st.subheader("Tìm kiếm sinh viên")
        # Cho người dùng lựa chọn tiêu chí tìm kiếm
        criteria = st.selectbox(
            "Chọn tiêu chí tìm kiếm",
            ("Họ tên", "MSSV", "Khoa", "Khoa & Họ tên")
        )

        # Nhập giá trị tìm kiếm chính
        value = st.text_input("Nhập giá trị tìm kiếm")

        # Nếu tiêu chí là "Khoa & Họ tên", cho phép nhập thêm một giá trị phụ
        additional_value = ""
        if criteria == "Khoa & Họ tên":
            additional_value = st.text_input("Nhập tên cần tìm (Họ tên)")

        if st.button("Tìm kiếm"):
            # Map tiêu chí hiển thị sang các key tương ứng của hàm tim_kiem_sinh_vien
            criteria_map = {
                "Họ tên": "ho_ten",
                "MSSV": "mssv",
                "Khoa": "khoa",
                "Khoa & Họ tên": "khoa_ho_ten"
            }
            # Gọi hàm tìm kiếm và nhận kết quả trả về là danh sách các dict
            result = service.tim_kiem_sinh_vien(criteria_map[criteria], value, additional_value)
            
            if result:
                df = pd.DataFrame(result)
                st.dataframe(df)
            else:
                st.info("Không tìm thấy sinh viên nào.")
    
    elif operation == "Hiển thị danh sách sinh viên":
        st.subheader("Danh sách sinh viên")
        data = service.hien_thi_danh_sach()
        if data:
            # Chuyển đổi list of dict thành DataFrame để hiển thị đẹp hơn
            df = pd.DataFrame(data)
            st.dataframe(df)
        else:
            st.info("Danh sách sinh viên đang rỗng.")
    
    elif operation == "Import/Export dữ liệu":
        menu_import_export(service)

def menu_khoa(service):
    operation = st.selectbox(
        "Chọn thao tác", 
        ("Thêm khoa", "Sửa khoa", "Hiển thị danh sách khoa")
    )
    
    if operation == "Thêm khoa":
        st.subheader("Thêm khoa")
        ten_khoa = st.text_input("Nhập tên khoa mới", key="them_khoa")
        if st.button("Thêm khoa"):
            result = service.them_khoa(ten_khoa)
            if "thành công" in result.lower():
                st.success(result)
            else:
                st.error(result)
    
    elif operation == "Sửa khoa":
        st.subheader("Sửa khoa")
        # Lấy danh sách khoa để hiển thị dưới dạng dropdown
        ds_khoa = service.hien_thi_danh_sach_khoa()
        if ds_khoa:
            ten_khoa_cu = st.selectbox("Chọn khoa cần sửa", ds_khoa, key="chon_khoa")
            ten_khoa_moi = st.text_input("Nhập tên khoa mới", key="sua_khoa")
            if st.button("Sửa khoa"):
                result = service.sua_khoa(ten_khoa_cu, ten_khoa_moi)
                if "thành công" in result.lower():
                    st.success(result)
                else:
                    st.error(result)
        else:
            st.info("Danh sách khoa rỗng. Không có khoa nào để sửa.")
    
    elif operation == "Hiển thị danh sách khoa":
        st.subheader("Danh sách khoa")
        ds_khoa = service.hien_thi_danh_sach_khoa()
        if ds_khoa:
            df = pd.DataFrame(ds_khoa)
            st.dataframe(df)
        else:
            st.info("Danh sách khoa rỗng.")

def menu_chuong_trinh(service):
    operation = st.selectbox(
        "Chọn thao tác", 
        ("Thêm chương trình đào tạo", "Sửa chương trình đào tạo", "Hiển thị danh sách chương trình đào tạo")
    )
    
    if operation == "Thêm chương trình đào tạo":
        st.subheader("Thêm chương trình đào tạo")
        ten_ct = st.text_input("Nhập tên chương trình đào tạo mới", key="them_ct")
        if st.button("Thêm chương trình đào tạo"):
            result = service.them_chuong_trinh(ten_ct)
            if "thành công" in result.lower():
                st.success(result)
            else:
                st.error(result)
    
    elif operation == "Sửa chương trình đào tạo":
        st.subheader("Sửa chương trình đào tạo")
        ds_ct = service.hien_thi_danh_sach_chuong_trinh()
        if ds_ct:
            ten_ct_cu = st.selectbox("Chọn chương trình cần sửa", ds_ct, key="chon_ct")
            ten_ct_moi = st.text_input("Nhập tên chương trình đào tạo mới", key="sua_ct")
            if st.button("Sửa chương trình đào tạo"):
                result = service.sua_chuong_trinh(ten_ct_cu, ten_ct_moi)
                if "thành công" in result.lower():
                    st.success(result)
                else:
                    st.error(result)
        else:
            st.info("Danh sách chương trình đào tạo rỗng.")
    
    elif operation == "Hiển thị danh sách chương trình đào tạo":
        st.subheader("Danh sách chương trình đào tạo")
        ds_ct = service.hien_thi_danh_sach_chuong_trinh()
        if ds_ct:
            df = pd.DataFrame(ds_ct)
            st.dataframe(df)
        else:
            st.info("Danh sách chương trình đào tạo rỗng.")

def menu_tinh_trang(service):
    operation = st.selectbox(
        "Chọn thao tác", 
        ("Thêm tình trạng", "Sửa tình trạng", "Hiển thị danh sách tình trạng")
    )
    
    if operation == "Thêm tình trạng":
        st.subheader("Thêm tình trạng mới")
        ten_tt = st.text_input("Nhập tên tình trạng mới", key="them_tt")
        if st.button("Thêm tình trạng"):
            result = service.them_tinh_trang(ten_tt)
            if "thành công" in result.lower():
                st.success(result)
            else:
                st.error(result)
    
    elif operation == "Sửa tình trạng":
        st.subheader("Sửa tình trạng")
        ds_tt = service.hien_thi_danh_sach_tinh_trang()
        if ds_tt:
            ten_tt_cu = st.selectbox("Chọn tình trạng cần sửa", ds_tt, key="chon_tt")
            ten_tt_moi = st.text_input("Nhập tên tình trạng mới", key="sua_tt")
            if st.button("Sửa tình trạng"):
                result = service.sua_tinh_trang(ten_tt_cu, ten_tt_moi)
                if "thành công" in result.lower():
                    st.success(result)
                else:
                    st.error(result)
        else:
            st.info("Danh sách tình trạng rỗng.")
    
    elif operation == "Hiển thị danh sách tình trạng":
        st.subheader("Danh sách tình trạng")
        ds_tt = service.hien_thi_danh_sach_tinh_trang()
        if ds_tt:
            df = pd.DataFrame(ds_tt)
            st.dataframe(df)
        else:
            st.info("Danh sách tình trạng rỗng.")

def main():
    st.markdown(
        """
        <style>
        body {
            background-color: #FFFFFF;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center;'>🌟 HỆ THỐNG QUẢN LÝ 🌟</h1>", unsafe_allow_html=True)
    st.write("---")
    
    st.sidebar.header("HỆ THỐNG QUẢN LÝ SINH VIÊN")
    try:
        image = Image.open("logo.jpg")

        # Scale ảnh mà không giảm chất lượng
        new_width = 300  # Thay đổi theo nhu cầu
        aspect_ratio = image.height / image.width
        new_height = int(new_width * aspect_ratio)

        resized_image = image.resize((new_width, new_height), Image.LANCZOS)

        st.sidebar.image(resized_image, use_column_width=True)
    except Exception as e:
        st.sidebar.text("LOGO")
    
    menu = st.sidebar.selectbox(
        "CHỌN MỤC QUẢN LÝ", 
        (
            "QUẢN LÝ SINH VIÊN", 
            "QUẢN LÝ KHOA", 
            "QUẢN LÝ CHƯƠNG TRÌNH ĐÀO TẠO", 
            "QUẢN LÝ TÌNH TRẠNG", 
            "THÔNG TIN PHIÊN BẢN"
        )
    )
    
    # Khởi tạo các đối tượng service
    sinhvien_service = SinhVienService()
    khoa_service = KhoaService()
    chuong_trinh_service = ChuongTrinhService()
    tinh_trang_service = TinhTrangService()
    
    # Nội dung chính
    with st.container():
        if menu == "QUẢN LÝ SINH VIÊN":
            st.markdown("<h2 style='text-align:center;'>👩 QUẢN LÝ SINH VIÊN</h2>", unsafe_allow_html=True)
            menu_sinh_vien(sinhvien_service)
        elif menu == "QUẢN LÝ KHOA":
            st.markdown("<h2 style='text-align:center;'>🏫 QUẢN LÝ KHOA</h2>", unsafe_allow_html=True)
            menu_khoa(khoa_service)
        elif menu == "QUẢN LÝ CHƯƠNG TRÌNH ĐÀO TẠO":
            st.markdown("<h2 style='text-align:center;'>🎓 QUẢN LÝ CHƯƠNG TRÌNH ĐÀO TẠO</h2>", unsafe_allow_html=True)
            menu_chuong_trinh(chuong_trinh_service)
        elif menu == "QUẢN LÝ TÌNH TRẠNG":
            st.markdown("<h2 style='text-align:center;'>📊 QUẢN LÝ TÌNH TRẠNG</h2>", unsafe_allow_html=True)
            menu_tinh_trang(tinh_trang_service)
        elif menu == "THÔNG TIN PHIÊN BẢN":
            st.markdown("<h2 style='text-align:center;'>ℹ️ THÔNG TIN PHIÊN BẢN</h2>", unsafe_allow_html=True)
            show_version()

if __name__ == "__main__":
    main()