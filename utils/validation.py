import re
import datetime


def kiem_tra_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def kiem_tra_sdt(sdt):
    pattern = r"^(0|\+84)(\d{9})$"
    return re.match(pattern, sdt) is not None


def kiem_tra_ngay_sinh(ngay_sinh):
    try:
        datetime.datetime.strptime(ngay_sinh, "%d/%m/%Y")
        return True
    except ValueError:
        return False
