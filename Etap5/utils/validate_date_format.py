from datetime import datetime

def validate_date_format(date_str, date_format="%d-%m-%Y"):
    """
    Проверяет, что дата имеет корректный формат.
    """
    try:
        datetime.strptime(date_str, date_format)
        return True, "Дата валидна"
    except ValueError:
        return False, f"Некорректный формат даты: {date_str}. Ожидаемый формат: {date_format}"
