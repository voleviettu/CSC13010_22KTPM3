import json
import csv
from models.sinhvien import SinhVien  

def load_json_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_json_file(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_csv_file(filename):
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                data.append(row)
            return data
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Lỗi khi đọc file CSV: {e}")
        return []


def save_csv_file(data, filename):
    if not data:
        print("Không có dữ liệu để xuất.")
        return

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            # Lấy header từ dictionary đầu tiên trong danh sách
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()  # Ghi header
            for row in data:
                writer.writerow(row)
    except Exception as e:
        print(f"Lỗi khi ghi file CSV: {e}")


def load_sinhvien_data(filename="data/sinhvien.json", file_type="json"):
    try:
        if file_type == "json":
            data = load_json_file(filename)
        elif file_type == "csv":
            data = load_csv_file(filename)
        else:
            print("Loại file không được hỗ trợ.")
            return []

        return [SinhVien(**item) for item in data]
    except Exception as e:
        print(f"Lỗi khi load dữ liệu sinh viên: {e}")
        return []


def save_sinhvien_data(
    danh_sach_sinh_vien, filename="data/sinhvien.json", file_type="json"
):
    data = [sv.to_dict() for sv in danh_sach_sinh_vien]
    try:
        if file_type == "json":
            save_json_file(data, filename)
        elif file_type == "csv":
            save_csv_file(data, filename)
        else:
            print("Loại file không được hỗ trợ.")
    except Exception as e:
        print(f"Lỗi khi lưu dữ liệu sinh viên {e}")
