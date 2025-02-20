import json

def load_json_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_json_file(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_sinhvien_data(filename="data/sinhvien.json"):
    from models.sinhvien import SinhVien  # Tránh import vòng tròn
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [SinhVien(**item) for item in data]  # Sử dụng dictionary unpacking
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_sinhvien_data(danh_sach_sinh_vien, filename="data/sinhvien.json"):
    data = [sv.to_dict() for sv in danh_sach_sinh_vien]
    save_json_file(data, filename)