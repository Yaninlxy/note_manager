from datetime import datetime
import uuid

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        return False

def validate_status(status):
    return status in ['новая', 'в процессе', 'выполнена']

def generate_unique_id():
    return str(uuid.uuid4())
