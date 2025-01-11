import json

def save_notes_json(notes, filename):
    """
    Сохраняет список заметок в файл в формате JSON.

    :param notes: Список заметок (каждая заметка — словарь).
    :param filename: Имя файла для сохранения заметок.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
        print(f"Заметки успешно сохранены в файл {filename}.")
    except Exception as e:
        print(f"Ошибка при сохранении заметок: {e}")

if __name__ == "__main__":
    # Пример использования
    notes = [
        {
            "username": "Алексей",
            "title": "Список покупок",
            "content": "Купить продукты",
            "status": "новая",
            "created_date": "11-01-2025",
            "issue_date": "12-01-2025"
        },
        {
            "username": "Мария",
            "title": "Подготовка к уборке",
            "content": "Пылесосим, моем",
            "status": "в процессе",
            "created_date": "11-01-2025",
            "issue_date": "12-01-2025"
        }
    ]

    save_notes_json(notes, "notes.json")
