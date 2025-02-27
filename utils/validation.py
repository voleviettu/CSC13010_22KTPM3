import re
import datetime
import logging
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler("app.log", encoding="utf-8")
])

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# Cấu hình tên miền hợp lệ
VALID_EMAIL = config['VALID_EMAIL']

# Cấu hình định dạng số điện thoại hợp lệ (Việt Nam)
VALID_MOBILE = config['VALID_MOBILE']

VALID_STATUS = config['VALID_STATUS']

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
    
def kiem_tra_trang_thai(old_status: str, new_status: str) -> bool:
    allowed_transition = [s for s in VALID_STATUS.get(old_status, [])]
    print(allowed_transition)
    if new_status in allowed_transition:
        logging.info(f'Tình trạng hợp lệ: {new_status}')
        return True
    else:
        logging.warning(f"Tình trạng không hợp lệ: {new_status}")
        return False
        