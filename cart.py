import re
from datetime import datetime
import base36


def get_numbers(s, max_len):
    numbers = re.findall(r'\d+', s)
    res = [int(num) for num in numbers]
    if len(res) != max_len:
        return False

    return res


def get_address(text):
    zip_code = r'\b\d{4}-\d{3}\b'
    match = re.search(zip_code, text)
    if match:
        return match.group()

    return None


def get_phone(text):
    phone = re.sub(r'\D', '', text)
    if phone == '' or len(phone) < 6 or len(phone) > 12:
        return False

    return phone


def get_orderid():
    orderid = int(datetime.now().strftime("%m%d%H%M%S"))
    res = base36.dumps(orderid).upper()

    return res
