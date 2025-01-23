from datetime import datetime
import uuid

def validate_date(date_str):
    """
    Проверяет, соответствует ли дата формату "дд-мм-гггг".
    """
    try:
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        return False


def validate_status(status):
    """
    Проверяет, что статус находится в допустимом списке.
    """
    return status in ['новая', 'в процессе', 'выполнена']


def generate_unique_id():
    """
    Генерирует уникальный идентификатор.
    """
    return str(uuid.uuid4())
