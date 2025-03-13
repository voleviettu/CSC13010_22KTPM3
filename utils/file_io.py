import json
import csv
import logging
import datetime
from models.sinhvien import SinhVien

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler("app.log", encoding="utf-8"),
])

def load_json_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            logging.info(f"Đang tải file JSON: {filename}")
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Lỗi khi tải file JSON {filename}: {e}")
        return []

def save_json_file(data, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            logging.info(f"Đã lưu file JSON: {filename}")
    except Exception as e:
        logging.error(f"Lỗi khi lưu file JSON {filename}: {e}")

def load_csv_file(filename):
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            logging.info(f"Đang tải file CSV: {filename}")
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                data.append(row)
            return data
    except FileNotFoundError as e:
        logging.error(f"Không tìm thấy file: {filename}")
        return []
    except Exception as e:
        logging.error(f"Lỗi khi đọc file CSV {filename}: {e}")
        return []

def save_csv_file(data, filename):
    if not data:
        logging.warning("Không có dữ liệu để xuất.")
        return

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
            logging.info(f"Đã lưu file CSV: {filename}")
    except Exception as e:
        logging.error(f"Lỗi khi lưu file CSV {filename}: {e}")

def load_sinhvien_data(filename="data/sinhvien", file_type="json"):
    try:
        if file_type == "json":
            data = load_json_file(filename+'.json')
        elif file_type == "csv":
            data = load_csv_file(filename+'.csv')
        else:
            logging.error("Loại file không được hỗ trợ.")
            return []

        logging.info(f"Đã tải dữ liệu sinh viên từ {filename}")
        sinhviens = []
        for item in data:
            # Chuyển đổi creation_datetime từ string (ISO format) về datetime object
            if 'creation_datetime' in item:  # Kiểm tra xem có trường này không
                item['creation_datetime'] = datetime.datetime.fromisoformat(item['creation_datetime'])
            sinhviens.append(SinhVien(**item))  # Tạo đối tượng SinhVien
        return sinhviens
    except Exception as e:
        logging.error(f"Lỗi khi tải dữ liệu sinh viên: {e}")
        return []

def save_sinhvien_data(danh_sach_sinh_vien, filename="data/sinhvien", file_type="json"):
    data = [sv.to_dict() for sv in danh_sach_sinh_vien]
    try:
        if file_type == "json":
            save_json_file(data, filename+'.json')
        elif file_type == "csv":
            save_csv_file(data, filename+'.csv')
        else:
            logging.error("Loại file không được hỗ trợ.")
    except Exception as e:
        logging.error(f"Lỗi khi lưu dữ liệu sinh viên: {e}")