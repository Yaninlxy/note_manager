def validate_status(status):
    """
    Проверяет, что статус заметки является допустимым.
    """
    valid_statuses = {"новая", "в процессе", "завершена"}
    if status not in valid_statuses:
        return False, f"Некорректный статус: {status}. Допустимые статусы: {', '.join(valid_statuses)}"
    return True, "Статус валиден"
