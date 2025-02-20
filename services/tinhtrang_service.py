from utils.file_io import load_json_file, save_json_file
import json

class TinhTrangService:
  def __init__(self, tinh_trang_file="data/tinhtrang.json"):
    self.tinh_trang_file = tinh_trang_file
    self.danh_sach_tinh_trang = load_json_file(tinh_trang_file)

  def them_tinh_trang(self):
    print("\nThêm tình trạng mới:")
    ten_tinh_trang_moi = self._nhap_ten_tinh_trang()
    self.danh_sach_tinh_trang.append(ten_tinh_trang_moi)
    self.save_data()
    print(f"Đã thêm tình trạng '{ten_tinh_trang_moi}' thành công.")

  def sua_tinh_trang(self):
    print("\nSửa tên tình trạng:")
    ten_tinh_trang_cu = self._chon_tinh_trang()
    if ten_tinh_trang_cu:
      ten_tinh_trang_moi = self._nhap_ten_tinh_trang(ten_tinh_trang_cu)
      index = self.danh_sach_tinh_trang.index(ten_tinh_trang_cu)
      self.danh_sach_tinh_trang[index] = ten_tinh_trang_moi
      self.save_data()
      print(f"Đã sửa tình trạng '{ten_tinh_trang_cu}' thành '{ten_tinh_trang_moi}'.")

  def hien_thi_danh_sach_tinh_trang(self):
    print("\nDanh sách tình trạng:")
    if not self.danh_sach_tinh_trang:
      print("[]")
    else:
      print(json.dumps(self.danh_sach_tinh_trang, indent=2, ensure_ascii=False))

  def _nhap_ten_tinh_trang(self, ten_tinh_trang_cu=None):
    while True:
      if ten_tinh_trang_cu:
        ten_tinh_trang = input(f"Nhập tên tình trạng mới (hoặc Enter để giữ nguyên '{ten_tinh_trang_cu}'): ") or ten_tinh_trang_cu
      else:
        ten_tinh_trang = input("Nhập tên tình trạng: ")

      if ten_tinh_trang not in self.danh_sach_tinh_trang:
        return ten_tinh_trang
      else:
        print(f"Tên tình trạng '{ten_tinh_trang}' đã tồn tại. Vui lòng nhập tên khác.")

  def _chon_tinh_trang(self):
    self.hien_thi_danh_sach_tinh_trang()
    while True:
      ten_tinh_trang = input("Nhập tên tình trạng bạn muốn chỉnh sửa: ")
      if ten_tinh_trang in self.danh_sach_tinh_trang:
        return ten_tinh_trang
      else:
        print("Tên tình trạng không tồn tại. Vui lòng chọn lại.")
  def save_data(self):
    save_json_file(self.danh_sach_tinh_trang, self.tinh_trang_file)