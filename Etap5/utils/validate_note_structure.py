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
