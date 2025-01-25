from db_operations import (
    create_table,
    save_note_to_db,
    load_notes_from_db,
    update_note_in_db,
    delete_note_from_db,
    search_notes_by_keyword,
    filter_notes_by_status
)

def add_note_handler(db_path):
    """
    Обработчик для добавления заметки.
    """
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержимое заметки: ")
    status = input("Введите статус заметки (Например: В процессе, Завершено): ")
    created_date = input("Введите дату создания (в формате ДД-ММ-ГГГГ): ")
    issue_date = input("Введите дату выполнения (в формате ДД-ММ-ГГГГ): ")

    note = {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date
    }

    save_note_to_db(note, db_path)

def list_notes_handler(db_path):
    """
    Обработчик для отображения всех заметок.
    """
    notes = load_notes_from_db(db_path)
    if notes:
        print("Все заметки:")
        for note in notes:
            print(
                f"ID: {note['id']}, Пользователь: {note['username']}, Заголовок: {note['title']}, "
                f"Статус: {note['status']}, Дата создания: {note['created_date']}, "
                f"Дата выполнения: {note['issue_date']}"
            )
    else:
        print("Заметки отсутствуют.")

def update_note_handler(db_path):
    """
    Обработчик для обновления заметки.
    """
    note_id = input("Введите ID заметки для обновления: ")
    title = input("Введите новый заголовок заметки: ")
    content = input("Введите новое содержимое заметки: ")
    status = input("Введите новый статус заметки: ")
    issue_date = input("Введите новую дату выполнения (в формате ДД-ММ-ГГГГ): ")

    updates = {
        "title": title,
        "content": content,
        "status": status,
        "issue_date": issue_date
    }

    update_note_in_db(note_id, updates, db_path)

def delete_note_handler(db_path):
    """
    Обработчик для удаления заметки.
    """
    note_id = input("Введите ID заметки для удаления: ")
    delete_note_from_db(note_id, db_path)

def search_notes_handler(db_path):
    """
    Обработчик поиска заметок по ключевому слову.
    """
    keyword = input("Введите ключевое слово для поиска: ")
    notes = search_notes_by_keyword(keyword, db_path)
    if notes:
        print("Результаты поиска:")
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Содержимое: {note['content']}")
    else:
        print("Заметки с таким ключевым словом не найдены.")

def filter_notes_handler(db_path):
    """
    Обработчик фильтрации заметок по статусу.
    """
    status = input("Введите статус для фильтрации (Например: В процессе, Завершено): ")
    notes = filter_notes_by_status(status, db_path)
    if notes:
        print("Результаты фильтрации:")
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Статус: {note['status']}")
    else:
        print(f"Заметки со статусом '{status}' не найдены.")

def main():
    db_path = 'note_manager.db'
    create_table(db_path)

    while True:
        print("\nМеню:")
        print("1. Добавить заметку")
        print("2. Обновить заметку")
        print("3. Удалить заметку")
        print("4. Показать все заметки")
        print("5. Найти заметку по ключевому слову")
        print("6. Отфильтровать заметки по статусу")
        print("7. Выйти")

        choice = input("Выберите действие (1-7): ")
        if choice == '1':
            add_note_handler(db_path)
        elif choice == '2':
            update_note_handler(db_path)
        elif choice == '3':
            delete_note_handler(db_path)
        elif choice == '4':
            list_notes_handler(db_path)
        elif choice == '5':
            search_notes_handler(db_path)
        elif choice == '6':
            filter_notes_handler(db_path)
        elif choice == '7':
            print("Выход из программы.")
            break
        else:
            print("Ошибка: выберите действие от 1 до 7.")

if __name__ == "__main__":
    main()
