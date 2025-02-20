from services.sinhvien_service import SinhVienService
from services.khoa_service import KhoaService

def main():
  sinhvien_service = SinhVienService()
  khoa_service = KhoaService() 


  while True:
    print("\n----- QUẢN LÝ SINH VIÊN -----")
    print("1. Thêm sinh viên")
    print("2. Xóa sinh viên")
    print("3. Cập nhật thông tin sinh viên")
    print("4. Tìm kiếm sinh viên")
    print("5. Hiển thị danh sách sinh viên")
    print("6. Thêm khoa")          
    print("7. Sửa khoa")          
    print("8. Hiển thị danh sách khoa")
    print("0. Thoát")

    lua_chon = input("Nhập lựa chọn của bạn: ")

    if lua_chon == '1':
      sinhvien_service.them_sinh_vien()
    elif lua_chon == '2':
      sinhvien_service.xoa_sinh_vien()
    elif lua_chon == '3':
      sinhvien_service.cap_nhat_sinh_vien()
    elif lua_chon == '4':
      sinhvien_service.tim_kiem_sinh_vien()
    elif lua_chon == '5':
      sinhvien_service.hien_thi_danh_sach()
    elif lua_chon == '6':
      khoa_service.them_khoa()     
    elif lua_chon == '7':
      khoa_service.sua_khoa()      
    elif lua_chon == '8':
      khoa_service.hien_thi_danh_sach_khoa()
    elif lua_chon == '0':
      print("Thoát chương trình.")
      break
    else:
      print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
  main()