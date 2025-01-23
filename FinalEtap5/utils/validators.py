import uuid

def generate_note_id():
    """
    Генерирует уникальный идентификатор для заметки.
    """
    return str(uuid.uuid4())

def is_title_unique(notes, title):
    """
    Проверяет, что заголовок заметки уникален в списке.
    """
    for note in notes:
        if note.get("title") == title:
            return False, f"Заметка с заголовком '{title}' уже существует."
    return True, "Заголовок уникален"

def log_message(message, level="INFO"):
    """
    Логирует сообщение с указанным уровнем.
    """
    levels = {"INFO": "ℹ️", "WARNING": "⚠️", "ERROR": "❌"}
    prefix = levels.get(level.upper(), "ℹ️")
    print(f"{prefix} {message}")
    
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

def validate_note_structure(note):
    """
    Проверяет, что заметка содержит все обязательные поля.
    """
    required_fields = {
        "username", 
        "title", 
        "content", 
        "status", 
        "created_date", 
        "issue_date"
    }
    missing_fields = required_fields - note.keys()
    if missing_fields:
        return False, f"Отсутствуют обязательные поля: {', '.join(missing_fields)}"
    return True, "Заметка валидна"

def validate_status(status):
    """
    Проверяет, что статус заметки является допустимым.
    """
    valid_statuses = {"новая", "в процессе", "завершена"}
    if status not in valid_statuses:
        return False, f"Некорректный статус: {status}. Допустимые статусы: {', '.join(valid_statuses)}"
    return True, "Статус валиден"
