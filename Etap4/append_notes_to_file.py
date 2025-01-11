def append_notes_to_file(notes, filename):
    """
    Добавляет новые заметки в существующий файл.

    :param notes: Список новых заметок (каждая заметка — словарь).
    :param filename: Имя файла для добавления заметок.
    """
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            for note in notes:
                file.write(f"Имя пользователя: {note.get('username', '')}\n")
                file.write(f"Заголовок: {note.get('title', '')}\n")
                file.write(f"Описание: {note.get('content', '')}\n")
                file.write(f"Статус: {note.get('status', '')}\n")
                file.write(f"Дата создания: {note.get('created_date', '')}\n")
                file.write(f"Дедлайн: {note.get('issue_date', '')}\n")
                file.write("---\n")
        print(f"Заметки успешно добавлены в файл {filename}.")
    except Exception as e:
        print(f"Ошибка при добавлении заметок: {e}")

if __name__ == "__main__":
    # Пример использования
    new_notes = [
        {
            "username": "Алексей",
            "title": "Покупка подарков",
            "content": "Купить подарок на день рождения",
            "status": "новая",
            "created_date": "05-01-2025",
            "issue_date": "10-01-2025"
        },
        {
            "username": "Кэт",
            "title": "Жизнь кэт",
            "content": "поесть, по спать, по мурчать",
            "status": "в процессе",
            "created_date": "04-01-2025",
            "issue_date": "20-01-2025"
        },
        {
            "username": "Аннет",
            "title": "Работа",
            "content": "24/7",
            "status": "в процессе",
            "created_date": "11-01-2025",
            "issue_date": "12-01-2025"
        }
    ]

    append_notes_to_file(new_notes, "notesappend.txt")
