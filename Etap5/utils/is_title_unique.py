def is_title_unique(notes, title):
    """
    Проверяет, что заголовок заметки уникален в списке.
    """
    for note in notes:
        if note.get("title") == title:
            return False, f"Заметка с заголовком '{title}' уже существует."
    return True, "Заголовок уникален"
