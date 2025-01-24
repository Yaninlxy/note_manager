from db_operations import create_table, save_note_to_db, load_notes_from_db, update_note_in_db, delete_note_from_db

if __name__ == "__main__":
    db_path = 'note_manager.db'

    # Создание таблицы
    create_table(db_path)

    # Добавление заметки
    note = {
        "username": "Alexey",
        "title": "Тестовая заметка",
        "content": "Содержимое тестовой заметки.",
        "status": "В процессе",
        "created_date": "23-01-2025",
        "issue_date": "25-01-2025"
    }
    save_note_to_db(note, db_path)

    # Загрузка заметок
    notes = load_notes_from_db(db_path)
    print("Загруженные заметки:", notes)

    # Обновление заметки
    updates = {
        "title": "Обновленная заметка",
        "content": "Обновленное содержимое.",
        "status": "Завершено",
        "issue_date": "26-01-2025"
    }
    update_note_in_db(note_id=1, updates=updates, db_path=db_path)

    # Удаление заметки
    delete_note_from_db(note_id=1, db_path=db_path)
