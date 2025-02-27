import re
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler("app.log", encoding="utf-8")
])

# Cấu hình tên miền hợp lệ
VALID_EMAIL = "student.university.edu.vn"

# Cấu hình định dạng số điện thoại hợp lệ (Việt Nam)
VALID_MOBILE = r"^(0[3|5|7|8|9]\d{8}|\+84[3|5|7|8|9]\d{8})$"

def kiem_tra_email(email, domain=VALID_EMAIL):
    pattern = rf"^[a-zA-Z0-9._%+-]+@{re.escape(domain)}$"
    result = re.match(pattern, email) is not None
    if result:
        logging.info(f"Email hợp lệ: {email}")
    else:
        logging.warning(f"Email không hợp lệ: {email}")
    return result

def kiem_tra_sdt(sdt, pattern=VALID_MOBILE):
    result = re.match(pattern, sdt) is not None
    if result:
        logging.info(f"Số điện thoại hợp lệ: {sdt}")
    else:
        logging.warning(f"Số điện thoại không hợp lệ: {sdt}")
    return result

def kiem_tra_ngay_sinh(ngay_sinh):
    try:
        datetime.datetime.strptime(ngay_sinh, "%d/%m/%Y")
        logging.info(f"Ngày sinh hợp lệ: {ngay_sinh}")
        return True
    except ValueError:
        logging.warning(f"Ngày sinh không hợp lệ: {ngay_sinh}")
        return False