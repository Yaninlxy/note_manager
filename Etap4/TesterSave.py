from save_notes_to_file import save_notes_to_file


if __name__ == "__main__":
    # Пример списка заметок
    notes = [
        {
            "username": "Алексей",
            "title": "Список покупок",
            "content": "Купить молоко, хлеб, яйца",
            "status": "новая",
            "created_date": "07-01-2025",
            "issue_date": "08-01-2025"
        },
        {
            "username": "Мария",
            "title": "Планы на выходные",
            "content": "Поехать в парк, встретиться с друзьями",
            "status": "выполнена",
            "created_date": "08-01-2025",
            "issue_date": "09-01-2025"
        }
    ]

    # Сохранение заметок в файл
    save_notes_to_file(notes, "notes.txt")
