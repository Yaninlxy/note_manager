import uuid

def generate_note_id():
    """
    Генерирует уникальный идентификатор для заметки.
    """
    return str(uuid.uuid4())
